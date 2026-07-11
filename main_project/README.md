# 🎯 X Education Lead Scoring System

### Live Demo:
https://lead-scoring-project-ejhc.onrender.com

> **Note:** This project is hosted on Render's free tier. If the application has been inactive for some time, it may take around 30–50 seconds to wake up.

---

## 📌 Project Overview

X Education receives a large number of leads from various online channels. However, only a small percentage of these leads convert into paying customers, causing sales teams to spend significant time on low-potential prospects.

This project implements a complete end-to-end Lead Scoring System using Machine Learning to predict whether a lead is likely to convert. By assigning scores to incoming leads, the system helps prioritize high-quality prospects and improve conversion rates.

The project includes data preprocessing, model training, a responsive web interface, and deployment on Render.

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
├── requirements.txt
├── Procfile
├── render.yaml
└── README.md
```

---

# ✨ Features Implemented

- Lead conversion prediction using Machine Learning.
- Interactive and responsive web interface.
- Single lead prediction.
- CSV file upload support for bulk predictions.
- Data preprocessing and feature engineering pipeline.
- Model persistence using Joblib.
- Flask backend for serving predictions.
- Deployment-ready configuration using Render.

---

# 🛠️ Tech Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Flask
- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

### Deployment

- Render
- GitHub
- Gunicorn

---

# 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Model Serialization
8. Flask Integration
9. Deployment on Render

---

# 🚀 How to Run Locally

Make sure Python 3.10 or above is installed.

Open a terminal inside the project folder.

## Create a virtual environment

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

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start the Flask server

```bash
python app.py
```

---

## Open in browser

```text
http://localhost:5000
```

---

# 📂 GitHub Repository

Repository Link:

https://github.com/SameerJeswani/Sameer_Jeswani_JECRC_Foundation_Celebal-DataScience

Project Folder:

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

GitHub:

https://github.com/SameerJeswani

---

# 📜 License

This project was developed for educational and learning purposes as part of the Celebal Technologies Data Science Foundation Program.
