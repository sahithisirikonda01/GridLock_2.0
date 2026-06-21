import joblib
import pandas as pd

from utils.config import (
    MODEL_PATH,
    ENCODER_PATH,
    TARGET_ENCODER_PATH
)

model = joblib.load(
    MODEL_PATH
)

encoders = joblib.load(
    ENCODER_PATH
)

target_encoder = joblib.load(
    TARGET_ENCODER_PATH
)

def predict_risk(
    event_type,
    event_cause,
    corridor,
    police_station,
    zone,
    junction
):

    input_df = pd.DataFrame({
        "event_type": [event_type],
        "event_cause": [event_cause],
        "corridor": [corridor],
        "police_station": [police_station],
        "zone": [zone],
        "junction": [junction]
    })

    FEATURES = [
        "event_type",
        "event_cause",
        "corridor",
        "police_station",
        "zone",
        "junction"
    ]

    for col in FEATURES:

        value = str(input_df[col].iloc[0])

        if value not in encoders[col].classes_:
            return f"Unknown value in {col}: {value}"

        input_df[col] = encoders[col].transform([value])

    # VERY IMPORTANT
    input_df = input_df[FEATURES]

    # prediction = model.predict(input_df)[0]

    # risk = target_encoder.inverse_transform(
    #     [prediction]
    # )[0]

    # return risk
    prediction = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]

    risk = target_encoder.inverse_transform(
        [prediction]
    )[0]

    confidence = round(
        max(probabilities) * 100,
        2
    )

    return risk, confidence