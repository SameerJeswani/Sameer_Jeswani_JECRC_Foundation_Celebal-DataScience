# Lead Score Console — X Education

A small Flask web app that serves the Lead Scoring model built for the Celebal
Technologies internship project. Enter a lead's details and get a live
Lead Score (0-100), tier (Hot / Warm / Cold), and recommended sales action.

## What's inside

```
lead_scoring_app/
├── app.py                      # Flask app (routes: /, /predict, /api/predict, /health)
├── train_model.py              # Rebuilds the sklearn pipeline from cleaned_data.csv
├── requirements.txt            # Python dependencies
├── Procfile                    # Tells Render/Heroku how to start the app
├── render.yaml                 # One-click Render Blueprint config
├── templates/index.html        # UI (Jinja2 template)
├── static/style.css            # UI styling
└── model_artifacts/
    ├── cleaned_data.csv            # Cleaned training data (for retraining)
    ├── lead_scoring_pipeline.joblib # Trained sklearn Pipeline (preprocessing + Logistic Regression)
    └── metadata.json               # Dropdown options + model metrics used by the UI
```

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

To retrain the model (e.g. after changing `cleaned_data.csv`):

```bash
python train_model.py
```

This regenerates `model_artifacts/lead_scoring_pipeline.joblib` and `metadata.json`.

## Deploy to Render

**Option A — Blueprint (fastest):**
1. Push this folder to a new GitHub repository.
2. In the Render dashboard, click **New +** → **Blueprint**, and point it at your repo.
   Render will read `render.yaml` and configure everything automatically.
3. Click **Apply** — Render installs `requirements.txt` and starts the app with
   `gunicorn app:app`. Your first deploy takes 2-5 minutes.

**Option B — Manual Web Service:**
1. Push this folder to GitHub.
2. In Render, click **New +** → **Web Service**, connect the repo.
3. Set:
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Click **Create Web Service**.

Render assigns a free `https://<your-app-name>.onrender.com` URL once the build
finishes. No environment variables are required — the app reads the model file
directly from `model_artifacts/`.

> Note: Render's free tier spins the service down after periods of inactivity,
> so the first request after idle time can take ~30-50 seconds to respond
> while it wakes up. This is normal and not a bug in the app.

## API endpoint

Besides the web form, there's a JSON endpoint for programmatic use:

```bash
curl -X POST https://<your-app>.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "TotalVisits": 8,
    "Total Time Spent on Website": 1200,
    "Page Views Per Visit": 4,
    "Do Not Email": "No",
    "Lead Origin": "Lead Add Form",
    "Lead Source": "Welingak Website",
    "Last Activity": "SMS Sent",
    "Specialization": "Finance Management",
    "What is your current occupation": "Working Professional",
    "City": "Mumbai",
    "Last Notable Activity": "SMS Sent"
  }'
```

Response:
```json
{"lead_score": 97, "conversion_probability": 0.9721, "tier": "Hot Lead"}
```
