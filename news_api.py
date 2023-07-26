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

def get_articles(this_url):    
    response = requests.get(this_url)

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
    get_articles(("https://newsapi.org/v2/top-headlines?"
                  "country=us&"
                  "apiKey=82471e592e8c4d3d95ec33e3add393be"))
    
    print("\nHEALTH NEWS")
    get_articles(("https://newsapi.org/v2/top-headlines?"
                  "country=us&"
                  "category=health&apiKey=82471e592e8c4d3d95ec33e3add393be"))
    
    print("\nSCIENCE NEWS")
    get_articles(("https://newsapi.org/v2/top-headlines?"
                  "country=us&"
                  "category=science&apiKey=82471e592e8c4d3d95ec33e3add393be"))
    
    print("\nTECHNOLOGY NEWS")
    get_articles(("https://newsapi.org/v2/top-headlines?"
                  "country=us&"
                  "category=technology&apiKey=82471e592e8c4d3d95ec33e3add393be"))
    time.sleep(300)  # Pause execution for 5 minutes