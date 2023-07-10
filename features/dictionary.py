import requests
import json
from chatbot import say, get_command
def get_word_definition(word):
    url = f"https://dictionaryapi.com/api/v3/references/sd3/json/{word}?key=1e82ec93-2b96-445c-bdd2-abed12306850"
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        if isinstance(data, list):
            if len(data) > 0 and 'shortdef' in data[0]:
                return data[0]['shortdef'][0]
            else:
                return "No definition found."
        else:
            return "No definition found."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
def ai_speak(word,voice):
    while True:
        if word == "exit":
            break
        else:
            definition = get_word_definition(word)
            say(definition,voice)
            say("Would you like to hear another definition?",voice)
            response = get_command()
            if "yes" in response.lower():
                say("Sure, please tell me the word.",voice)
                word = get_command()
            else:
                say("Okay, let me know if you need assistance with anything else.", voice)
                return

def dictionary(voice):
    say("Sure, please tell me the word.",voice)
    word = get_command()
    while True:
        if "exit" in word.lower():
            say("Okay, let me know if you need assistance with anything else.",voice)
            break
        elif "error" in word.lower():
            say("Sorry, I couldn't catch the word. Please try again.",voice)
            word = get_command()
        else:
            word = word.strip().split()[0]
            ai_speak(word,voice)
            break
