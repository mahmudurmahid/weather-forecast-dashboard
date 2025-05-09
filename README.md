# 🌦️ Weather Forecast Dashboard

The **Weather Forecast Dashboard** is an interactive Streamlit application that retrieves and displays weather forecast data for any location over the next 1–5 days. Users can choose to view either temperature trends as a line chart or visualize sky conditions (like clear, cloudy, rainy, or snowy) with corresponding icons.

This tool is helpful for travelers, planners, or anyone needing quick and accessible weather insights without navigating complex APIs or websites.

[Live Streamlit App](https://mahmudurmahid-weather-forecast-dashboard-main-dqcrno.streamlit.app/)

---

## 📑 CONTENTS

- [User Experience](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Page Layout](#page-layout)
  - [Color Scheme & Visuals](#color-scheme--visuals)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Planned Improvements](#planned-improvements)
- [Technologies Used](#technologies-used)
  - [Languages](#languages-used)
  - [Libraries](#libraries-used)
- [Project Files](#project-files)
- [Installation & Usage](#installation--usage)
  - [How to Run](#how-to-run)
  - [Setting Up API Keys](#setting-up-api-keys)
- [Testing](#testing)
- [Credits](#credits)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

---

## 🧠 User Experience (UX)

### User Stories

As a user, I want to:

- Enter a city or town name and view the weather forecast for up to 5 days.
- Choose between viewing temperature trends or sky conditions.
- See clear, visual representations like line charts and icons for better understanding.
- Be notified of errors, such as invalid locations or missing data.
- Use the app quickly without needing to register or configure settings.

---

## 🎨 Design

### Page Layout

- **Title:** Clearly states the app’s purpose.
- **Input Controls:**
  - Text input for location.
  - Slider for selecting number of forecast days.
  - Select box for choosing data type (Temperature or Sky).
- **Output Display:**
  - Line chart for temperature forecasts.
  - Icon gallery for sky condition forecasts.

### Color Scheme & Visuals

- **Chart Style:** Clean Plotly Express charts with date on the x-axis and temperature (°C) on the y-axis.
- **Sky Conditions:** Uses visually appealing PNG icons for conditions like clear, clouds, rain, and snow.
- **Layout:** Streamlit defaults with responsive and minimalist design.

---

## 🛠 Features

### Implemented Features

- ✅ Fetches 3-hour interval forecast data from OpenWeather API.
- ✅ Displays temperature forecasts as line graphs.
- ✅ Shows sky conditions using weather icons.
- ✅ Allows selection of forecast duration (1–5 days).
- ✅ Implements error handling for invalid locations.
- ✅ Modular code with separation between frontend (`main.py`) and backend (`backend.py`).

### Planned Improvements

- 🔄 Add loading spinners during data fetch.
- 🔄 Improve error feedback for network issues.
- 🔄 Include more forecast metrics like humidity, wind, or pressure.
- 🔄 Allow language or unit preference customization.
- 🔄 Add map-based location search or autocomplete.

---

## 💻 Technologies Used

### Languages Used

- Python 3.13

### Libraries Used

| Library     | Purpose                            |
| ----------- | ---------------------------------- |
| `streamlit` | UI framework for dashboard         |
| `plotly`    | Interactive chart rendering        |
| `requests`  | HTTP requests to OpenWeather API   |
| `dotenv`    | Environment variable management    |
| `pandas`    | Data handling (used indirectly)    |
| `pillow`    | Image display support in Streamlit |

---

## 📁 Project Files

```bash
.
├── main.py # Streamlit frontend logic
├── backend.py # API call and data parsing logic
├── images/ # Folder with icons: clear.png, cloud.png, rain.png, snow.png
├── .env # Contains the OpenWeather API key
├── requirements.txt # All required dependencies
```

---

## 🚀 Installation & Usage

### Prerequisites

Ensure Python 3 is installed on your system. Then install the required packages:

```bash
pip install -r requirements.txt
```

### Setting Up API Keys

Sign up at OpenWeatherMap and get your API key.

Create a .env file in the root directory and add your key like so:

```bash
openweather_api_key=your_api_key_here
```

### How to Run

To start the dashboard, run the following command:

```bash

streamlit run main.py
```

Then, open the provided local URL in your browser to use the app.

## ✅ Testing

Manual testing was carried out to verify:

- Accurate chart display for various cities and forecast durations. ✔
- Error messages shown for invalid cities. ✔
- Images render correctly for known sky conditions. ✔
- App remains stable under multiple use cases. ✔
- Forecasts reflect correct date ranges based on current time. ✔

## 🧾 Credits

### Code

- Written in Python using Streamlit and Plotly.
- Designed for clarity, modularity, and easy customization.

## Acknowledgements

- Weather data powered by OpenWeatherMap API.
- Icon images sourced from public domain or custom-designed for display.
- Thanks to Streamlit and Plotly teams for enabling rapid dashboard development.
