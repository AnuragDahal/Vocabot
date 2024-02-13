import pyttsx3#pip install pyttsx3
import datetime
import speech_recognition as sr#pip install speechRecognition
import wikipedia
import webbrowser
import os
import random
import pywhatkit as pw
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
   hour=int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morning Sir")
   elif hour>=12 and hour<=16:
         speak("Good Afternoon Sir")
   elif hour>16 and  hour<=19:
      speak("Good Evening Sir")
   else:
      speak("GoodNight Sir")
   speak("I am Jarvis! How can I help you sir")

def takecommand():
   '''It takes microphone input from the user as input
   '''
   r=sr.Recognizer()
   with sr.Microphone() as source:
      print('Listening....')
      r.energy_threshold
      r.pause_threshold=1
      audio=r.listen(source)
   try:
        print("Recognizing")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said {query}")

   except Exception as e:
     print(e)
     print("Please Say it again..")
     return "None"
   return query
    #  speak("Please say it again..")
# if __name__==";__main__":
greet()
while True:
        query= takecommand().lower()

      # logic for executing tasks on query
        if "wikipedia" in query:
            speak("Searching wikipedia... ")
            query=query.replace("wikipedia",'')
            results=wikipedia.summary(query,sentences=3)
            speak("According to the information I found on wikipedia")
            print(results)
            speak(results)
        elif "open google" in query:
            print("opening....")
            speak("opening")
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            print("opening....")
            speak("opening")
            webbrowser.open("stackiverflow.com")
        elif "open wikipedia" in query:
            print("opening....")
            speak("opening")
            webbrowser.open("wikipedia.com")
        elif "open facebook" in query:
            print("opening....")
            speak("opening")
            webbrowser.open("facebook.com")
        elif "open youtube" in query:
            speak("Opening")
            webbrowser.open("youtube.com")
        elif ""in query:
            print("searching")
            pw.search(query)
        # elif "play music" in query:
            # music=add location
            #songs= os.listdir(music)
            # print(songs)  
            # os.startfile(os.path.join(music,songs[0])) include frandom module to print radnom songs
        elif "time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"the time is {strtime}")  
        elif "open vs" in query:
            path="C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "open photos" in query:
         photo_path="D:\\Laxman\\Anurag"
         photos=os.listdir(photo_path)
         photo=random.randint(0,len(photos))
         os.startfile(os.path.join(photo_path,photos[photo]))
        elif "quit" in query:
            exit()
        elif "search" in query:
          search_query = query.replace("search", "").strip()
          if search_query != "":
            print("Searching...")
            pw.search(search_query)
          else:
            print("Please provide a search query.")


            
               
    
        
 


