import speech_recognition as sr
import pyttsx3 as px
import pywhatkit as pt
import wikipedia as wp
import webbrowser
engine = px.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)


from main import takeCommand,speak

query=takeCommand().lower()

def searchGoogle(query):
    if"google"in query:
        import wikipedia as googleScrap
        query=query.replace("jarvis","")
        query=query.replace("google search","")
        query=query.replace("google","")
        speak("This is what i found on google")
        try:
            pt.search(query)
            result=googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable out available")
def searchYoutube(query):
    if"youtube" in query:
        speak("THis is what i found for you search")
        query=query.replace("youtube search","")   
        query= query.replace("youtube","")      
        query=query.replace ("jarvis","")
        web="https://www.youtube.com/results?search_query="+query 
        webbrowser.open(web)
        pt.playonyt(query)
        speak("Done,mam")  
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia.....")
        query=query.replace("wikipedia","")
        query=query.replace("search wikipedia","")
        query=query.replace("jarvis","")
        results=wp.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

