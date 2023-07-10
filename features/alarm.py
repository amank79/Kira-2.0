import datetime
import pygame


def alarm(query):
    timehere = open("C:/Python projects/kira5.0/Data/alarm.txt", "a")
    timehere.write(query)
    timehere.close()
    ring(query)

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("kira", "")
    timenow = timenow.replace("set alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)

    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime >= Alarmtime:
            print("Alarm ringing, sir")
            play_alarm_sound()
            break

def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Python projects/kira5.0/Data/alarm.mp3")
    pygame.mixer.music.play()