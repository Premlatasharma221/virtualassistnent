import wolframalpha
import pyttsx3
import speech_recognition
from main import speak
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def wolfRamAlpha(query):

    apikey="92HAV9-QP5JWT49LR"
    requester=wolframalpha.Client(apikey)
    requested=requester.query(query)

    try:
        answer=next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calcu(query):
    term=str(query)
    term=term.replace("jarvis","")
    term=term.replace("multiply","*")
    term=term.replace("plus","+")
    term=term.replace("Divide","/")
    term=term.replace("minus","-")

    final=str(term)
    try:
        results=wolfRamAlpha(final)
        print(f"{results}")       
    except:
        speak("The voice is not answerable") 



