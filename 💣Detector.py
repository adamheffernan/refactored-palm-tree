import pandas as pd
import plotly.express as px
import streamlit as st
### SET UP THE SHEET, IMPORT FROM GOOGLE, ETC"""
st.set_page_config(page_title="Detector", page_icon=":bomb:")
st.markdown(":bomb: Detector")
st.sidebar.markdown(":bomb: Detector")
sheet_id = "1Zrg_dw1uk6Jw6YLXXNUIWDRAnlS4Fj9UK717Er4HJzw"
sheet_name = "BombDetector"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
st.sidebar.header("Select Filters")
bomb_data = pd.read_csv(url, on_bad_lines='skip', keep_default_na=False)

### FILTERING OF DATA BEGINS"""
allTeams = st.sidebar.checkbox("Select All Teams", value=True)
if allTeams:
    team = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["TEAM"].unique(),
        default=bomb_data["TEAM"].unique()
    )
else:
    team = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["TEAM"].unique()
    )

allSalaries = st.sidebar.checkbox("Select All Salaries", value=True)
if allSalaries:
    salary = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["PRICE"].unique(),
        default=bomb_data["PRICE"].unique()
    )
else:
    salary = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["PRICE"].unique()
    )

allPos = st.sidebar.checkbox("Select All Positions", value=True)
if allPos:
    pos = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["POS"].unique(),
        default=bomb_data["POS"].unique()
    )
else:
    pos = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["POS"].unique()
    )

allOrder = st.sidebar.checkbox("Select All Batting Order", value=True)
if allOrder:
    order = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["ORDER"].unique(),
        default=bomb_data["ORDER"].unique()
    )
else:
    order = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["ORDER"].unique()
    )

allBomb = st.sidebar.checkbox("Select All Bomb Ratings", value=True)
if allBomb:
    rating = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["RATING"].unique(),
        default=bomb_data["RATING"].unique()
    )
else:
    rating = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["RATING"].unique()
    )

allPitch = st.sidebar.checkbox("Select All Pitch Amounts", value=True)
if allPitch:
    pitch_sample = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["PITCHERSAMPLE"].unique(),
        default=bomb_data["PITCHERSAMPLE"].unique()
    )
else:
    pitch_sample = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["PITCHERSAMPLE"].unique()
    )

allHit = st.sidebar.checkbox("Select All Hitter Sample Sizes", value=True)
if allHit:
    hitter_sample = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["HITTERSAMPLE"].unique(),
        default=bomb_data["HITTERSAMPLE"].unique()
    )
else:
    hitter_sample = st.sidebar.multiselect(
        "Select one or more options:",
        options=bomb_data["HITTERSAMPLE"].unique()
    )
### FILTERING OF DATA DONE"""
bomb_data_selection = bomb_data.query(
    "TEAM==@team & POS==@pos & ORDER==@order & PRICE==@salary & HITTERSAMPLE==@hitter_sample & "
    "PITCHERSAMPLE==@pitch_sample & RATING==@rating "
)

st.dataframe(bomb_data_selection)
