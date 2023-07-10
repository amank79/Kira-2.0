import wikipedia
from chatbot import get_command, say ,say_david


def wikipedia_search(voice):
    say("What would you like to search on Wikipedia?",voice)

    search_query = get_command()

    while True:

        if any(keyword in search_query.lower() for keyword in ["close wikipedia", "exit"]):
            say("Closing Wikipedia.",voice)
            break

        if "error" not in search_query.lower():

            try:
                summary = wikipedia.summary(search_query, sentences=2)
                say_david(summary)

                say("Would you like to know more?",voice)
                more_query = get_command()

                if "yes" in more_query.lower():
                    full_summary = wikipedia.summary(search_query)
                    # say_default(full_summary)

            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:5]  # Limiting to 5 options
                options_text = "\n".join(options)
                say_david(f"Multiple options found. Please choose one:\n{options_text}")

            except wikipedia.exceptions.PageError:
                say("Sorry, I couldn't find any Wikipedia page for that topic.",voice)

        say("What else would you like to search on Wikipedia?",voice)
        search_query = get_command()
