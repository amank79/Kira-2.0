import webbrowser
import pywhatkit
import wikipedia as googleScrap
from chatbot import *
from time import sleep
import pyautogui


def searchGoogle(query,voice):
    if "google" in query.lower():
        query = query.replace("kira", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        query = query.replace("search", "")
        query = query.replace("Google", "")
        say("This is what i found on google",voice)

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            say(result,voice)

        except:
            say("No speakable output available",voice)

def searchYoutube(query,voice):
    if "youtube" in query.lower():
        say("This is what i found for your search!",voice)
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("YouTube", "")
        query = query.replace("kira", "")
        query = query.replace("search","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        sleep(2)
        pyautogui.press("F")
        say("Done, Sir",voice)

