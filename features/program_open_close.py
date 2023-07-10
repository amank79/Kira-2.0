import pyautogui
from chatbot import say,get_command
import psutil

# def open_program(voice,query):
#     query = query.replace("open", "")
#     query = query.replace("jarvis", "")
#     pyautogui.press("super")
#     pyautogui.typewrite(query)
#     pyautogui.sleep(2)
#     pyautogui.press("enter")

def close_program(program_name,voice):
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == program_name.lower():
                proc.kill()
                say(f"Closed {program_name} successfully.",voice)
                return
        except psutil.NoSuchProcess:
            pass
    say(f"Failed to find or close {program_name}.",voice)