import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import os
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

r = sr.Recognizer()
translator = Translator()

while True:
    with sr.Microphone() as source:
        print("Speak Now!!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print('END')
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text == "exit":
                break
            
            translation = translator.translate(speech_text, dest='en')
            print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

            # Convert translated text to speech
            engine.say(translation.text)
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print("Could not request result from Google")
