🎯 X Education Lead Scoring System
Live Demo:
https://lead-scoring-project-ejhc.onrender.com
Note: This project is hosted on Render's free tier. If the application has been inactive for some time, it may take around 30–50 seconds to wake up.
📌 Project Overview
X Education receives a large number of leads from various online channels. However, only a small percentage of these leads convert into paying customers, causing sales teams to spend significant time on low-potential prospects.
This project implements a complete end-to-end Lead Scoring System using Machine Learning to predict whether a lead is likely to convert. By assigning scores to incoming leads, the system helps prioritize high-quality prospects and improve conversion rates.
The project includes data preprocessing, exploratory data analysis, model training, a responsive web interface, and deployment on Render.
🏗️ Project Architecture

```
main_project/
├── model_artifacts/
│   ├── cleaned_data.csv
│   ├── lead_scoring_pipeline.joblib
│   └── metadata.json
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── EDA_and_Model_Building.ipynb
├── requirements.txt
├── Procfile
├── render.yaml
└── README.md
```

✨ Features Implemented

* Lead conversion prediction using Machine Learning.
* Interactive and responsive web interface.
* Single lead prediction.
* CSV file upload support for bulk predictions.
* Data preprocessing and feature engineering pipeline.
* Exploratory Data Analysis (EDA) and model comparison notebook (`EDA_and_Model_Building.ipynb`).
* Model persistence using Joblib.
* Flask backend for serving predictions.
* Deployment-ready configuration using Render.
🛠️ Tech Stack
Frontend

* HTML
* CSS
* JavaScript
Backend

* Flask
* Python
Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib
Deployment

* Render
* GitHub
* Gunicorn
📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (see `EDA_and_Model_Building.ipynb`)
4. Feature Engineering
5. Data Preprocessing
6. Model Training & Comparison
7. Model Evaluation
8. Model Serialization
9. Flask Integration
10. Deployment on Render
📓 Exploratory Data Analysis & Model Comparison
The full EDA — missing value analysis, conversion-rate visualizations by Lead Source and Last Activity, feature encoding, and a comparison of Logistic Regression, Decision Tree, and Random Forest models — is documented in:

```
EDA_and_Model_Building.ipynb
```

Random Forest was selected as the final model based on its best balance of Accuracy and ROC-AUC among the models compared.
🚀 How to Run Locally
Make sure Python 3.10 or above is installed.
Open a terminal inside the project folder.
Create a virtual environment

```
python -m venv venv
```

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Start the Flask server

```
python app.py
```

Open in browser

```
http://localhost:5000
```

📂 GitHub Repository
Repository Link:
https://github.com/SameerJeswani/Sameer_Jeswani_JECRC_Foundation_Celebal-DataScience
Project Folder:

```
main_project/
```

🎯 Objective
The objective of this project is to help X Education improve its lead conversion process by identifying high-potential leads and allowing sales teams to focus on prospects who are most likely to become customers.
👨‍💻 Author
Sameer Jeswani
B.Tech – Computer Science and Engineering
Jaipur Engineering College and Research Centre (JECRC), Jaipur
GitHub:
https://github.com/SameerJeswani
📜
