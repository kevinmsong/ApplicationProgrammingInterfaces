import requests
import json
from datetime import datetime
from pytz import timezone
import time
import os

def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def get_articles():
    # os.system('cls' if os.name == 'nt' else 'clear')

    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=82471e592e8c4d3d95ec33e3add393be')
    response = requests.get(url)

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
    get_articles()
    time.sleep(60)  # Pause execution for 60 seconds