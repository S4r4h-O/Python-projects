import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select date to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={
                "x": "Date", "y": "Temperature (C)"
                })
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                    "Clear": "images/clear.png", "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"
                    }
            # For each condition (clear, rain, etc), give the respective value from the dict
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            st.image(image_paths, width=115)

    except KeyError:
        st.write("This place probable doesn't exist!")

    except (ConnectionError, ConnectionResetError):
        st.write("Too many requests! Wait some time before trying again.")
