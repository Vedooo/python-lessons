import requests as rq
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = 'd31f3267cfcc431792407a1cdb467c0a'
SPOTIFY_CLIENT_SECRET = '214208bf2730483bad229ede4c1aa1e8'

date = input('Which date do you want travel to? Type date in this format YYYY-MM-DD: ')
url = f'https://www.billboard.com/charts/hot-100/{date}/'
spotify_endpoint = 'https://api.spotify.com/v1'

response = rq.get(url)
web_html = response.text
soup = BeautifulSoup(web_html,'html.parser')
song_names_spans = soup.select('ul li ul li h3')

# songs = soup.select("div.o-chart-results-list-row-container ul li ul li h3#title-of-a-story")

song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Vedoo', 
    )
)
user_id = sp.current_user()["id"]
playlist_endpoint = f'{spotify_endpoint}/users/{user_id}/playlists'
params = {
    "name": "Billboard Top 100",
    "public": False,
    "description": "A playlist which created by spotify api",
}

header = {
    "Authorization: Bearer",
    'Content-Type: application/json'
}

create_playlist = rq.post(playlist_endpoint, params=params)
