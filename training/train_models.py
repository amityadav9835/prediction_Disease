import pickle
from pathlib import Path

import pandas as pd
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
MODELS_DIR = BASE_DIR / "models"


def save_model(model, filename):
    MODELS_DIR.mkdir(exist_ok=True)
    with (MODELS_DIR / filename).open("wb") as model_file:
        pickle.dump(model, model_file)


def train_diabetes():
    data = pd.read_csv(DATASETS_DIR / "diabetes.csv")
    x = data.iloc[:, 0:8].to_numpy()
    y = data["Outcome"].to_numpy()

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        stratify=y,
        random_state=1,
    )

    model = svm.SVC(kernel="linear")
    model.fit(x_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(x_test))
    save_model(model, "diabetes.pkl")
    return accuracy


def train_heart():
    data = pd.read_csv(DATASETS_DIR / "heart.csv")
    x = data.iloc[:, 0:13].to_numpy()
    y = data["target"].to_numpy()

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        stratify=y,
        random_state=1,
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(x_test))
    save_model(model, "heart.pkl")
    return accuracy


def train_parkinsons():
    data = pd.read_csv(DATASETS_DIR / "ParkinsonsDisease.csv")
    data = data.drop(columns=["name"])
    x = data.drop(columns=["status"]).to_numpy()
    y = data["status"].to_numpy()

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        stratify=y,
        random_state=2,
    )

    model = svm.SVC(kernel="linear")
    model.fit(x_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(x_test))
    save_model(model, "parkinsons.pkl")
    return accuracy


if __name__ == "__main__":
    scores = {
        "Diabetes": train_diabetes(),
        "Heart Disease": train_heart(),
        "Parkinsons": train_parkinsons(),
    }

    for model_name, score in scores.items():
        print(f"{model_name} model accuracy: {score:.2%}")

    print(f"Models saved in: {MODELS_DIR}")
