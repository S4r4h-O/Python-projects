import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

positivity = []
negativity = []
for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()

    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

dates = [filepath.strip("diary/").strip(".txt") for filepath in filepaths]

st.title("Diary tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity, labels={
    "x": "Dates", "y": "Positivity"
    })
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity, labels={
    "x": "Dates", "y": "Negativity"
    })
st.plotly_chart(neg_figure)


