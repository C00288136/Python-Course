from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Load environment variables from .env file
load_dotenv()

# Ensure the date input and web scraping parts are commented or handled separately
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# URL = f"https://www.billboard.com/charts/hot-100/{date}/"
# response = requests.get(URL)
# web_page = response.text
# soup = BeautifulSoup(web_page, "html.parser")
# song_name_span = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_name_span]

# Spotify API credentials from environment variables
CLIENT_ID = os.environ.get("SPOTIFY_CLIENT")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")
REDIRECT_URI = "http://localhost/"  # Change the port here

# Ensure CLIENT_ID and CLIENT_SECRET are correctly loaded
if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Spotify client ID and secret must be set in the environment variables.")

# Define the scope for creating private playlists
scope = "playlist-modify-private"

print("Client ID:", CLIENT_ID)
print("Client Secret:", CLIENT_SECRET)
print("Redirect URI:", REDIRECT_URI)

# Continue with the rest of your script...


# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt"))

# Get the authenticated user's ID
user_id = sp.current_user()["id"]

print(user_id)
