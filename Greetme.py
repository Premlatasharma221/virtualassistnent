import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning,mam")
    elif hour>=12 and hour<16:
        speak("Good Afternoon ,mam")

    else:
        speak("Good Evening,mam")

    speak("Please tell me, How can I help you ?")

