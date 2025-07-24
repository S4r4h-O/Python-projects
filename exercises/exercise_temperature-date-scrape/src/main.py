import time
import sqlite3
import requests
from bs4 import BeautifulSoup

connection = sqlite3.connect("temperatures.db")
cursor = connection.cursor()

URL = "http://programmer100.pythonanywhere.com/"


def read():
    date = cursor.execute("SELECT date FROM temperatures")
    date = date.fetchall()
    temperature = cursor.execute("SELECT temperature FROM temperatures")
    temperature = temperature.fetchall()
    return date, temperature


def write(temperature):
    now = time.strftime("%d-%m-%y-%H-%M-%S")
    cursor.execute("INSERT INTO temperatures VALUES(?,?)", 
                   (now, temperature))
    connection.commit()


def scrape(url):
    r = requests.get(URL)
    r = r.text
    return r


def extract(source):
    soup = BeautifulSoup(source, 'html.parser')
    temperature = soup.find(id="temperatureId")
    temperature = temperature.b.string
    return temperature


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    write(extracted)
