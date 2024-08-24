import streamlit as st
import requests
import random
from PIL import Image
from io import BytesIO

class AICApi:
    def __init__(self):
        self.base_url = "https://api.artic.edu/api/v1"
    
    def get_random_artwork(self, query):
        url = f"{self.base_url}/artworks/search"
        params = {
            "q": query,
            "fields": "id,title,artist_display,image_id,date_display",
            "limit": 100
        }
        headers = {
            "AIC-User-Agent": "Python Script"
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data["data"]:
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
    response = requests.get(image_url)
    
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        st.error("Failed to download the image.")
        return None

def main():
    st.title("Art Institute of Chicago Artwork Explorer")
    
    query = st.text_input("Enter a search query for artwork:", "")
    
    if st.button("Get Random Artwork"):
        if query:
            aic_api = AICApi()
            
            with st.spinner("Fetching artwork..."):
                artwork = aic_api.get_random_artwork(query)
            
            if artwork:
                st.subheader(artwork['title'])
                st.write(f"**Artist:** {artwork['artist']}")
                st.write(f"**Date:** {artwork['date']}")
                
                image = display_image(artwork["image_url"])
                if image:
                    st.image(image, use_column_width=True)
            else:
                st.warning(f"No artworks found for the query: {query}")
        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()