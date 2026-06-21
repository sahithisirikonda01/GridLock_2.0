import streamlit as st
import joblib

from utils.predictor import predict_risk
from utils.recommendations import generate_recommendations

st.set_page_config(
    page_title="Recommendations",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Traffic Management Recommendations")

st.markdown("---")

encoders = joblib.load(
    "models/feature_encoders.pkl"
)

# ==========================
# INPUTS
# ==========================

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

# ==========================
# BUTTON
# ==========================

if st.button(
    "Generate Recommendations",
    use_container_width=True
):

    risk, confidence = predict_risk(
        event_type,
        event_cause,
        corridor,
        police_station,
        zone,
        junction
    )

    st.markdown("---")

    # ==========================
    # RISK RESULT
    # ==========================

    if risk == "High":

        st.error(
            f"🔴 Predicted Risk: {risk}"
        )

    else:

        st.success(
            f"🟢 Predicted Risk: {risk}"
        )

    st.info(
        f"Confidence Score: {confidence:.2f}%"
    )

    # ==========================
    # RESOURCE ESTIMATION
    # ==========================

    st.subheader(
        "📊 Resource Estimation"
    )

    col1, col2 = st.columns(2)

    if risk == "High":

        with col1:
            st.metric(
                "👮 Traffic Personnel",
                "6"
            )

        with col2:
            st.metric(
                "🚧 Barricades",
                "12"
            )

    else:

        with col1:
            st.metric(
                "👮 Traffic Personnel",
                "2"
            )

        with col2:
            st.metric(
                "🚧 Barricades",
                "2"
            )

    st.markdown("---")

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    recommendations = generate_recommendations(
        risk,
        event_cause,
        event_type,
        zone,
        corridor
    )
    st.subheader(
        "💡 Recommended Actions"
    )

    if len(recommendations) == 0:

        st.warning(
            "No recommendations generated."
        )

    else:

        for rec in recommendations:

            st.info(rec)