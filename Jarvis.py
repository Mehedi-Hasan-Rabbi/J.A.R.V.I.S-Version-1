import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from email_credential import senderemail, epwd
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty("voice", voices[0].id)
        speak("Hello this is Jarvis")
    
    if voice == 2:
        engine.setProperty("voice", voices[1].id)
        speak("Hello this is Friday")
    
def time():
    Time  = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is: ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is: ")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening sir!") 
    else:
        speak("Good Night sir!")

def wishme():
    speak("Welcome back sir!")
    greeting()
    str=engine.getProperty('voice')
    if 'DAVID' in str: 
        speak("Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")
    else:
        speak("Friday at your service, plesase tell me how can i help you!")

def takeCommandCMD():
    query = input("Please tell me how can I help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizning...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Can you please try that again?")
        #I didn\'t quiet catch you sir. Can you please try that again?
        return "None"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('stmp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsappmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key='1a1ffd37e19842368a96e389ca546411')
    speak('what topic you need the news about?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic, 
                                    language='en', 
                                    page_size=5)

    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    
    speak("That's it for now i'll update you in some time")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\Mehedi Hasan\\Desktop\\J.A.R.V.I.S\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def password_generator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 10
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flipCoin():
    speak("Okey sir, flipping a coin")
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    print(toss)
    speak("I flippend the coin and you got " + toss)

def rollDie():
    speak("Okey sir rolling a die for you")
    die = ['1', '2', '3', '4', '5', '6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    print(roll)
    speak("I rolled a die and you got " + roll)

def systemInfo():
    cpu = str(psutil.cpu_percent())
    speak("CPU is at " + cpu + "percent")
    battery = psutil.sensors_battery()
    speak("Battery is at " + str(battery.percent) + "percent")
