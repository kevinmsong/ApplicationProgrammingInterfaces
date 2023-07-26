import time
import os
import requests
import json

category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'qs1rEr/IFadQwWPnWn6Ufg==bguWQvSpD7BiAgLY'})
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