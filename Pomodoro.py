from datetime import datetime, timedelta
import time
import os
import json
import keyboard

## read the json file to get the number of breaks and Pomodoro sessions
work_sesh=1
break_sesh=1
json_pomodoro=open("Pomodoro.json","r")
for line in json_pomodoro:
    if 'Pomodoro' in line:
        work_sesh+=1
    elif 'Break' in line:
        break_sesh+=1
json_pomodoro.close()

## function to document the session in the json file
def document_sesh(type):
        json_pomodoro=open("Pomodoro.json","a")
        json_pomodoro.write(json.dumps({type:time.strftime("%d/%m/%Y  %I:%M%p")}))
        json_pomodoro.write("\n")
        json_pomodoro.close()

## define Pomodoro timer periods
timer=timedelta(minutes=25)
breaktime=timedelta(minutes=5)
zero=timedelta(minutes=0)

## menu to choose between a)Pomodoro b)Break c)Stats d)Quit
response=''
while(response not in ("a","b","c","d")):
    time.sleep(0.5)
    os.system('cls')
    print("What would you like to do?\n\n\ta)Start a Pomodoro session\n\tb)Take a break\n\tc)Check your statistics\n\td)Quit\n")
    response=input("Please type a,b or c: \n")

    if response=='a':
        os.system('cls')
        print(f"Pomodoro session #{work_sesh}:")
        while timer>zero:
            print(timer-timedelta(seconds=1),end="\r")
            timer=timer-timedelta(seconds=1)
            time.sleep(1)
        document_sesh("Pomodoro")
        print(f"Pomodoro session #{work_sesh} is over")
        work_sesh+=1
        response=''

    elif response=='b':
        os.system('cls')
        print(f"Break session #{break_sesh}:")
        while breaktime>zero:
            print(breaktime-timedelta(seconds=1),end="\r")
            breaktime=breaktime-timedelta(seconds=1)
            time.sleep(1)
        print(f"Break session #{break_sesh} is over")
        document_sesh("Break")
        break_sesh+=1
        response=''

    elif response=='c':
        os.system('cls')
        print("Statistics:")
        print(f"Pomodoro sessions: {work_sesh}")
        print(f"Break sessions: {break_sesh}")
        keystroke=keyboard.read_key()
        response=''


    elif response=='d':
        os.system('cls')
        exit("Sorry to see you go")
