from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

@app.route("/home")
def home():
    return render_template("home.html")


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


if __name__ == "__main__":
   app.run(debug=True)
