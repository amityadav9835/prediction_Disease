# AI Doctor - Multiple Disease Predictor

AI Doctor is a Django web application that predicts possible disease risk using trained machine learning models. The app includes user authentication, a professional responsive UI, CSV-based model training, and prediction pages for three diseases.

## Features

- User signup, login, and logout
- Protected prediction pages for authenticated users
- Diabetes prediction
- Heart disease prediction
- Parkinsons disease prediction
- Responsive dashboard UI
- CSS animations
- CSV datasets included
- Model training script included

## Tech Stack

- Python
- Django
- SQLite
- NumPy
- Pandas
- Scikit-learn
- HTML
- CSS

## Project Structure

```text
ai_doctor/
  settings.py
  urls.py

predictor/
  views.py
  urls.py
  forms.py
  ml.py
  models.py

templates/
  predictor/
    base.html
    home.html
    prediction_form.html
  registration/
    login.html
    signup.html

static/
  css/
    style.css
  images/
    backgroundimage.jpg

datasets/
  diabetes.csv
  heart.csv
  ParkinsonsDisease.csv

models/
  diabetes.pkl
  heart.pkl
  parkinsons.pkl

training/
  train_models.py
  README.md

manage.py
requirements.txt
db.sqlite3
```
## Live Demo
To see a live demo of the project, [click here](https://prediction-disease-opa6.onrender.com/)

## Installation

Open terminal in the project folder:

```powershell
cd D:\ai_doctor
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run database migrations:

```powershell
python manage.py migrate
```

## Run The Project

Start the Django development server:

```powershell
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

## Main URLs

```text
/                         Home page
/signup/                  Create account
/accounts/login/          Login
/logout/                  Logout
/diabetes/                Diabetes prediction
/heartdisease/            Heart disease prediction
/parkinsons/              Parkinsons prediction
/admin/                   Django admin
```

Prediction pages require login.

## Create Admin User

To access Django admin:

```powershell
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## Model Training

The CSV datasets are stored in:

```text
datasets/
```

To train all models:

```powershell
python training\train_models.py
```

This trains the models and saves them into:

```text
models/
```

Output files:

```text
models/diabetes.pkl
models/heart.pkl
models/parkinsons.pkl
```

## Datasets

Diabetes:
- CSV file: `datasets/diabetes.csv`
- Target column: `Outcome`
- Algorithm: Support Vector Machine

Heart Disease:
- CSV file: `datasets/heart.csv`
- Target column: `target`
- Algorithm: Logistic Regression

Parkinsons:
- CSV file: `datasets/ParkinsonsDisease.csv`
- Target column: `status`
- Removed column before training: `name`
- Algorithm: Support Vector Machine

## How Prediction Works

1. User logs in.
2. User opens a prediction page.
3. User enters medical input values.
4. Django validates the form.
5. `predictor/ml.py` loads the correct `.pkl` model.
6. The model predicts the result.
7. The result is shown on the page.

## Important Files

`predictor/views.py`

Controls homepage, signup, logout, and disease prediction pages.

`predictor/ml.py`

Loads trained model files and runs predictions.

`predictor/forms.py`

Contains signup form and dynamically creates prediction forms.

`training/train_models.py`

Reads CSV datasets, trains ML models, prints accuracy, and saves `.pkl` files.

`static/css/style.css`

Contains all website styling, responsive design, and animations.

## Note

This project is for learning and demonstration purposes only. Predictions should not be treated as medical advice.
