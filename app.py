import pandas as pd
import streamlit as st

st.title(" Road Damage Monitoring System")

df = pd.read_csv("data/potholes.csv")

st.write("Detected Potholes Data:")
st.dataframe(df)

st.map(df.rename(columns={"Latitude": "lat", "Longitude": "lon"}))