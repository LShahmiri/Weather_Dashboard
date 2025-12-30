import streamlit as st
import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤")

st.title("🌤 Weather Dashboard")

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    if city:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            st.subheader(data["name"])
            st.write(f"🌡 Temperature: {data['main']['temp']} °C")
            st.write(f"💧 Humidity: {data['main']['humidity']} %")
            st.write(f"🌬 Wind Speed: {data['wind']['speed']} m/s")
            st.write(f"☁ Description: {data['weather'][0]['description']}")
        else:
            st.error("City not found")
