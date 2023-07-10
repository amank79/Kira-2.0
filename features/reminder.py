import datetime
from chatbot import say
def set_reminder(voice):
    say("Please type on keyboard. What is the reminder for? ",voice)
    reminder_text = input()
    say("When should the reminder be triggered? (Format: HH:MM AM/PM) ",voice)
    reminder_time = input()

    try:
        reminder_time = datetime.datetime.strptime(reminder_time, "%I:%M %p")
    except ValueError:
        say("Invalid time format. Please enter time in the format: HH:MM AM/PM",voice)
        return

    current_time = datetime.datetime.now()
    delta_time = reminder_time - current_time

    if delta_time.total_seconds() <= 0:
        say("The reminder time should be in the future.",voice)
    else:
        say("Reminder set successfully!",voice)
        datetime.time.sleep(delta_time.total_seconds())
        say(f"Reminder: {reminder_text}",voice)

