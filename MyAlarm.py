import pyttsx3
import datetime
import os

engine = pyttsx3.init()
filepath = (os.getcwd())+"\\"+"alarms"
todayfile = (datetime.date.strftime(datetime.date.today(), "%d_%m_%Y"))+".txt"
file = filepath+"\\"+"Alarm_"+todayfile

try:
    with open(file, 'r') as myfile:
        content = myfile.read()
        while True:
            engine.say(content)
            engine.runAndWait()
except:
    print("file not found")