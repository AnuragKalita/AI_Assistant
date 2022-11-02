import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speck(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speck("Good Morning!")
    elif hour>=12 and hour<18:
        speck("Good Afternoon!")
    else:
        speck("Good Evening!")

    speck("I am your personal care assistance.")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speck("Listening.")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speck("Recognizing.")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        speck("Say that again please.")
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speck('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speck("According to WikiPedia")
            print(results)
            speck(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = '' # Enter your music directory name
            songs = os.listdir(music_dir)
            print(songs)
            speck("Playing Music.")
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speck(f"Sir, the time is {strTime}")
        elif 'good night' in query:
            speck('Good night sweet dreams sir!')
            quit()
