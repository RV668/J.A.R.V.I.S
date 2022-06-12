from unicodedata import name
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening! Sir")

    speak("I am Jarvis. How may I help you?")

def takeCommand():
   
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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query    

def current_date():
    datetime.date

if __name__=="__main__":
    wishMe()
    # while True:
    while True:
        query = takeCommand().lower()

    # logic for excecuting tasks based on query
        
        
        if 'jarvis' or 'ai' in query:
        
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("Okay sir, opening youtube for you.")
                webbrowser.open("youtube.com")

            elif 'open scratch' in query:
                speak("Okay sir, opening scratch for you.")
                webbrowser.open("scratch.mit.edu")
                
            elif 'open between us' in query:
                speak("Okay sir, opening between us for you.")
                webbrowser.open("https://www.betweenus.in/Parent/Default.aspx?count=1")
                
            elif 'open beanstalk reader' in query:
                speak("Okay sir, opening benstalk reader for you.")
                webbrowser.open("https://beanstalk.kitaboo.com/reader/MobileReader/index.html#/bookshelf")

            elif 'open google.com' in query:
                speak("Okay sir, opening google for you.")
                webbrowser.open("google.com")

            elif 'open bing' in query:
                speak("Okay sir, opening bing for you.")
                webbrowser.open("bing.com")

            elif 'open cs timer' in query:
                speak("Okay sir, opening cs timer for you.")
                webbrowser.open("cstimer.net")

            elif 'amazon' in query:
                speak("Okay sir, opening amazon for you.")
                webbrowser.open("amazon.com")

            elif 'open gmail' in query:
                speak("Okay sir, opening gmail for you.")
                webbrowser.open("gmail.com")

            elif 'open github' in query:
                speak("Okay sir, opening github for you.")
                webbrowser.open("https://github.com/")

            elif 'open stack overflow' in query:
                speak("Okay sir, opening stack overflow for you.")
                webbrowser.open("https://stackoverflow.com/users/19312574/ranvijay-pahalwan")

            elif 'open spotify' in query:
                speak("Okay sir, opening spotify for you.")
                webbrowser.open("https://open.spotify.com/?nd=1")

            elif 'play music' in query:
                music_dir = 'E:\\web page\\J.A.R.V.I.S\\music'
                songs = os.listdir(music_dir)
                speak("Okay sir, playing music for you.")
                os.startfile(os.path.join(music_dir, songs[0+8]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'the date' in query:
                strDate = datetime.date.today()
                speak(f"Sir, the date is {strDate}")       

            elif 'open vs code' in query:
                speak("Okay sir, opening vs code for you.")
                codePath = "C:\\Users\\ABC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open microsoft edge' in query:
                speak("Okay sir, opening microsoft edge for you.")
                edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                os.startfile(edgePath)

            elif 'open google chrome' in query:
                speak("Okay sir, opening google chrome for you.")
                gcPath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(gcPath)

            elif 'open pycharm' in query:
                speak("Okay sir, opening pycharm for you.")
                pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1\\bin\\pycharm64.exe"
                os.startfile(pyPath)

            elif 'quit' in query:
                quit()

            elif 'thank you' in query:
                speak("You're welcome Sir!")
                print("You're welcome Sir!")
                quit()