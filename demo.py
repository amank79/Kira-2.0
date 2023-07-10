from features.wikipedia_search import wikipedia_search
from features.music import *
from features.dictionary import *
from features.weather import *
from features.joke import *
from features.news import *
from features.reminder import *
from features.wikihow import *
from features.current_time import *
from features.search_yg import *
from features.volume import *
from features.calculate import *
from features.program_open_close import *
from features.whatsapp import *
from features.play_game import *
from features.pdf_reader import *
from chatbot import ChatBot
import pyautogui
from features.select_voice import SelectVoiceFeature
from features.alarm import  *
from features.scheduling import *
import transformers
import numpy  as np
from features.clap import Tester
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration


if __name__ == "__main__":
    assistant_name = "Kira"
    creator_name = "Aman"

    ai_name = assistant_name
    user_name = ""
    voice_feature = SelectVoiceFeature()

    voice = voice_feature.voice
    print("----- Starting up", assistant_name, "-----")
    ai = ChatBot(name="Kira")

    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    transformers.logging.set_verbosity_error()
    blenderbot_tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
    blenderbot_model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")
    say_david("Clap to Wake-UP KIRA")
    Tester()

    while True:
        current_time = datetime.datetime.now()
        current_hour = current_time.hour

        if current_hour < 12:
            greeting = f"Good morning, Sir!. How are you today?"
        elif current_hour < 18:
            greeting = f"Good afternoon, Sir!. How's your day going?"
        else:
            greeting = f"Good evening, Sir!. How was your day?"

        say(greeting, voice)
        while True:
            query = get_command()

            if ai_name.lower() in query.lower():
                say(f"Yes, I'm {ai_name}. How can I assist you, {user_name}?",voice)


            elif "what can you do" in query.lower() or "what are your capabilities" in query.lower() or "what are you capable of" in query.lower():
                capabilities = "I can provide information, play music, give weather updates, share jokes, set reminders, " \
                               "perform searches, control video playback, adjust volume, open/close programs, send " \
                               "WhatsApp messages, play games, read PDF files, schedule your day, and more!"
                say(capabilities, voice)

            elif "tell me about yourself" in query.lower() or "who are you" in query.lower() or "what is your name" in query.lower():
                about_me = f"I am {assistant_name}. I am a chatbot created by {creator_name}. My purpose is to assist you with various tasks " \
                           "such as providing information, playing music, giving weather updates, sharing jokes, " \
                           "setting reminders, performing searches, and more. How can I assist you today?"
                say(about_me, voice)
                about_kira = "I am Kira, an AI chatbot created by Aman. My purpose is to assist you with various tasks " \
                             "such as providing information, playing music, giving weather updates, sharing jokes, " \
                             "setting reminders, performing searches, and more. How can I assist you today?"
                say(about_kira, voice)

            elif "set your name" in query.lower():
                new_name = query.lower().replace("set your name to", "").strip()
                ai_name = new_name
                say(f"Thank you for setting my name as {ai_name}.",voice)

            elif "set my name" in query.lower():
                new_name = query.lower().replace("set my name to", "").strip()
                user_name = new_name
                say(f"Thank you, {user_name}, for letting me know your name.",voice)

            elif "exit" in query.lower():
                say("Exiting the program. Goodbye!", voice)
                exit(0)


            elif "change voice" in query.lower():
                # Voice change code
                say("Name the voice that you want to use", voice)
                print("1. Sonia\n2. Prabhat")
                command = get_command()
                if "sonia" in command.lower():
                    voice = "sonia"
                    say("Voice successfully changed to Sonia", voice)

                elif "prabhat" in command.lower():
                    voice = "prabhat"
                    say("Voice successfully changed to Prabhat", voice)

                voice_feature.voice = voice  # Update the voice attribute
                voice_feature.update_voice()

            elif "dictionary" in query.lower() or "word" in query.lower():
                dictionary(voice)

            elif "whatsapp" in query.lower():
                send_whatsapp_message(voice)

            elif any(keyword in query.lower() for keyword in ["play music on spotify", "spotify "]):
                music(voice)

            elif "open spotify" in query.lower():
                say("Opening Spotify...", voice)
                os.startfile(
                    "C:/Users/LENOVO/AppData/Roaming/Spotify/Spotify.exe")

            elif "time" in query.lower():
                time(voice)

            elif "weather in" in query.lower():
                city = query.lower().replace("weather in", "").strip()
                weather_info = get_weather(city)
                say(weather_info, voice)

            elif "news" in query.lower():
               latestnews(voice)

            elif "reminder" in query.lower():
                set_reminder(voice)

            elif any(i in query.lower() for i in ["thank", "thanks"]):
                response = np.random.choice(
                    ["You're welcome!", "Anytime!", "No problem!", "Cool!", "I'm here if you need me!",
                     "You're welcome!"])
                say(response, voice)

            elif "google" in query.lower():
                searchGoogle(query,voice)

            elif "youtube" in query.lower():
                searchYoutube(query,voice)

            elif "pause video" in query.lower():
                pyautogui.press("k")
                say("video paused",voice)
            elif "play video" in query.lower():
                pyautogui.press("k")
                say("video played",voice)
            elif "mute video" in query.lower():
                pyautogui.press("m")
                say("video muted",voice)

            elif "volume up" in query:
                say("Turning volume up,sir",voice)
                volumeup()

            elif "volume down" in query:
                say("Turning volume down, sir",voice)
                volumedown()

            elif "learning" in query.lower():
                wikihow(voice)

            elif "open wikipedia" in query.lower():
                wikipedia_search(voice)

            elif "joke" in query.lower():
                jokes(voice)

            elif "click my photo" in query:
                say("Get ready with pose", voice)
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                say("SMILE", voice)
                pyautogui.press("enter")

            elif "screenshot" in query.lower():
                im = pyautogui.screenshot()
                im.save("Data/screenshot.jpg")

            elif "open" in query.lower():
                open_program(query,voice)

            elif "close" in query.lower():
                close_program(query,voice)

            elif "set alarm" in query.lower():
                print("Input time example: 10 and 10 and 10")
                a = input("Please tell the time: ")
                alarm(a)
                say("Alarm successfully set",voice)

            elif "remember that" in query:
                rememberMessage = query.replace("remember that", "")
                say("You told me to " + rememberMessage,voice)
                remember = open("Remember.txt", "a")
                remember.write(rememberMessage)
                remember.close()
            elif "do you remember" in query:
                remember = open("Remember.txt", "r")
                say("You told me to " + remember.read(),voice)

            elif "calculate" in query.lower():
                query = query.replace("calculate", "")
                query = query.replace("kira", "")
                calc(query,voice)

            elif "schedule my day" in query.lower():
               schedule_on(voice)

            elif "show my schedule" in query.lower():
                show_schedule(voice)

            elif " lets play game" in query.lower():
                game_play(voice)

            elif "read pdf" in query.lower():
               pdf_read(voice)

            else:
                if query == "ERROR":
                    continue
                else:
                    # Tokenize the user input
                    inputs = blenderbot_tokenizer(query, return_tensors="pt")

                    # Generate the response from the model
                    response_ids = blenderbot_model.generate(**inputs, max_length=100)

                    # Decode the generated response
                    response = blenderbot_tokenizer.decode(response_ids[0], skip_special_tokens=True)

                    say(response, voice)

