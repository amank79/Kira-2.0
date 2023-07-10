from pywikihow import search_wikihow
from chatbot import say, get_command, say_david


def wikihow(voice):
    say("Starting the learning mode.",voice)
    while True:
        say("Can you please tell me what you want to learn.",voice)
        how = get_command()
        try:
            if "exit" in how.lower() or "close" in how.lower():
                say("Okay, exiting the mode.",voice)
                break
            if "error" not in how.lower():
                max_results = 1
                how_to_info = search_wikihow(how, max_results)
                assert len(how_to_info) == 1
                say_david(how_to_info[0].summary)
        except Exception as e:
            say("Sorry, I couldn't find any information for that.",voice)