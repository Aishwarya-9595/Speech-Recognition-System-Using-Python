
import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import datetime
import calendar
import random
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import time
import os.path

from time import sleep

#warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n\nListening...")
        audio = recog.listen(source)

    data = " "

    try:

        data = recog.recognize_google(audio)
        print("\nYou said: " + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data


def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."


def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello"]

    response = ["howdy", "whats good", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]

while True:

    try:
        text = rec_audio()
        speak = ""

        if call(text):

            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today
                response(speak)

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."
                response(speak)

            elif 'who is' in text:                 
                person=text.replace('who is','') 
                info=wikipedia.summary(person,2)    
                speak=speak + info                         
                response(speak)
            
            elif "who are you" in text or "define yourself" in text:
                speak = speak + """Hello, I am an Assistant. Your Assistant. I am here to make your life easier.  
                You can command me to perform various tasks such as solving mathematical questions or opening 
                applications etcetera."""
                response(speak)

            elif "your name" in text:
                speak = speak + "My name is Assistant."
                response(speak)

            elif "who am I" in text:
                speak = speak + "You must probably be a human."
                response(speak)

            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "It is a secret."
                response(speak)

            elif "how are you" in text:
                speak = speak + "I am fine, Thank you!"
                speak = speak + "\nHow are you?"
                response(speak)

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that you are fine"
                response(speak)

            elif 'joke' in text.lower():
                speak=talk(pyjokes.get_joke())
                response(speak)

            elif "open" in text.lower():

                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                    )
                    response(speak)

                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    os.startfile(
                        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office"
                    )
                    response(speak)

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")
                    response(speak)

                elif "google" in text.lower():
                    speak = speak + "Opening Google\n"
                    webbrowser.open("https://google.com/")
                    response(speak)

            elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
                talk("for how many seconds do you want me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + " seconds completed. Now you can ask me anything"
                response(speak)

            elif "exit" in text or "quit" in text:
                exit()

    except:
        talk("I don't know that")

