import pyttsx3
import speech_recognition 
import pyautogui
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
import random
import webbrowser


for i in range(3):
    user_ip=input("Enter Password to open Jarvis : ")
    pw_file=open("pass.txt",'r')
    pw=pw_file.read()
    pw_file.close()
    if(user_ip==pw):
        print("Welcome,mam : pls speak wake up to load me up")
        break
    elif(i==2 and user_ip!=pw):
        exit()
    elif(user_ip!=pw):
        print("Try again")
 





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
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
                    speak("Ok mam , You can me call anytime")
                    break 
                elif "hello" in query:
                    speak("Hello mam, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, mam")
                elif "how are you" in query:
                    speak("Perfect, mam")
                elif "thank you" in query:
                    speak("you are welcome, mam")
                elif 'tired' in query:
                    speak("Playing you favourite song,mam")
                    a=(1,2,3)
                    b=random.choice(a)
                    if b==1:
                        webbrowser.open('https://www.youtube.com/watch?v=wncNcu6jEgs')
                    elif b==2:
                        webbrowser.open('https://www.youtube.com/watch?v=w8Zcr9IhFO0')
                    else:
                        webbrowser.open('https://www.youtube.com/watch?v=2IlzAP9ibT0')


                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,mam")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, mam")
                    volumedown()
                elif "open" in query:
                    from DIctapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from DIctapp import closeappweb
                    closeappweb(query)   

                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query) 
                 ## news functions
                elif 'news' in query:
                    from NewsRead import latest_news
                    latest_news()

                ## calculate function
                elif 'calculate' in query:    
                    from Calculates import Calcu,wolfRamAlpha
                    query=query.replace("calculate","")
                    query=query.replace("jarvis","")
                    Calcu(query)
                ## Whatsapp function
                elif 'whatsapp' in query:
                    from Whatsapp import sendMessage
                    sendMessage()
               
                elif "temperature" in query:
                    search = "temperature in bhopal"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in bhopal"
                    url = f"https://www.google.com/search?q={search}"
                    
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    weath = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {weath}") 
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,mam")
                    exit()

                elif "remember that " in query:
                    rememberMsg=query.replace('remember that',"")    
                    rememberMsg=query.replace('jarvis',"")   
                    speak("You told me to remember that"+rememberMsg)
                    remember=open("Remember.txt","w")
                    remember.write(rememberMsg)
                    remember.close()
                elif "what do you remember" in query:
                    remember=open('Remember.txt','r')
                    speak("You told me "+remember.read())   
                    ## shutdown function 
                elif "shutdown" in query:
                    speak("Are u sure u want to shutdown the system")
                    shutdown =input("Do you wish to shutdown your computer ? (yes/no)")
                    if shutdown=='yes':
                        os.system("shutdown /s /t 1")
                    elif shutdown=="no":
                        break   
               
                    





