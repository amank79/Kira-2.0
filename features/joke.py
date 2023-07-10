import requests
from chatbot import say
def get_joke():
    base_url = "https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Spooky"
    while True:
        response = requests.get(base_url)
        data = response.json()
        if data["type"] == "single":
            return data["joke"]
        elif data["type"] == "twopart":
            return f"{data['setup']} {data['delivery']}"
        else:
            print("Sorry, I couldn't fetch a joke at the moment.")

def jokes(voice):
    joke = get_joke()
    say(joke,voice)