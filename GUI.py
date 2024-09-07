import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
from Jarvis import *
import threading

class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

def jarvis():
    wishme()
    while(True):
        query = takeCommandMic().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'hi how is it going' in query:
            speak('Great')
        
        elif 'how are you doing?' in query:
            speak('Very well, thanks.')
        
        elif 'nice to meet you.' in query:
            speak('Thank you.')
        
        elif 'it is a pleasure to meet you.' in query:
            speak('Thank you.')

        elif 'hi' in query or 'hello' in query:
            speak('Hello, sir how are you')

        elif 'how are you' in query:
            speak('I am doing jolly good, sir.')
        
        elif 'who are you' in query:
            speak('I am a virtual assistant and i need love')

        elif 'What is up' in query:
            speak('The sky is up but I am fine thanks. What about you?')

        elif 'switch to friday' in query:
            getvoices(2)
            wishme()

        elif 'switch to jarvis' in query:
            getvoices(1)
            wishme()

        elif 'text mode' in query:
            takeCommandCMD()

        elif 'voice mode' in query:
            takeCommandMic()

        elif 'email' in query:
            email_list = {
                'user':'sohag7731@gmail.com'
            }
            try:
                speak('To whom you want to send the mail?')
                name = takeCommandMic()
                receiver = email_list[name]
                speak("What is the subject of the email")
                subject = takeCommandMic()
                speak('what should i say?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("unable to send the email")

        elif 'whatsapp message' in query:
            user_name = {
                'myself': '+880 1XXX-XXXXXX',
                'teacher': '+880 1XXX-XXXXXX'
            }
            try:
                speak('To whom you want to send the whats app message?')
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("What is the message")
                message = takeCommandMic()
                sendwhatsappmsg(phone_no, message)
                speak("Messege has been send")
            except Exception as e:
                print(e)
                speak("unable to send the message")

        elif 'wikipedia' in query: # Wikipedia about iPhone
            speak('searching on wikipepia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'search on google' in query:
            searchgoogle()

        elif 'search on youtube' in query:
            speak('what should i search for on youtube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
        
        elif 'open youtube' in query:
            speak('Opening Youtube')
            wb.open("https://youtube.com")
        
        elif 'open google' in query:
            speak('Opening Google')
            wb.open("https://google.com")

        elif 'weather' in query:
            speak('say the city name?')
            city = takeCommandMic()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=61480aca76d2d5bfee195dd79e64c6de'

            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data['weather'] [0] ['description']
            temp = round((temp - 32) * 5/9)
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} city is like')
            speak('Temperature : {} degree celcius'.format(temp))
            speak('weather is {}'.format(desp))

        elif 'news' in query:
            news()

        elif 'read' in query:
            text2speech()

        elif 'open file explorer' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        elif 'open code blocks' in query:
            codepath = 'C:\\Program Files\\CodeBlocks\\codeblocks.exe'
            os.startfile(codepath)   

        elif 'open code' in query:
            codepath = 'C:\\Users\Mehedi Hasan\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(codepath)
        
        elif 'open word' in query:
            codepath = 'C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE'
            os.startfile(codepath)

        elif 'open power point' in query:
            codepath = 'C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE'
            os.startfile(codepath)

        elif 'open excel' in query:
            codepath = 'C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE'
            os.startfile(codepath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query:
            speak('what you want me to remember')
            data = takeCommandMic()
            speak("You want me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You want me to remember that " + remember.read())

        elif 'password' in query:
            password_generator()
        
        elif 'flip' in query:
            flipCoin()
        
        elif 'roll' in query:
            rollDie()

        elif 'system' in query:
            systemInfo()

        elif 'offline' in query:
            quit()

root = tk.Tk()
root.title("J.A.R.V.I.S")
lbl = ImageLabel(root)
lbl.pack()
lbl.load('Home.gif')
root.iconbitmap('icon.ico')
exit_button = tk.Button(root, text="Exit", width="49", bg="Blue", fg="white", command=root.destroy)
exit_button.pack()

############## Jarvis ################
thread = threading.Thread(target=jarvis)
thread.setDaemon(True)
thread.start()
######################################

root.mainloop()