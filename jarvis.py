import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)     


def wishMe():
     hour = int(datetime.datetime.now().hour) 
     if hour>=0 and hour<12:
          speak("Good Morning!") 

     elif hour>=0 and hour<18:
          speak("Good Afternoon!")

     else:
          speak('Good Evening!')

     speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 1
          audio = r.listen(source)

     try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n" )
     except Exception as e:

          #print(e)
          print("Please say that again...")
          return "none"
          return query
def speak(audio):
     engine.say(audio)
     engine.runAndWait()

if __name__ == "__main__":  
    wishMe()
    takeCommand()