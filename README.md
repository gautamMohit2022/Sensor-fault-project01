#  Sensor Fault Detection in Semiconductor Wafers

### End-to-End Machine Learning Pipeline for Quality Control in Manufacturing

---

##  Project Overview

This project detects **defective semiconductor wafers** based on sensor readings captured during the manufacturing process. It builds an ML-based binary classification pipeline to identify faulty wafers in real-time, aiming to reduce waste and production downtime.

---

##  Objectives

- Predict wafer quality as **Good (1)** or **Bad (-1)**.
- Use **590+ sensor features** collected during fabrication.
- Enable **real-time prediction** using a Flask web interface.
- Structure code for **modular, scalable, and cloud-deployable** use.

---

##  Tech Stack

| Component         | Tools Used                                       |
|------------------|--------------------------------------------------|
| Language          | Python 3.10+                                     |
| ML Models         | XGBoost, Logistic Regression, Random Forest      |
| Web Interface     | Flask, Jinja2, HTML/CSS                          |
| Visualization     | Seaborn                                          |
| Monitoring        | Evidently (Model Drift)                          |
| Database          | MongoDB via `pymongo`                            |
| Cloud (planned)   | AWS EC2, S3 using `boto3`                         |
| CI/CD (planned)   | GitHub Actions                                   |

---

##  ML Workflow

### Training Pipeline:
-  **Data Ingestion** → Reads wafer sensor data.
-  **Data Transformation** → Cleans & preprocesses.
-  **Model Training** → Trains a binary classifier.
-  **Evaluation** → Generates performance metrics.

### Prediction Pipeline:
-  **Flask UI** → Accepts sensor input & predicts wafer status.
-  **Result Logging** → (Future) Stores in MongoDB for monitoring.


---

## 🖥️ Running the Project Locally

```bash
# Step 1: Create virtual environment
conda create -p venv python=3.10 -y
conda activate venv/

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the Flask app
python app.py
Open your browser at: http://localhost:5000

--Dataset Overview
Features: 590 sensor readings per wafer.

Target:

1 → Good wafer

-1 → Faulty wafer

Use case: Fault detection during semiconductor fabrication.

Dependencies (Highlights):
Flask==2.2.3
xgboost==1.6.2
evidently>=0.3.0
pymongo==4.2.0
boto3==1.26.105
imblearn, seaborn, jinja2, Werkzeug
uvicorn, python-dotenv, dill

Install all:
pip install -r requirements.txt

Skills Demonstrated:
Full ML lifecycle: data prep → training → prediction

Modular codebase using src/ structure

Logging, custom exceptions, environment config

Basic frontend integration with Flask + HTML

MLOps readiness: cloud, CI/CD, monitoring

 About Me:
👤 Mohit Gautam
GitHub: @gautamMohit2022


