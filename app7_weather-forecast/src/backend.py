import requests
from dotenv import load_dotenv
from os import getenv
from typing import Optional
import streamlit as st

load_dotenv()
api_key = getenv("API_KEY")


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": place, "appid": api_key}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        filtered_data = data["list"]
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]       

    except (ConnectionResetError, ConnectionError):
        st.write("Too many requests! Wait some time before trying again")

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
