import os
import sys

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(0, ROOT_DIR)

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier

from utils.config import (
    PROCESSED_DATA,
    MODEL_PATH
)

# Load processed data
df = pd.read_csv(PROCESSED_DATA)

# ONLY USE IMPORTANT FEATURES

feature_cols = [
    "event_type",
    "event_cause",
    "corridor",
    "police_station",
    "zone",
    "junction"
]

target_col = "priority"

X = df[feature_cols]

y = df[target_col]

print("Features Used:")
print(feature_cols)

print("\nTarget:")
print(target_col)

# Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model

model = XGBClassifier(
    n_estimators=300,
    max_depth=8,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:", accuracy)

print(
    classification_report(
        y_test,
        predictions
    )
)

joblib.dump(
    model,
    MODEL_PATH
)

print("\nXGBoost Model Saved Successfully")