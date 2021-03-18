import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mike' in command:
                command = command.replace('mike', '')
                print(command)
    except:
        pass
    return command

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  

    talk("Hello , my name is Krishna. Please tell me how may I help you")
    
    

def callruchi():
    talk("Ruchi , Ruchi , Ruchi , Papa , is waiting for you , Come fast")
def parik():
    talk("Parikshit,  padhne baitho , Jaldi baitho ,  aur , agar homework ,  baki hai ,  to wo bhi, karo")
def mumlove():
    talk("Mummy , Chinta ,  mat kije ,hmlog , sabkoi appse , bahut , pyar karte , hai ")
def papa():
    talk("Papa ,Come fast home , we all are waiting for you")
def run_mike():
    command = take_command()
    print(command)
   
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you ok' in command:
        talk('sorry, I have a headache')
    elif 'you are good' in command:
        talk('Thanks, thats my pleasure')
    elif 'you are shit' in command:
        talk('sorry, what crime did I make') 
    elif 'are you busy' in command:
        talk('No , what happen,tell me, I will try to help you')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open code' in command:
        codePath = "C:\\Users\\VIJAY SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'open chrome' in command:
        codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(codePath)
        
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
    elif 'amway' in command:
        webbrowser.open("amway.in")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'i have an issue' in command:
        webbrowser.open("stackoverflow.com")
    elif 'my class' in command:
        webbrowser.open("code.whitehatjr.com")
    elif 'upload code' in command:
        webbrowser.open("github.com")
    elif 'hi krishna' in command:
        wishMe()
    elif 'call ruchi' in command:
        callruchi()
    elif 'not studying' in command:
        parik()
    elif 'late' in command:
        papa()
    elif 'angry' in command:
        mumlove()
    elif 'going for sleep' in command:
        talk("Ok , Good Night , that was a pleasure being with you today")
    elif 'cortana' in command:
        talk("Nothing ,but a less abled ,shitty freind")
    else:
        talk('Please say the command again.')        


while True:
    run_mike()
