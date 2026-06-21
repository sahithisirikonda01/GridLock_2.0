import streamlit as st
import plotly.express as px

from utils.analytics import (
    load_data,
    total_events,
    planned_events,
    unplanned_events,
    high_priority_events
)

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("📊 Dashboard")

df = load_data()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Events",
    total_events(df)
)

col2.metric(
    "Planned Events",
    planned_events(df)
)

col3.metric(
    "Unplanned Events",
    unplanned_events(df)
)

col4.metric(
    "High Priority",
    high_priority_events(df)
)

st.divider()

left, right = st.columns(2)

with left:

    zone_counts = (
        df["zone"]
        .value_counts()
        .reset_index()
    )

    zone_counts.columns = [
        "Zone",
        "Count"
    ]

    fig = px.bar(
        zone_counts,
        x="Zone",
        y="Count",
        title="Events by Zone"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    cause_counts = (
        df["event_cause"]
        .value_counts()
        .reset_index()
    )

    cause_counts.columns = [
        "Cause",
        "Count"
    ]

    fig = px.pie(
        cause_counts,
        names="Cause",
        values="Count",
        title="Event Causes"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

corridor_counts = (
    df["corridor"]
    .value_counts()
    .head(10)
    .reset_index()
)

corridor_counts.columns = [
    "Corridor",
    "Count"
]

fig = px.bar(
    corridor_counts,
    x="Corridor",
    y="Count",
    title="Top Corridors"
)

st.plotly_chart(
    fig,
    use_container_width=True
)