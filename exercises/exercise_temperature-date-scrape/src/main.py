import time
import requests
import pandas as pd
import streamlit as st
import plotly.express as px
from bs4 import BeautifulSoup


def write(content):
    with open("data.txt", "a") as file:
        file.write(content)


now = time.strftime("%d-%m-%y-%H-%M-%S")

URL = "http://programmer100.pythonanywhere.com/"

r = requests.get(URL)
r = r.text

soup = BeautifulSoup(r, 'html.parser')
temperature = soup.find(id="temperatureId")
temperature = temperature.b
write(f"{now},{temperature.string}" + "\n")

df = pd.read_csv("data.txt", parse_dates=True)

figure = px.line(x=df["date"], y=df["temperature"],
                 labels={
                     "x": "Date", "y": "Temperature"
                     })

st.plotly_chart(figure)
