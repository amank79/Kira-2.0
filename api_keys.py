# api_keys.py
import spotipy
from spotipy import SpotifyOAuth

weather_api_key = 'e3ef83c91a7bd6d33ec24a9662f9e4e9'
news_api_key = "246b169effe24c81b632371b85404e9e"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='Your_client_id',
                                                   client_secret='Your_secret_id',
                                                   redirect_uri='http://localhost:8000/callback',
                                                   scope='user-modify-playback-state'))
username = ""
password = ""
