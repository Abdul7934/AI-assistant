import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # You may need to adjust the player based on your system.

# Function to handle user commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! I'm Bucky, your AI assistant.")
    elif "how are you" in command:
        speak("I'm just a computer program, so I don't have feelings, but thanks for asking!")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I didn't understand your command.")

# Main loop for listening to user commands
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")

        user_command = recognizer.recognize_google(audio)
        print(f"You said: {user_command}")
        handle_command(user_command.lower())

    except sr.UnknownValueError:
        print("I didn't catch that. Could you please repeat?")
    except sr.RequestError as e:
        print(f"Sorry, I encountered an error: {e}")
import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # You may need to adjust the player based on your system.

# Function to handle user commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! I'm Bucky, your AI assistant.")
    elif "how are you" in command:
        speak("I'm just a computer program, so I don't have feelings, but thanks for asking!")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I didn't understand your command.")

# Main loop for listening to user commands
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")

        user_command = recognizer.recognize_google(audio)
        print(f"You said: {user_command}")
        handle_command(user_command.lower())

    except sr.UnknownValueError:
        print("I didn't catch that. Could you please repeat?")
    except sr.RequestError as e:
        print(f"Sorry, I encountered an error: {e}")
