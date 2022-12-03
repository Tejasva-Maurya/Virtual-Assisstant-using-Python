#pip install speech_recognition
import speech_recognition as sr
#!pip install pyttsx3
import pyttsx3
import datetime
#!pip install wikipedia
import wikipedia
import webbrowser
import os

from wikipedia.wikipedia import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


MASTER = 'TEJAS'

# speak the text   
def speak(text):
    engine.say(text)
    engine.runAndWait()

# wish your master according to time 
def wishME():
    hour = int(datetime.datetime.now().hour)
    
    if 5 <= hour < 12 :
        speak('Good Morning ')
    elif 12 <= hour <= 17 :
        speak('Good Afternoon ')
    elif 17 < hour < 22 :
        speak('Good Evening ')
    else :
        speak('Good Night ')
    

# take voice command from microphone 
def takeCommand ():
    r = sr.Recognizer()
    with sr.Microphone(0) as source :
        print(' Listening... ')
        audio = r.listen(source,None,5) # taking and listening audio

    try : # recognizing the command
        print(' Recognizing... ') 
        query = r.recognize_google(audio, language = 'en-in')
        print(f'user said: {query} \n')
        return query

    except Exception as e : # error handling
        print('Please say it again')
        return ' '
      


# main program starts here 

print('Initializing AI ........')
speak('Initializing AI ........' )
speak('Hello , '+ MASTER)
wishME()


start = takeCommand()

speak('I am AI, How can I help you ? ')
 
while 'exit' not in start : # loop for contineous running of AI
    
    query = start

    # Logic for executing task as per the query
    # search anythything in wikipedia  
    if 'wikipedia' in query.lower() :
        speak(' Searching in wikipedia... ')
        query = query.replace('wikipedia' , '')
        results = wikipedia.summary(query, sentences = 2)
        speak(results)
        print(results)
        start = takeCommand()




    # open yourtube on google chrome 
    elif ('open yourtube' and 'chrome') in query.lower() :
        speak('Opening Youtube on Chrome...')
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        url = 'www.youtube.com'
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)
        start = takeCommand()


    # to open yourtube
    elif 'open youtube' in query.lower():
        speak('opening Youtube...')
        webbrowser.open('https://www.youtube.com/') 
        start = takeCommand()

    # search on yourtube
    elif ('search' and 'on youtube') in query.lower() :
        speak('searching on Youtube ...')
        query = query.replace('search','')
        url = (f'https://www.youtube.com/results?search_query={query}')
        webbrowser.open(url)
        start = takeCommand()

    # for opening browser 
    elif 'open browser' in query.lower():
        speak('opening browser...')
        webbrowser.open('https://www.google.co.in/')
        start = takeCommand()

    #open google
    elif 'open google' in query.lower():
        speak('opening google...')
        webbrowser.open ('https://www.google.co.in/')
        start = takeCommand()

    # to search on browser 
    elif 'search' in query.lower() :
        speak('searching....')
        query = query.replace('search','')
        url = ('https://www.google.co.in/search?q=' + query)
        webbrowser.open(url)
        start = takeCommand()

    # to play music
    elif ('play' and 'music') in query.lower() :
        
        songs_dir = 'C:\\Users\\Tejas\\Music'
        songs =os.listdir(songs_dir)
        length = len(songs)
       

        for i in range(1,length): # to print the list of songs available
            print(f'{i} :- {songs[i]} ')
        speak('From the above list which song do you want to play.')

        option = takeCommand() # To select the songs from the list

        for i in range(1,length): # to play musics
            if option.lower() in songs[i].lower() :
                os.startfile(os.path.join(songs_dir,songs[i]))
        speak('Playing Music ....')
        start = takeCommand()
    
    elif ('play' and 'movies') in query.lower() :
        
        movies_dir = 'D:\movies'
        movies =os.listdir(movies_dir)
        length = len(movies)
       

        for i in range(1,length): # to print the list of songs available
            print(f'{i} :- {movies[i]} ')
        speak('From the above list which movie do you want to watch.')

        option = takeCommand() # To select the movies from the list

        for i in range(1,length): # to play movies
            if option.lower() in movies[i].lower() :
                os.startfile(os.path.join(movies_dir,movies[i]))
        speak('Playing movie ....')
        start = takeCommand()
    
    # to open whatsapp:
    elif 'whatsapp' in query.lower() :
        webbrowser.open ('https://web.whatsapp.com/')
        speak('opening whatsapp .....')
        start = takeCommand()
    
    # time 
    elif 'time' in query.lower() :
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'The time is {strTime}')
        start = takeCommand()


    elif ' ' in query.lower():
        start = takeCommand()
    else :
        # speak ('please Try again !! ')
        start = takeCommand()
speak('Thanks For Using Me ...')
print('Thanks For Using Me')
speak('Closing AI....')
print('Closing AI ....')
