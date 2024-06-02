import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Processing...")
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))
            return ""

command = listen().lower()
