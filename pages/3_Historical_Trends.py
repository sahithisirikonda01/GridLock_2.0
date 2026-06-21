import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Historical Trends",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Historical Trends Dashboard")
st.markdown("---")

# Load Dataset
df = pd.read_csv("data/raw/Astram event data_anonymized.csv")

# ==========================
# Data Cleaning
# ==========================

df["created_date"] = pd.to_datetime(
    df["created_date"],
    errors="coerce"
)

df["month"] = df["created_date"].dt.strftime("%Y-%m")

# ==========================
# KPI SECTION
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Events",
        len(df)
    )

with col2:
    st.metric(
        "Total Zones",
        df["zone"].nunique()
    )

with col3:
    st.metric(
        "Event Causes",
        df["event_cause"].nunique()
    )

with col4:
    st.metric(
        "Police Stations",
        df["police_station"].nunique()
    )

st.markdown("---")

# ==========================
# Events by Month
# ==========================

st.subheader("📅 Events by Month")

month_df = (
    df.groupby("month")
    .size()
    .reset_index(name="Events")
)

fig_month = px.line(
    month_df,
    x="month",
    y="Events",
    markers=True,
    title="Monthly Event Trend"
)

st.plotly_chart(
    fig_month,
    use_container_width=True
)

# ==========================
# Events by Cause
# ==========================

st.subheader("🚧 Events by Cause")

cause_df = (
    df["event_cause"]
    .value_counts()
    .reset_index()
)

cause_df.columns = [
    "Cause",
    "Count"
]

fig_cause = px.bar(
    cause_df,
    x="Cause",
    y="Count",
    title="Event Cause Distribution"
)

st.plotly_chart(
    fig_cause,
    use_container_width=True
)

# ==========================
# Events by Zone
# ==========================

st.subheader("🗺️ Events by Zone")

zone_df = (
    df["zone"]
    .value_counts()
    .reset_index()
)

zone_df.columns = [
    "Zone",
    "Count"
]

fig_zone = px.pie(
    zone_df,
    names="Zone",
    values="Count",
    title="Zone-wise Event Distribution"
)

st.plotly_chart(
    fig_zone,
    use_container_width=True
)

# ==========================
# Planned vs Unplanned
# ==========================

st.subheader("🚦 Planned vs Unplanned")

event_type_df = (
    df["event_type"]
    .value_counts()
    .reset_index()
)

event_type_df.columns = [
    "Event Type",
    "Count"
]

fig_type = px.bar(
    event_type_df,
    x="Event Type",
    y="Count",
    color="Event Type",
    title="Planned vs Unplanned Events"
)

st.plotly_chart(
    fig_type,
    use_container_width=True
)

# ==========================
# Priority Distribution
# ==========================

st.subheader("⚠ Priority Distribution")

priority_df = (
    df["priority"]
    .value_counts()
    .reset_index()
)

priority_df.columns = [
    "Priority",
    "Count"
]

fig_priority = px.pie(
    priority_df,
    names="Priority",
    values="Count",
    title="Priority Distribution"
)

st.plotly_chart(
    fig_priority,
    use_container_width=True
)