import streamlit as st
import plotly.express as px
from main import write, scrape, extract, read
 
URL = "http://programmer100.pythonanywhere.com/"

scraped = scrape(URL)
extracted = extract(scraped)
write(temperature=extracted)

date, temperature = read()
date = [item[0] for item in date]
temperature = [item[0] for item in temperature]

figure = px.line(x=date, y=temperature,
                 labels={"x": "Date", "y": "Temperature"})

st.plotly_chart(figure)
