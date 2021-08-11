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
import core
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


# Reconhecimento de Fala

while True:
    data = stream.read(4000 ,exception_on_overflow = False)
    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result['text'] is not None:
            text = result['text']

            print(text)

            if text == 'que horas são' or text == 'que ora é':
                speak(core.SystemInfo.get_time())
                text = ''

            elif text == 'que dia é hoje' or text == 'hoje é que dia' or text == 'qual a data de hoje':
                speak(core.SystemInfo.get_day())
                text = ''
