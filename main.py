import speech_recognition as sr
import webbrowser
import pyttsx3

recongnizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":

    speak("Initializing Jarvis...")

    while True:
        # Create a recognizer
        r = sr.Recognizer()

        # Use microphone as source
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)   # Capture voice input

        # Try to recognize speech using Sphinx (offline recognition)
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))