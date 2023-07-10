from chatbot import say, get_command
from plyer import notification
from pygame import mixer

def schedule_on(voice):
    tasks = []  # Empty list
    say("Do you want to clear old tasks? (YES or NO)", voice)
    query = get_command().lower()
    if "yes" in query:
        file = open("Data/task.txt", "w")
        file.write("")
        file.close()
        say("How many tasks do you want to add", voice)
        no_tasks = int(get_command())
        for i in range(no_tasks):
            say(f"What is your {i+1} task", voice)
            task = get_command()
            tasks.append(task)
            file = open("Data/task.txt", "a")
            file.write(f"{i+1}. {tasks[i]}\n")
            file.close()
        say("Your tasks have been successfully added", voice)
    elif "no" in query:
        say("How many tasks do you want to add", voice)
        no_tasks = int(get_command())
        for i in range(no_tasks):
            say(f"What is your {i+1} task", voice)
            task = get_command()
            tasks.append(task)
            file = open("Data/task.txt", "a")
            file.write(f"{i+1}. {tasks[i]}\n")
            file.close()
        say("Your tasks have been successfully added", voice)

def show_schedule(voice):
    say("Showing your schedule in a second", voice)
    file = open("Data/task.txt", "r")
    content = file.read()
    file.close()
    mixer.init()
    mixer.music.load("Data/notification.mp3")
    mixer.music.play()
    notification.notify(
        title="My Schedule",
        message=content,
        timeout=15
    )
