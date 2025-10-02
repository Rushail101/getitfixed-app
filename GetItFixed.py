import streamlit as st
import pandas as pd
import numpy as np
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json

# Title of the app
st.title("Get it Fixed!")
st.subheader("Your one-stop solution for all repair needs the government won't cater to.")

col1, col2 = st.columns(2)
with col1:
    if st.button("Take a picture"):
        st.camera_input("Take a picture of the infrastructure you want to get fixed.")
with  col2:
    if st.button("Upload a picture"):
        st.file_uploader("Upload a picture of the infrastructure you want to get fixed.")

st.selectbox("Select the issue.", ["Road", "Street Light", "Pothole", "Garbage", "Water Logging", "Electricity Issue", "Other"])
description = st.text_area("Describe the issue in detail")

if st.checkbox("Get my location (Click on it twice if it doesn't work the first time)"):
    loc = get_geolocation()
    st.write(f"Your coordinates are {loc['coords']['latitude'], loc['coords']['longitude']}")
    st.map(pd.DataFrame({'lat': [loc['coords']['latitude']], 'lon': [loc['coords']['longitude']]}))

