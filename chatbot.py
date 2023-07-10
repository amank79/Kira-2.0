import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import subprocess
import speech_recognition as sr
import datetime
import pyttsx3
import os
from googletrans import Translator

class ChatBot():
    def __init__(self, name):
        self.name = name
# Only use when user talking in hindi

    # def speech_to_text(self):
    #     recognizer = sr.Recognizer()
    #
    #     with sr.Microphone() as mic:
    #         print("Listening...")
    #         audio = recognizer.listen(mic)
    #         self.text = "ERROR"
    #
    #     try:
    #         speech = recognizer.recognize_google(audio, language='hi-IN')
    #         # print("Recognized Speech (Hindi):", speech)
    #
    #         # Check if the recognized speech is in English
    #         is_english = all(ord(char) < 128 for char in speech)
    #
    #         if is_english:
    #             self.text = speech
    #             # print("Detected English speech:", self.text)
    #         else:
    #             translator = Translator()
    #             translation = translator.translate(speech, src='hi', dest='en')
    #             self.text = translation.text
    #             print("You -->", self.text)
    #     except:
    #         print("You --> ERROR")


    # hindi to hindi
    #     def speech_to_text(self):
    #         recognizer = sr.Recognizer()
    #
    #         with sr.Microphone() as mic:
    #             print("Listening...")
    #             audio = recognizer.listen(mic)
    #             self.text = "ERROR"
    #
    #         try:
    #             speech = recognizer.recognize_google(audio, language='hi-IN')
    #             self.text = speech
    #             print("You:", self.text)
    #         except:
    #             print("Me --> ERROR")


    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...")
            audio = recognizer.listen(mic)
            self.text = "ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me  --> ", self.text)
        except:
            print("Me  -->  Please, say that again")




    def text_to_speech_prabhat(self, text):
        voice = 'en-IN-PrabhatNeural'
        command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "Data/data.mp3"'

        # Execute the command and capture the output
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('Data/data.mp3')
        print(f"Kira --> {text}")

        try:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)


        except Exception as e:
            print(e)

        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()

    def text_to_speech_sonia(self, text):
        voice = 'en-GB-SoniaNeural'
        command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "Data/data.mp3"'

        # Execute the command and capture the output
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('Data/data.mp3')
        print(f"Kira --> {text}")

        try:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)


        except Exception as e:
            print(e)

        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()

    def text_to_speech_david(self, text):
        print("Kira -->", text)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Set voice to David
        engine.setProperty('rate', 150)  # Set rate to 150
        engine.say(text)
        engine.runAndWait()

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

ai=ChatBot("Kira")

def get_command():
    ai.speech_to_text()
    return ai.text

def say(text,voice):
    if voice == 'sonia':
        ai.text_to_speech_sonia(text)
    elif voice == 'prabhat':
        ai.text_to_speech_prabhat(text)

def say_david(text):
    ai.text_to_speech_david(text)
