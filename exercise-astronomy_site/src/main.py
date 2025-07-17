import requests
import streamlit as st
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
api_key = os.getenv("API_KEY")

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
r = requests.get(url)
page_content = r.json()

st.set_page_config(layout="centered")

st.header(page_content['title'])
st.subheader(page_content['date'])

img_url = page_content['url']
img_raw = requests.get(img_url, stream=True)

img_file = Path(f"images/{page_content['date']}.jpg")
if not img_file.exists():
    with open(img_file, "wb") as img:
        img.write(img_raw.content)

st.image(f"images/{page_content['date']}.jpg")

st.text(page_content['explanation'])
