# Model Training

This folder shows how the machine learning models are trained from CSV data and saved as pickle files for Django.

## CSV Files

The datasets are stored in:

```text
datasets/
  diabetes.csv
  heart.csv
  ParkinsonsDisease.csv
```

## Output Model Files

When training is complete, the script saves:

```text
models/
  diabetes.pkl
  heart.pkl
  parkinsons.pkl
```

These files are loaded by `predictor/ml.py` when the user submits a prediction form.

## Run Training

From the project root:

```powershell
python training/train_models.py
```

## Training Flow

1. Read CSV file using pandas.
2. Separate input features `X` and target output `y`.
3. Split data into training and testing data.
4. Train a machine learning classifier.
5. Check test accuracy.
6. Save the model as a `.pkl` file.

## Models

Diabetes:
- CSV: `datasets/diabetes.csv`
- Features: first 8 columns
- Target: `Outcome`
- Algorithm: Support Vector Machine
- Output: `models/diabetes.pkl`

Heart Disease:
- CSV: `datasets/heart.csv`
- Features: first 13 columns
- Target: `target`
- Algorithm: Logistic Regression
- Output: `models/heart.pkl`

Parkinsons:
- CSV: `datasets/ParkinsonsDisease.csv`
- Removed column: `name`
- Features: all columns except `status`
- Target: `status`
- Algorithm: Support Vector Machine
- Output: `models/parkinsons.pkl`
