import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from datetime import datetime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from Greetme import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temprature" in query:
                    search="temprature in Bhopal"
                    url=f"https://www.google.com/search?q={search}"
                    r= requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div",class_="BNeawe").text
                    speak(f"Current{search} is {temp}")
                elif "weather" in query:
                    search="weather in Bhopal"
                    url=f"https://www.google.com/search?q={search}"
                    r= requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    weath=data.find("div",class_="BNeawe").text
                    speak(f"Current{search} is {weath}") 
                elif "what is the time" in query:
                    strTime=datetime.now().strftime("%H:%M")
                    speak(f"Mam, the time is {strTime}")
                elif"finally sleep" in query:
                    speak("Going to sleep ,Mam")
                    exit()






      
                    
     

    
    
