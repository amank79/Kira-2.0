import datetime
from chatbot import say
def time(voice):
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    say(f"Sir, the current time is {current_time}",voice)
