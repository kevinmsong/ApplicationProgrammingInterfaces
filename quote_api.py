import time
import os

API_NINJAS_KEY = os.environ.get("API_NINJAS_KEY", "").strip()
if not API_NINJAS_KEY:
    raise SystemExit(
        "Missing required environment variable API_NINJAS_KEY. "
        "Set it before running this script (see .env.example)."
    )

import requests
import json

category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
try:
    response = requests.get(api_url, headers={'X-Api-Key': API_NINJAS_KEY})
except requests.RequestException:
    raise SystemExit("API Ninjas request failed.") from None
r = response.json()

def get_quote():
    print('\"'+ r[0]["quote"] + '\"', "\n" + r[0]["author"])

def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

while(True):
    clear_screen()
    get_quote()
    time.sleep(600)  # Pause execution for 10 minutes
