import pandas as pd
import plotly.express as px
import streamlit as st

fig = None
fig2 = None

pref_data = {
    "Prefecture": ["Tokyo", "Osaka", "Kanagawa"],
    "Population": [10000000, 5000000, 4000000],
}

city_data = {
    "Tokyo": {"Shinjuku": 400000, "Shibuya": 300000, "Minato": 200000},
    "Osaka": {"Namba": 150000, "Umeda": 120000},
    "Kanagawa": {"Yokohama": 400000, "Kawasaki": 200000},
}

pref_df = pd.DataFrame(pref_data)
city_dfs = {
    k: pd.DataFrame(list(v.items()), columns=["City", "Population"])
    for k, v in city_data.items()
}

st.title("Population Visualization App")

selected_pref = st.selectbox("Select Prefecture:", ["--", "Tokyo", "Osaka", "Kanagawa"])

num_display = st.selectbox("Number of Bars:", [2, 5, 10])

filter_tokyo = st.sidebar.checkbox("Tokyo", value=True)
filter_osaka = st.sidebar.checkbox("Osaka", value=True)
filter_kanagawa = st.sidebar.checkbox("Kanagawa", value=True)

filters = {
    'Tokyo': filter_tokyo,
    'Osaka': filter_osaka,
    'Kanagawa': filter_kanagawa
}

if selected_pref == "--":  # 都道府県が選択されていない場合
    topN_pref = pref_df.nlargest(num_display, "Population")
    fig = px.bar(
        topN_pref,
        x="Population",
        y="Prefecture",
        orientation="h",
        title="Top N Prefectures by Population",
    )

    filtered_data = pref_df[pref_df['Prefecture'].isin([k for k, v in filters.items() if v])]
    fig2 = px.bar(
        filtered_data,
        x="Population",
        y="Prefecture",
        orientation="h",
        title="Filtered Prefectures by Population",
    )

else:  # 都道府県が選択された場合
    city_df = city_dfs[selected_pref]
    topN_city = city_df.nlargest(num_display, "Population")
    fig = px.bar(
        topN_city,
        x="Population",
        y="City",
        orientation="h",
        title=f"Top N Cities in {selected_pref} by Population",
    )
if fig:
    fig.update_layout(
        xaxis_title="Population",
        yaxis_title="Region",
        xaxis=dict(tickangle=45),  # x軸のメモリを45度回転
    )
    st.plotly_chart(fig)

if fig2:
    fig2.update_layout(
        xaxis_title="Population",
        yaxis_title="Region",
        xaxis=dict(tickangle=45),  # x軸のメモリを45度回転
    )
    st.plotly_chart(fig2)

