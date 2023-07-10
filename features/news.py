from chatbot import say , get_command , say_david
import requests

def latestnews(voice):
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=246b169effe24c81b632371b85404e9e",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=246b169effe24c81b632371b85404e9e",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=246b169effe24c81b632371b85404e9e",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=246b169effe24c81b632371b85404e9e",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=246b169effe24c81b632371b85404e9e",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=246b169effe24c81b632371b85404e9e"
    }

    say("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]", voice)
    field = get_command()

    url = api_dict.get(field.lower())

    if url is None:
        print("Invalid field. Please try again.")
        return

    response = requests.get(url)

    if response.status_code == 200:
        news = response.json()
        say("Here is the first news.", voice)

        articles = news["articles"]
        for article in articles:
            title = article["title"]
            say_david(title)
            news_url = article["url"]
            print(f"For more info, visit: {news_url}")
            say_david("Do you want to here more headlines")
            choice = get_command()
            if "no" in choice.lower():
                break

        say("That's all", voice)
    else:
        say("Failed to retrieve news.")

