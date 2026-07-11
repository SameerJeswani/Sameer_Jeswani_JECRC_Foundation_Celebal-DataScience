import os
import json
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

print("RUNNING MY NEW PROJECT")


pipeline = joblib.load(os.path.join(BASE_DIR, 'model_artifacts', 'lead_scoring_pipeline.joblib'))
with open(os.path.join(BASE_DIR, 'model_artifacts', 'metadata.json')) as f:
    METADATA = json.load(f)

NUMERIC_FEATURES = METADATA['numeric_features']
BINARY_FEATURES = METADATA['binary_features']
CATEGORICAL_FEATURES = METADATA['categorical_features']
CATEGORICAL_OPTIONS = METADATA['categorical_options']
METRICS = METADATA['metrics']

DEFAULTS = {
    'TotalVisits': 3,
    'Total Time Spent on Website': 300,
    'Page Views Per Visit': 2.5,
    'Do Not Email': 'No',
    'A free copy of Mastering The Interview': 'No',
    'Lead Origin': 'Landing Page Submission',
    'Lead Source': 'Google',
    'Last Activity': 'Email Opened',
    'Specialization': 'Not Provided',
    'What is your current occupation': 'Unemployed',
    'City': 'Mumbai',
    'Last Notable Activity': 'Modified',
}


def score_to_tier(score):
    if score >= 80:
        return 'Hot Lead', 'hot'
    elif score >= 40:
        return 'Warm Lead', 'warm'
    else:
        return 'Cold Lead', 'cold'


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        numeric_features=NUMERIC_FEATURES,
        categorical_features=CATEGORICAL_FEATURES,
        categorical_options=CATEGORICAL_OPTIONS,
        defaults=DEFAULTS,
        metrics=METRICS,
        result=None,
    )


def build_input_row(form):
    row = {}
    for feat in NUMERIC_FEATURES:
        val = form.get(feat, DEFAULTS[feat])
        row[feat] = float(val)
    for feat in BINARY_FEATURES:
        row[feat] = 1 if form.get(feat, 'No') == 'Yes' else 0
    for feat in CATEGORICAL_FEATURES:
        row[feat] = form.get(feat, DEFAULTS[feat])
    return row


@app.route('/predict', methods=['POST'])
def predict():
    row = build_input_row(request.form)
    X = pd.DataFrame([row])
    prob = float(pipeline.predict_proba(X)[0, 1])
    score = int(round(prob * 100))
    tier, tier_class = score_to_tier(score)

    result = {
        'score': score,
        'probability': round(prob * 100, 1),
        'tier': tier,
        'tier_class': tier_class,
    }

    # merge submitted values back in so the form keeps user's inputs
    merged_defaults = dict(DEFAULTS)
    for feat in NUMERIC_FEATURES:
        merged_defaults[feat] = row[feat]
    for feat in BINARY_FEATURES:
        merged_defaults[feat] = 'Yes' if row[feat] == 1 else 'No'
    for feat in CATEGORICAL_FEATURES:
        merged_defaults[feat] = row[feat]

    return render_template(
        'index.html',
        numeric_features=NUMERIC_FEATURES,
        categorical_features=CATEGORICAL_FEATURES,
        categorical_options=CATEGORICAL_OPTIONS,
        defaults=merged_defaults,
        metrics=METRICS,
        result=result,
    )


@app.route('/api/predict', methods=['POST'])
def api_predict():
    """JSON API endpoint: POST a JSON body with the same field names."""
    data = request.get_json(force=True)
    row = {}
    for feat in NUMERIC_FEATURES:
        row[feat] = float(data.get(feat, DEFAULTS[feat]))
    for feat in BINARY_FEATURES:
        row[feat] = 1 if data.get(feat, 'No') == 'Yes' else 0
    for feat in CATEGORICAL_FEATURES:
        row[feat] = data.get(feat, DEFAULTS[feat])

    X = pd.DataFrame([row])
    prob = float(pipeline.predict_proba(X)[0, 1])
    score = int(round(prob * 100))
    tier, _ = score_to_tier(score)
    return jsonify({'lead_score': score, 'conversion_probability': round(prob, 4), 'tier': tier})


@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
