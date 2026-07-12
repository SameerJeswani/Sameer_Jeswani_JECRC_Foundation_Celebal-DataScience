# 🎯 X Education Lead Scoring System

## 🌐 Live Demo

**Live Application:** https://lead-scoring-project-ejhc.onrender.com

> **Note:** This project is hosted on Render's free tier. If the application has been inactive for some time, it may take around **30–50 seconds** to wake up.

---

# 📌 Project Overview

X Education receives a large number of leads from various online channels. However, only a small percentage of these leads convert into paying customers, resulting in inefficient use of sales resources.

This project implements a complete end-to-end **Lead Scoring System** using Machine Learning to predict whether a lead is likely to convert. By assigning scores to incoming leads, the system helps prioritize high-quality prospects and improve conversion rates.

The project includes:

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation
- Interactive web interface
- Deployment on Render

---

# 🏗️ Project Architecture

```text
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

---

# ✨ Features

✅ Lead conversion prediction using Machine Learning.

✅ Interactive and responsive web interface.

✅ Single lead prediction.

✅ CSV upload support for bulk predictions.

✅ Data preprocessing and feature engineering pipeline.

✅ Exploratory Data Analysis and model comparison notebook.

✅ Model persistence using Joblib.

✅ Flask backend for serving predictions.

✅ Deployment-ready configuration using Render.

---

# 🛠️ Tech Stack

## Frontend

- HTML
- CSS
- JavaScript

## Backend

- Python
- Flask

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

## Deployment

- Render
- GitHub
- Gunicorn

---

# 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Model Training and Comparison
7. Model Evaluation
8. Model Serialization
9. Flask Integration
10. Deployment

---

# 📓 Exploratory Data Analysis & Model Comparison

The complete EDA process is documented in:

```text
EDA_and_Model_Building.ipynb
```

The notebook includes:

- Missing value analysis
- Data visualization
- Conversion-rate analysis
- Feature engineering
- Feature encoding
- Model comparison

The following models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

**Random Forest** was selected as the final model because it achieved the best balance between Accuracy and ROC-AUC score.

---

# 🚀 How to Run Locally

## Clone the Repository

```bash
git clone https://github.com/SameerJeswani/Sameer_Jeswani_JECRC_Foundation_Celebal-DataScience.git
```

## Move to the Project Folder

```bash
cd main_project
```

## Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask Server

```bash
python app.py
```

Open your browser and visit:

```text
http://localhost:5000
```

---

# 📂 GitHub Repository

**Repository Link:**

```text
https://github.com/SameerJeswani/Sameer_Jeswani_JECRC_Foundation_Celebal-DataScience
```

**Project Folder:**

```text
main_project/
```

---

# 🎯 Objective

The objective of this project is to help X Education improve its lead conversion process by identifying high-potential leads and allowing sales teams to focus on prospects who are most likely to become customers.

---

# 👨‍💻 Author

**Sameer Jeswani**

B.Tech – Computer Science and Engineering

Jaipur Engineering College and Research Centre (JECRC), Jaipur

GitHub: https://github.com/SameerJeswani

---

# 📜 License

This project was developed as part of the **Celebal Technologies Data Science Internship Program** for educational and learning purposes.
