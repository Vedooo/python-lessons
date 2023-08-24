import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from urllib.parse import urlencode
import base64
import webbrowser

ACCESS_TOKEN= ''
CID = ''
SECRET = ''

auth_headers = {
    "client_id": CID,
    "response_type": "code",
    "redirect_uri": "http://127.0.0.1:5000/callback",
    "scope": "user-library-read"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

code = 'AQBbVq7C7eYL794mEveXKk0v8RQtfOsT_SvdKH9I2obBUhKHHTUxQd7ADE0Kq2PS06qWZaPSTluoV9IW3QI_ZLJiwxvYMUWp0tIcrz0k5B7gIToeqKHFm4Bo9j4ZFJ9YMcyaDdkHsomObuJrtPq7hZz79p27gOOdRYUMuPmYGCIKixKV-MqQNbx-0Hw2cPpX5HyAAkY'

encoded_credentials = base64.b64encode(CID.encode() + b':' + SECRET.encode()).decode("utf-8")
token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}
token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://127.0.0.1:5000/callback"
}
r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
token = r.json()["access_token"]
print(token)

user_headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

user_params = {
    "limit": 50
}

user_tracks_response = requests.get("https://api.spotify.com/v1/me/tracks", params=user_params, headers=user_headers)
print(user_tracks_response.json())