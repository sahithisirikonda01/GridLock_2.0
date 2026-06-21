import streamlit as st
import joblib

from utils.similarity import find_similar_events

st.set_page_config(
    page_title="Similar Events",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Similar Historical Events")
st.markdown(
    """
    Retrieve the most similar historical traffic events
    and understand their risk levels.
    """
)

st.markdown("---")

# Load encoders
encoders = joblib.load(
    "models/feature_encoders.pkl"
)

# ======================
# INPUT SECTION
# ======================

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

st.markdown("---")

# ======================
# FIND SIMILAR EVENTS
# ======================

if st.button(
    "🔍 Find Similar Events",
    use_container_width=True
):

    results = find_similar_events(
        event_type,
        event_cause,
        corridor,
        police_station,
        zone,
        junction
    )

    st.success(
        "Top 5 Similar Historical Events Retrieved"
    )

    st.markdown("---")

    # ======================
    # RISK SUMMARY
    # ======================

    high_count = (
        results["priority"] == "High"
    ).sum()

    low_count = (
        results["priority"] == "Low"
    ).sum()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "High Risk Events",
            high_count
        )

    with col2:
        st.metric(
            "Low Risk Events",
            low_count
        )

    st.markdown("---")

    if high_count >= 3:

        st.error(
            f"⚠ {high_count}/5 similar events were HIGH PRIORITY.\n\n"
            f"Historical data suggests elevated congestion risk."
        )

    else:

        st.success(
            f"✅ Only {high_count}/5 similar events were HIGH PRIORITY.\n\n"
            f"Historical data suggests manageable traffic impact."
        )

    st.markdown("---")

    # ======================
    # DISPLAY EVENTS
    # ======================

    st.subheader(
        "📋 Similar Historical Events"
    )

    for idx, row in results.iterrows():

        with st.expander(
            f"Event #{idx}"
        ):

            c1, c2 = st.columns(2)

            with c1:

                st.write(
                    f"**Event Type:** {row['event_type']}"
                )

                st.write(
                    f"**Event Cause:** {row['event_cause']}"
                )

                st.write(
                    f"**Zone:** {row['zone']}"
                )

            with c2:

                st.write(
                    f"**Police Station:** {row['police_station']}"
                )

                st.write(
                    f"**Corridor:** {row['corridor']}"
                )

                st.write(
                    f"**Junction:** {row['junction']}"
                )

            st.markdown("---")

            if row["priority"] == "High":

                st.error(
                    "🔴 HIGH PRIORITY"
                )

            elif row["priority"] == "Low":

                st.success(
                    "🟢 LOW PRIORITY"
                )

            else:

                st.warning(
                    f"⚠ {row['priority']}"
                )