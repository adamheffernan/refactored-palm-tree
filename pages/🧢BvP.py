import streamlit as st
import pandas as pd
import inspect
import textwrap
import time

st.set_page_config(page_title="Player Portal", page_icon=":baseball:")
st.markdown(":baseball: Portal")
st.sidebar.markdown(":baseball: Portal")
sheet_id = "1Zrg_dw1uk6Jw6YLXXNUIWDRAnlS4Fj9UK717Er4HJzw"
sheet_name = "BvP"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
st.sidebar.header("Select Filters")
bvp = pd.read_csv(url, on_bad_lines='skip', keep_default_na=False)
st.dataframe(bvp)
