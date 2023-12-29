import pyttsx3  # Text-to-speech library
import datetime
import speech_recognition as sr  # Speech recognition library
import wikipedia
import webbrowser
import os
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greet():
    current_time = datetime.datetime.now().strftime("%H:%M")
    if 5 <= int(current_time.split(":")[0]) < 12:
        speak("Good morning!")
    elif 12 <= int(current_time.split(":")[0]) < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I'm Bucky, your virtual assistant. How can I assist you today?")
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return None
if __name__ == "__main__":
    greet()
    while True:
        query = take_command().lower()

        if query is None:
            continue

        if 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")

        elif 'search' in query:
            speak("What would you like me to search for?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'wikipedia' in query:
            speak("What would you like to know from Wikipedia?")
            search_query = take_command()
            try:
                result = wikipedia.summary(search_query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("I found multiple results. Please be more specific.")

        elif 'exit' in query:
            speak("Goodbye! Have a great day!")
            exit()
