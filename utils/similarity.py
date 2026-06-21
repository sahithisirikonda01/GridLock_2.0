import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors

# Load processed data
df = pd.read_csv(
    "data/processed/processed_events.csv"
)

FEATURES = [
    "event_type",
    "event_cause",
    "corridor",
    "police_station",
    "zone",
    "junction"
]

# Train KNN on historical events
knn = NearestNeighbors(
    n_neighbors=5,
    metric="euclidean"
)

knn.fit(df[FEATURES])

encoders = joblib.load(
    "models/feature_encoders.pkl"
)

target_encoder = joblib.load(
    "models/target_encoder.pkl"
)


def find_similar_events(
    event_type,
    event_cause,
    corridor,
    police_station,
    zone,
    junction
):

    input_df = pd.DataFrame([{
        "event_type": event_type,
        "event_cause": event_cause,
        "corridor": corridor,
        "police_station": police_station,
        "zone": zone,
        "junction": junction
    }])

    # Encode user input
    for col in FEATURES:

        input_df[col] = encoders[col].transform(
            input_df[col]
        )

    distances, indices = knn.kneighbors(
        input_df
    )

    similar_df = df.iloc[
        indices[0]
    ].copy()

        # Decode features
    for col in FEATURES:
        similar_df[col] = encoders[col].inverse_transform(
            similar_df[col].astype(int)
        )

    # Decode target
    similar_df["priority"] = target_encoder.inverse_transform(
        similar_df["priority"].astype(int)
    )

    return similar_df[
        [
            "event_type",
            "event_cause",
            "corridor",
            "police_station",
            "zone",
            "junction",
            "priority"
        ]
    ]