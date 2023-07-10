import webbrowser
import pyautogui
from time import sleep
from chatbot import say, get_command

def send_whatsapp_message(voice):
    person_map = {}

    with open("C:/Python projects/kira-Ai2.0/Data/recipients.txt", "r") as file:
        for line in file:
            name, number = line.strip().split(":")
            person_map[name] = number

    for i, person in enumerate(person_map, start=1):
        print(f"{i}. {person.title()}")
    say("Who you want to send message",voice)
    recipient_name = get_command()

    if recipient_name.lower() not in person_map:
        print("Kira --> Invalid recipient")
        return

    recipient_number = person_map[recipient_name.lower()]

    say("What's the message?",voice)
    message = get_command()
    message = message.lower()

    try:
        webbrowser.open(f"https://web.whatsapp.com/send?phone={recipient_number}&text={message}")
        say("WhatsApp opened",voice)
        sleep(15)  # Wait for WhatsApp to load
        pyautogui.press("enter")  # Send the message

        say("Message sent successfully",voice)
    except Exception as e:
        print("Kira --> An error occurred while sending the message:", str(e))

# Call the function to send the WhatsApp message

