import json
from datetime import datetime
import time
import os

NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "").strip()
if not NEWS_API_KEY:
    raise SystemExit(
        "Missing required environment variable NEWS_API_KEY. "
        "Set it before running this script (see .env.example)."
    )

import requests
from pytz import timezone

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def get_articles(category=None):
    params = {"country": "us", "apiKey": NEWS_API_KEY}
    if category:
        params["category"] = category
    try:
        response = requests.get(NEWS_API_URL, params=params)
    except requests.RequestException:
        raise SystemExit("NewsAPI request failed.") from None

    r = response.json()

    for article in r["articles"]:
        timestamp = article["publishedAt"]

        # Parse the timestamp string to a datetime object
        datetime_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")

        # Convert UTC time to Pacific Time
        pacific = timezone('US/Pacific')
        datetime_object_pacific = datetime_object.replace(tzinfo=timezone('UTC')).astimezone(pacific)

        # Format the datetime object to the desired string format
        formatted_date = datetime_object_pacific.strftime("%m/%d/%y %I:%M %p")
        print(formatted_date, article["title"])

while True:
    clear_screen()
    print("DISCOUNT CABLE NEWS NETWORK")
    print("\nTOP HEADLINES")
    get_articles()

    print("\nHEALTH NEWS")
    get_articles("health")

    print("\nSCIENCE NEWS")
    get_articles("science")

    print("\nTECHNOLOGY NEWS")
    get_articles("technology")
    time.sleep(300)  # Pause execution for 5 minutes