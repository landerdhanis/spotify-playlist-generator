import requests
from bs4 import BeautifulSoup
import spotipy

SPOTIFY_CLIENT_ID = "ed1ddde9fe75459c8cb36a43d9e4be26"
CLIENT_SECRET = "689a94cd08064c379e996b51b35046cc"

URL = "https://www.billboard.com/charts/hot-100/2012-06-15"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

auth = spotipy.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=CLIENT_SECRET, scope="playlist-modify-private",
                            redirect_uri="https://example.com/", username="1158668296")


sp = spotipy.Spotify(auth_manager=auth)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")