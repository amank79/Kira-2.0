import webbrowser
import speech_recognition as sr
from api_keys import sp
from chatbot import say

def open_spotify():
    webbrowser.get().open("https://open.spotify.com")

def get_song_name():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening for song name...")
        audio = recognizer.listen(mic)
    try:
        song_name = recognizer.recognize_google(audio)
        print("Song Name:", song_name)
        return song_name
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
    except sr.RequestError:
        print("Sorry, I encountered an error while processing your speech.")
    return ""

def play_song(song):
    results = sp.search(q=song, type='track', limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        print(f"Playing {song} on Spotify.")
    else:
        print("Sorry, the song was not found on Spotify.")


def music(voice):
    say("Sure! What would you like to hear, sir?", voice)
    if not sp.current_playback():
        say("Sorry, no device is available. Exiting music function.", voice)
        return

    song_name = get_song_name()
    if song_name:
        say(f"Playing the song {song_name}...", voice)
        play_song(song_name)
    else:
        say("Sorry, I didn't catch the song name. Please try again.", voice)



