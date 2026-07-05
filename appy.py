import streamlit as st
import requests

API_KEY = "1be12e7c98a13a37559d847f86ef2381"

st.title("🌦 Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()
    st.write(data)

    if response.status_code == 200:

        st.success(f"Weather in {city}")

        st.write("🌡 Temperature:", data["main"]["temp"], "°C")
        st.write("💧 Humidity:", data["main"]["humidity"], "%")
        st.write("☁ Condition:", data["weather"][0]["description"])
        st.write("💨 Wind Speed:", data["wind"]["speed"], "m/s")

    else:
        st.error("City not found!")