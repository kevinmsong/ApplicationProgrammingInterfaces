import argparse
import requests
import random
from io import BytesIO
from PIL import Image

class AICApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.artic.edu/api/v1"
    
    def get_random_artwork(self, query):
        # Search for artworks based on the query
        url = f"{self.base_url}/artworks/search"
        params = {
            "q": query,
            "fields": "id,title,artist_display,image_id,date_display",
            "limit": 100  # Adjust the limit as needed
        }
        headers = {
            "AIC-User-Agent": "Python Script"
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data["data"]:
                # Select a random artwork from the search results
                artwork = random.choice(data["data"])
                return {
                    "title": artwork.get("title"),
                    "artist": artwork.get("artist_display"),
                    "image_url": f"https://www.artic.edu/iiif/2/{artwork.get('image_id')}/full/843,/0/default.jpg",
                    "date": artwork.get("date_display")
                }
            else:
                return None
        else:
            raise Exception(f"Error: {response.status_code}")

def display_image(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    
    if response.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(response.content))
        
        # Display the image in the command line
        image.show()
    else:
        print("Failed to download the image.")

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Generate a random artwork from the Art Institute of Chicago based on a search query.")
    parser.add_argument("query", help="The search query for the artwork.")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Create an instance of the AICApi
    aic_api = AICApi(api_key="")  # No API key required for public access
    
    # Get a random artwork based on the search query
    artwork = aic_api.get_random_artwork(args.query)
    
    if artwork:
        print(f"Title: {artwork['title']}")
        print(f"Artist: {artwork['artist']}")
        print(f"Date: {artwork['date']}")
        
        # Display the artwork image
        display_image(artwork["image_url"])
    else:
        print(f"No artworks found for the query: {args.query}")

if __name__ == "__main__":
    main()