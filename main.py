# Our Main File

import speech_recognition as sr

# Create the recognizer
r = sr.Recognizer()

# Open the audio device
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        print(r.recognize_google(audio, language='pt'))