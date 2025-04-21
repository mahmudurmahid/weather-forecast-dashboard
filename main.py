import streamlit as st

st.title("Weather Forecast Dashboard")
location = st.text_input("Location:")
days = st.slider("Number of Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days for the weather forecast.")
option = st.selectbox("Select the Data to View", ("Temperature", "Sky"))
st.subheader(f"{option} forecast for the next {days} days in {location}")
