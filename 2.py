import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit as pw

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour <= 16:
        speak("Good Afternoon Sir")
    elif 16 < hour <= 19:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("I am Jarvis! How can I help you, sir?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.energy_threshold = 4000
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Please say it again..")
        return "None"
    return query


greet()

while True:
    query = take_command().lower()

    # Logic for executing tasks based on query
    if "wikipedia" in query:
        speak("Searching Wikipedia... ")
        query = query.replace("wikipedia", "").strip()
        results = wikipedia.summary(query, sentences=3)
        speak("According to the information I found on Wikipedia")
        print(results)
        speak(results)
    elif "open google" in query:
        print("Opening Google...")
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open stackoverflow" in query:
        print("Opening Stack Overflow...")
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
    elif "open wikipedia" in query:
        print("Opening Wikipedia...")
        speak("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")
    elif "open facebook" in query:
        print("Opening Facebook...")
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in query:
        print("Opening YouTube...")
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    if "play" in query and "on youtube" in query:
        song = query.replace("play", "").replace("on youtube", "").strip()
        print(f"Playing song: {song} on YouTube")
        speak(f"Playing song: {song} on YouTube")
        pw.playonyt(song)
    elif "open photos" in query:
        print("Opening photos...")
        speak("Opening photos")
        photo_path = "D:\\Laxman\\Anurag"  # Replace with your photo directory
        photos = os.listdir(photo_path)
        photo = random.choice(photos)
        os.startfile(os.path.join(photo_path, photo))
    elif "search" in query:
        search_query = query.replace("search", "").strip()
        if search_query:
            print("Searching...")
            pw.search(search_query)
        else:
            print("Please provide a search query.")
    elif "time" in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {str_time}")
    elif "open vs" in query:
        # Replace with your VS Code path
        vs_path = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vs_path)
    elif " quit" in query:
        exit()
