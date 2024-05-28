import requests
import json
import pyttsx3
from main import speak
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)




def latest_news():
    apidict={"business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2b89cb4638f84dc9a82cc661841319f8",
             'entertainment':'https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=2b89cb4638f84dc9a82cc661841319f8',
             'health':'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=2b89cb4638f84dc9a82cc661841319f8',
             'politics':'https://newsapi.org/v2/top-headlines?country=in&apiKey=2b89cb4638f84dc9a82cc661841319f8',
             'sports':'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=2b89cb4638f84dc9a82cc661841319f8',
             
             'technology':'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=2b89cb4638f84dc9a82cc661841319f8'

}
    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [politics]")
    field = input("Type field news that you want: ")
    for key ,value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

    