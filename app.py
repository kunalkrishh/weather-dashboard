import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Live Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

API_KEY = "90d28ac6d8c84b9bb03190244260207"

# ---------------- CSS ----------------

st.markdown("""
<style>

/* Background */

.stApp{
background:linear-gradient(135deg,#0F0F0F,#1A1A1A,#8B0000);
background-attachment:fixed;
}

/* Hide Streamlit Header */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */

.title{
text-align:center;
font-size:60px;
font-weight:800;
color:white;
margin-top:10px;
}

.subtitle{
text-align:center;
font-size:20px;
color:#d1d5db;
margin-bottom:30px;
}

/* Input */

.stTextInput input{
background:#202020;
color:white;
border:2px solid #E50914;
border-radius:12px;
font-size:18px;
padding:12px;
}

/* Button */

.stButton>button{
width:100%;
height:55px;
background:#E50914;
color:white;
font-size:18px;
font-weight:bold;
border:none;
border-radius:12px;
transition:0.3s;
}

.stButton>button:hover{
background:#B20710;
transform:scale(1.02);
}

/* Metric Cards */

div[data-testid="stMetric"]{
background:#181818;
padding:20px;
border-radius:18px;
border:1px solid #333;
box-shadow:0px 8px 20px rgba(0,0,0,0.4);
transition:0.3s;
}

div[data-testid="stMetric"]:hover{
transform:translateY(-6px);
border:1px solid #E50914;
box-shadow:0px 0px 25px rgba(229,9,20,.5);
}

div[data-testid="stMetricLabel"]{
color:#bbbbbb;
font-size:18px;
}

div[data-testid="stMetricValue"]{
color:white;
font-size:32px;
font-weight:bold;
}

/* Success */

.stSuccess{
border-radius:10px;
}

/* Footer */

.stCaption{
text-align:center;
color:#cccccc;
font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
"<div class='title'>🌦️ Live Weather Dashboard</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Check real-time weather of any city</div>",
unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT ----------------

city = st.text_input(
"📍 Enter City Name",
placeholder="Delhi"
)

if st.button("🔍 Get Weather"):

    if city.strip()=="":
        st.warning("Please enter a city name.")
        st.stop()

    url=f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"

    response=requests.get(url)

    data=response.json()

    if "error" in data:

        st.error(data["error"]["message"])

    else:

        location=data["location"]

        current=data["current"]

        st.success(
            f"Weather in {location['name']}, {location['country']}"
        )

        left,right=st.columns([1,2])

        with left:

            st.image(
                "https:"+current["condition"]["icon"],
                width=150
            )

            st.markdown(
                f"## {current['condition']['text']}"
            )

        with right:

            st.markdown(
                f"# 🌡️ {current['temp_c']} °C"
            )

            st.write(
                f"### 🥵 Feels Like: {current['feelslike_c']} °C"
            )

            st.write(
                f"📍 {location['name']}, {location['country']}"
            )

            st.write(
                f"🕒 {location['localtime']}"
            )

        st.divider()

        c1,c2,c3,c4=st.columns(4)

        with c1:
            st.metric(
                "💧 Humidity",
                f"{current['humidity']}%"
            )

        with c2:
            st.metric(
                "💨 Wind",
                f"{current['wind_kph']} km/h"
            )

        with c3:
            st.metric(
                "☀️ UV Index",
                current["uv"]
            )

        with c4:
            st.metric(
                "🌍 Pressure",
                f"{current['pressure_mb']} mb"
            )

        c5,c6,c7,c8=st.columns(4)

        with c5:
            st.metric(
                "👀 Visibility",
                f"{current['vis_km']} km"
            )

        with c6:
            st.metric(
                "☁️ Cloud",
                f"{current['cloud']}%"
            )

        with c7:
            st.metric(
                "🧭 Wind Direction",
                current["wind_dir"]
            )

        with c8:
            st.metric(
                "🌬️ Gust",
                f"{current['gust_kph']} km/h"
            )

        st.divider()

        with st.expander("📍 More Details"):

            st.write("**Region:**",location["region"])
            st.write("**Latitude:**",location["lat"])
            st.write("**Longitude:**",location["lon"])
            st.write("**Last Updated:**",current["last_updated"])

st.markdown("---")

st.caption("❤️ Developed by Krish Kunal | Powered by Streamlit & WeatherAPI")