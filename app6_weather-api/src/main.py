from flask import Flask, render_template
from numpy._core import records
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/home")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station: str, date: str):
    filename = f"data_small/TG_STAID0000{station}.txt"
    df = pd.read_csv(filename, skiprows=20,
                     parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
            "station": station,
            "date": date,
            "temperature": temperature
            }


@app.route("/api/v1/<station>/")
def all_data(station):
    filename = f"data_small/TG_STAID0000{station}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>/")
def yearly(station: str, year: str):
    filename = f"data_small/TG_STAID0000{station}.txt"
    df = pd.read_csv(filename, skiprows=20)
    # Convert from int to str
    df["    DATE"] = df["    DATE"].astype(str)
    # Filter the dates that starts with the string of the var year
    result = df[df["    DATE"].str.startswith(year)].to_dict(orient="records")
    return result


if __name__ == "__main__":
   app.run(debug=True)
