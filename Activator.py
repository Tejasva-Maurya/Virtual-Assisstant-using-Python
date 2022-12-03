import os
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def takeCommand ():
    r = sr.Recognizer()
    with sr.Microphone(0) as source :
        audio = r.listen(source,None,5) # taking and listening audio

    try : # recognizing the command
        query = r.recognize_google(audio, language = 'en-in')
        return query

    except Exception as e : # error handling
        print('Please say it again')
        return ' '


# speak the text   
def speak(text):
    engine.say(text)
    engine.runAndWait()

query = takeCommand()

while 'activate' not in query.lower():
    query = takeCommand()

if ('activate') in query.lower() :
        
    folder_dir = 'main.py'
    os.startfile(os.path.join(folder_dir))
    speak('activating AI.....')
