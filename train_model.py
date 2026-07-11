"""
Trains a deployment-friendly scikit-learn pipeline for the X Education
Lead Scoring project and saves it as model_artifacts/lead_scoring_pipeline.joblib

This mirrors the modelling approach used in the analysis notebook, but is
rebuilt as a single sklearn Pipeline (ColumnTransformer + LogisticRegression)
so it can be loaded and used for real-time predictions in the Flask web app.
"""
import pandas as pd
import numpy as np
import joblib
import json

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

df = pd.read_csv('model_artifacts/cleaned_data.csv')

# Group rare categories the same way as in the analysis notebook
def group_rare(series, threshold=100):
    counts = series.value_counts()
    rare = counts[counts < threshold].index
    return series.replace(rare, 'Other')

for col in ['Lead Source', 'Last Activity', 'Last Notable Activity']:
    df[col] = group_rare(df[col], threshold=100)
df['Lead Source'] = df['Lead Source'].replace({'google': 'Google'})

binary_map = {'Yes': 1, 'No': 0}
df['Do Not Email'] = df['Do Not Email'].map(binary_map)
df['A free copy of Mastering The Interview'] = df['A free copy of Mastering The Interview'].map(binary_map)

NUMERIC_FEATURES = ['TotalVisits', 'Total Time Spent on Website', 'Page Views Per Visit']
BINARY_FEATURES = ['Do Not Email', 'A free copy of Mastering The Interview']
CATEGORICAL_FEATURES = ['Lead Origin', 'Lead Source', 'Last Activity', 'Specialization',
                         'What is your current occupation', 'City', 'Last Notable Activity']

FEATURES = NUMERIC_FEATURES + BINARY_FEATURES + CATEGORICAL_FEATURES

X = df[FEATURES]
y = df['Converted']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, test_size=0.3, random_state=100, stratify=y)

preprocessor = ColumnTransformer(transformers=[
    ('num', MinMaxScaler(), NUMERIC_FEATURES),
    ('bin', 'passthrough', BINARY_FEATURES),
    ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'), CATEGORICAL_FEATURES),
])

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=2000, class_weight=None)),
])

pipeline.fit(X_train, y_train)

# Evaluate
train_probs = pipeline.predict_proba(X_train)[:, 1]
test_probs = pipeline.predict_proba(X_test)[:, 1]

CUTOFF = 0.4
train_preds = (train_probs > CUTOFF).astype(int)
test_preds = (test_probs > CUTOFF).astype(int)

train_acc = metrics.accuracy_score(y_train, train_preds)
test_acc = metrics.accuracy_score(y_test, test_preds)
test_auc = metrics.roc_auc_score(y_test, test_probs)
cm = metrics.confusion_matrix(y_test, test_preds)
test_sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])
test_specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

print(f"Train Accuracy: {train_acc:.4f}")
print(f"Test Accuracy:  {test_acc:.4f}")
print(f"Test AUC:       {test_auc:.4f}")
print(f"Test Sensitivity: {test_sensitivity:.4f}")
print(f"Test Specificity: {test_specificity:.4f}")

# Save pipeline
joblib.dump(pipeline, 'model_artifacts/lead_scoring_pipeline.joblib')

# Save metadata: dropdown options for the UI + feature lists + metrics
metadata = {
    "numeric_features": NUMERIC_FEATURES,
    "binary_features": BINARY_FEATURES,
    "categorical_features": CATEGORICAL_FEATURES,
    "categorical_options": {c: sorted([str(v) for v in df[c].dropna().unique()]) for c in CATEGORICAL_FEATURES},
    "cutoff": CUTOFF,
    "metrics": {
        "train_accuracy": round(train_acc, 4),
        "test_accuracy": round(test_acc, 4),
        "test_auc": round(test_auc, 4),
        "test_sensitivity": round(test_sensitivity, 4),
        "test_specificity": round(test_specificity, 4),
    }
}
with open('model_artifacts/metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print("\nSaved pipeline to model_artifacts/lead_scoring_pipeline.joblib")
print("Saved metadata to model_artifacts/metadata.json")
