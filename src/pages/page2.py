# page2.py
import pandas as pd
import plotly.express as px
import streamlit as st

age_data = {
    "Tokyo": {
        "10s": 1000000,
        "20s": 900000,
        "30s": 800000,
        "40s": 700000,
        "50s": 600000,
        "60s": 500000,
    },
    "Osaka": {
        "10s": 400000,
        "20s": 350000,
        "30s": 300000,
        "40s": 250000,
        "50s": 200000,
        "60s": 150000,
    },
    "Kanagawa": {
        "10s": 100000,
        "20s": 90000,
        "30s": 80000,
        "40s": 70000,
        "50s": 60000,
        "60s": 50000,
    },
}

selected_pref = st.selectbox("Select Prefecture:", ["Tokyo", "Osaka", "Kanagawa"])

age_df = pd.DataFrame(
    list(age_data[selected_pref].items()), columns=["Age Group", "Population"]
)

fig = px.pie(
    age_df,
    names="Age Group",
    values="Population",
    title=f"Population by Age Group in {selected_pref}",
)

st.plotly_chart(fig)
