# api_keys.py
import spotipy
from spotipy import SpotifyOAuth

weather_api_key = 'your_weather_api_key'
news_api_key = "your_news_api_key"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='Your_client_id',
                                                   client_secret='Your_secret_id',
                                                   redirect_uri='http://localhost:8000/callback',
                                                   scope='user-modify-playback-state'))
username = "your_email_id"
password = "your_password"
