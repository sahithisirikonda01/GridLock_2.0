# import streamlit as st

# st.set_page_config(
#     page_title="GridLock 2.0",
#     page_icon="🚦",
#     layout="wide"
# )

# st.title("🚦 GridLock 2.0")
# st.subheader("Event Driven Congestion Risk Analysis System")

# st.markdown("""
# ### Welcome

# Use the sidebar to navigate:

# - Dashboard
# - Risk Prediction

# Built using:
# - XGBoost
# - Streamlit
# - Historical Event Analysis
# """)


import streamlit as st

st.set_page_config(
    page_title="GridLock 2.0",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 GridLock 2.0")
st.subheader(
    "AI-Powered Traffic Event Risk Assessment & Congestion Management System"
)

st.markdown("---")

st.markdown(
"""
### 🎯 Project Overview

GridLock 2.0 is an intelligent traffic event management platform designed to help
traffic authorities analyze road events, predict congestion risks, retrieve similar
historical incidents, and generate actionable recommendations.

The system leverages Machine Learning (XGBoost) and historical traffic event data
to support data-driven decision making for urban traffic management.

---
"""
)

# ==========================
# FEATURES
# ==========================

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:

    st.success(
        "🚦 Risk Prediction\n\n"
        "Predicts traffic event priority using XGBoost."
    )

    st.success(
        "📈 Historical Trends\n\n"
        "Analyze traffic event patterns across time."
    )

    st.success(
        "🔍 Similar Event Retrieval\n\n"
        "Find historical events most similar to the current event."
    )

with col2:

    st.success(
        "💡 Recommendation Engine\n\n"
        "Generate traffic management actions automatically."
    )

    st.success(
        "📊 Interactive Dashboard\n\n"
        "Visualize event statistics and traffic insights."
    )

    

st.markdown("---")

