import pickle
from functools import lru_cache
from pathlib import Path

import numpy as np
from django.conf import settings


MODEL_FILES = {
    "diabetes": "diabetes.pkl",
    "heart": "heart.pkl",
    "parkinsons": "parkinsons.pkl",
}


@lru_cache(maxsize=len(MODEL_FILES))
def load_model(model_name):
    model_path = Path(settings.BASE_DIR) / "models" / MODEL_FILES[model_name]
    with model_path.open("rb") as model_file:
        return pickle.load(model_file)


def predict(model_name, values):
    model = load_model(model_name)
    processed_values = [np.array(values, dtype=float)]
    return int(model.predict(processed_values)[0])
