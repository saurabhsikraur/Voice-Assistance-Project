import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib #pip install secure-smtplib
import cv2 #pip install opencv-python
import random
import requests
from requests import get
import pywhatkit as kit  #pip install pywhatkit
import sys
import pyjokes #pip install pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("i am David ,sir! please tell me how may i help you")

#to convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hindi-ind')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('laukeshyadac@gmail.com', 'Laukesh@123')
    server.sendmail('laukeshyadac@gmail.com', to, content)
    server.close()

#for news update
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=22b808cd326c4a2fb89af5a37bbfe6a7'

    main_page = requests.get(main_url).json()
    print(main_page)
    articles = main_page["articles"]
    print(articles)
    head = []
    day = ["first", "second", "third", "fourth", " fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open youtube' in query:
            speak("sir, what should i search on youtube")
            ct = takeCommand().lower()
            kit.playonyt(f"{ct}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Saurabh.")

        elif 'tell me joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif ' power point presentation' in query:
            speak("opening power point presentation")
            power = r""
            os.startfile(power)

        elif 'what is your name' in query or 'who are you' in query:
            speak("my friends call me")
            speak("heera")
            print("my friends call me", "heera")

        elif 'how are you' in query:
            speak("i am fine, thank you")
            speak("how are you, sir")

        elif 'fine' in query or 'good' in query:
            speak("it's good to know that you are fine")

        #to find location
        elif 'where i am' in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir due to network issue i am not able to find where we are.")
                pass

        elif "shut down the system" in query:
            os.system("shutdown /r /t s")

        elif "restart the system" in query:
            os.system("shutdown /r /t s")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()


        elif 'play music' in query:
            music_dir ="C:\\Users\\saura\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your Ip address is {ip}")

        elif 'developer name' in query:
            speak("Saurabh yadav")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2210.5.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)

        elif 'open code' in query:
            codePath ="C:\\Users\\saura\\PycharmProjects\\pythonProject\\David.py "
            os.startfile(codePath)


        elif 'tell me news' in query:
            speak("please wait sir fetching the letest news")
            news()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'email to ritik' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower( )
                to = "cse21160@glbitm.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif'send a email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)

                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif'no thanks' in query or 'exit' in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir do you have any other work")