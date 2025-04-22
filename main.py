import streamlit as st
import plotly.express as px
from backend import get_weather_data

st.title("Weather Forecast Dashboard")
# Data required for rendering the dashboard
location = st.text_input("Location:")
forecast_days = st.slider("Number of Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days for the weather forecast.")
option = st.selectbox("Select the Data to View", ("Temperature", "Sky"))
# Display the selected data options
st.subheader(f"{option} forecast for the next {forecast_days} days in {location}")

# Get either temperature or sky data based on the selected option
dates, temperatures = get_weather_data(location, forecast_days, option_type)

# Create a temperature line chart
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
st.plotly_chart(figure)
