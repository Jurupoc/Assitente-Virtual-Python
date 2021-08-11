# Our Main File

'''

import speech_recognition as sr

# Create the recognizer
r = sr.Recognizer()

# Open the audio device
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        print(r.recognize_google(audio, language='pt'))

'''
from vosk import Model, KaldiRecognizer
import os
import pyaudio

import json

import pyttsx3
engine = pyttsx3.init()


def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-2].id)

    engine.say(text)
    engine.runAndWait()


model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000 ,exception_on_overflow = False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = rec.Result()
        res = json.loads(res)

        if res['text'] is not None:
            text = res['text']

            print(text)
            speak(text)
