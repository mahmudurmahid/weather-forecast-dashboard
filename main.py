import streamlit as st
import plotly.express as px

st.title("Weather Forecast Dashboard")
# Data required for rendering the dashboard
location = st.text_input("Location:")
days = st.slider("Number of Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days for the weather forecast.")
option = st.selectbox("Select the Data to View", ("Temperature", "Sky"))
# Display the selected data options
st.subheader(f"{option} forecast for the next {days} days in {location}")

def get_weather_data(days):
    dates = ["2023-20-01", "2023-20-02", "2023-20-03"]
    temperatures = [20, 22, 27]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


dates, temperatures = get_weather_data(days)
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
st.plotly_chart(figure)
