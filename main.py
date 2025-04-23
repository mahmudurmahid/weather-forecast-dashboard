import streamlit as st
import plotly.express as px
from backend import get_weather_data

st.title("Weather Forecast Dashboard")
# Data required for rendering the dashboard
location = st.text_input("Location:")
forecast_days = st.slider("Number of Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days for the weather forecast.")
option_type = st.selectbox("Select the Data to View", ("Temperature", "Sky"))
# Display the selected data options
st.subheader(f"{option_type} forecast for the next {forecast_days} days in {location}")

if location:
    try:
        filtered_data = get_weather_data(location, forecast_days)
        # Get either temperature or sky data based on the selected option
        if option_type == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data] # / 10 converts from K to C
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature line chart
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)

        if option_type == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            # Create a sky conditions visual
            st.image(image_paths, width=100, caption=sky_conditions)
    except KeyError:
        st.error("Invalid location. Please try again.")
