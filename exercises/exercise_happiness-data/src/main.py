import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In search for hapiness")
x_axis = st.selectbox("Select the data for the x axis", ("GDP", "Generosity", "Happiness"))
y_axis = st.selectbox("Select the data for the y axis", ("GDP", "Generosity", "Happiness"))
st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("happy.csv")
gdp = df["gdp"]
generosity = df["generosity"]
happiness = df["happiness"]

match x_axis:
    case "GDP":
        x = gdp

    case "Generosity":
        x = generosity

    case "Happiness":
        x = happiness

match y_axis:
    case "GDP":
        y = gdp

    case "Generosity":
        y = generosity

    case "Happiness":
        y = happiness

figure = px.scatter(x=x, y=y, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
