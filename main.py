import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = f'https://www.billboard.com/charts/hot-100/{date}/'

# Web Scraping for Top 100 songs of the week
response = requests.get(URL)
Hot100 = response.text

soup = BeautifulSoup(Hot100, 'html.parser')

songs = soup.select("li ul li h3")
song_list = [song.getText().strip() for song in songs]
print(song_list)

# Creating a spotify object and authenticating
spotipy = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret= os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt"
    )
)
# Getting Spotify Id
user_id = spotipy.current_user()['id']

# Getting the song URIs
songs_uris = []

for song in song_list:
    result = spotipy.search(q=f'track: {song} year: {date[:4]}')
    try:
        songs_uris.append(result['tracks']['items'][0]['uri'])
    except:
        print(f"{song} doesn't exist in Spotify. Skipped")

print(songs_uris)

# Creating the playlist
playlist = spotipy.user_playlist_create(user=user_id, name=f'{date[:4]} Billboard 100', public=False)

# Adding the songs to the playlist
spotipy.playlist_add_items(playlist_id=playlist['id'], items=songs_uris)