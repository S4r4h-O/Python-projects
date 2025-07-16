import requests
from dotenv import load_dotenv
import os
import polars as pl
from pathlib import Path
import send_email

load_dotenv()
api_key = os.getenv("API_KEY")

topic = "tesla"

url = ( 
    f"https://newsapi.org/v2/everything"
    f"?q={topic}&from=2025-06-16&sortBy"
    f"=publishedAt&apiKey={api_key}&language=en"
)
r = requests.get(url)
content = r.json()

body = ""
for article in content["articles"][:20]:
    try:
        body = body + article["title"] + "\n" \
        + article["description"] + "\n" + article["url"] + 2*"\n"

    except TypeError:
        pass

send_email.send_email(message="Subject: Todays news\n" + body)
