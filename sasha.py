import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyjokes

engine = pyttsx3.init('sapi5') #sapi 5 is for taking inputs as voice
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Sasha. How can i help you today?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maditi439@gmail.com', 'xxxxx')
    server.sendmail('aditimohanp111@gmail.com', to, content)
    server.close() 

if _name_ == "_main_":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
        
            print(results)
            speak(results)

        elif 'open codechef' in query:
            webbrowser.open("codechef.com")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
        
        elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")    

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'open zerodha' in query:
            webbrowser.open("kite.zerodha.com")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")
    

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'open torrent' in query: 
            speak(f"sorry it is illegal and i am not allowed to do so")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Documents\\songsproj'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        elif 'joke' in query:
            jok = pyjokes.get_joke()
            speak(jok)    
            print(jok)

        elif 'created you' in query:
            speak(f"i was created by aditi")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aditimohanp111@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="J962XX-2RVJTWYG79"
            client = wolframalpha.Client('J962XX-2RVJTWYG79')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif 'shutdown' in query:
            exit(0)
