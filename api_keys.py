# api_keys.py
import spotipy
from spotipy import SpotifyOAuth

weather_api_key = 'e3ef83c91a7bd6d33ec24a9662f9e4e9'
news_api_key = "246b169effe24c81b632371b85404e9e"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='04a35a51170d451b94e4ab0895a6a359',
                                                   client_secret='77cb87e9911a45628b93e01a8dd3b953',
                                                   redirect_uri='http://localhost:8000/callback',
                                                   scope='user-modify-playback-state'))
username = "aman67virendar@gmail.com"
password = "aman9492"