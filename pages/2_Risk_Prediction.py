import streamlit as st
import joblib

from utils.predictor import predict_risk

st.set_page_config(
    page_title="Risk Prediction",
    layout="wide"
)

st.title("🚦 Risk Prediction")

encoders = joblib.load(
    "models/feature_encoders.pkl"
)

col1, col2 = st.columns(2)

with col1:

    event_type = st.selectbox(
        "Event Type",
        encoders["event_type"].classes_
    )

    event_cause = st.selectbox(
        "Event Cause",
        encoders["event_cause"].classes_
    )

    corridor = st.selectbox(
        "Corridor",
        encoders["corridor"].classes_
    )

with col2:

    police_station = st.selectbox(
        "Police Station",
        encoders["police_station"].classes_
    )

    zone = st.selectbox(
        "Zone",
        encoders["zone"].classes_
    )

    junction = st.selectbox(
        "Junction",
        encoders["junction"].classes_
    )

if st.button(
    "Predict Risk",
    use_container_width=True
):

    result, confidence = predict_risk(
        event_type,
        event_cause,
        corridor,
        police_station,
        zone,
        junction
    )

    st.divider()

    if str(result).lower() == "high":

        st.error(
            f"🔴 HIGH RISK"
        )

    elif str(result).lower() == "medium":

        st.warning(
            f"🟠 MEDIUM RISK"
        )

    else:

        st.success(
            f"🟢 LOW RISK"
        )

    st.metric(
        "Predicted Priority",
        result
    )