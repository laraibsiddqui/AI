import speech_recognition as sr
#python text to speech version 3
import pyttsx3
#this is the package which allows you to search anything from youtube
import pywhatkit
#this package is for asking time and date to alexa
import datetime
#this package is for searching from wikipedia
import wikipedia
# this package is for asking jokes
import pyjokes
# for whether details
import weathercom

import json

#by the help of listener alexa recognize my sppech
listener= sr.Recognizer()
# i create an engine that is speak to me
engine= pyttsx3.init()
# alexa female voice
#by getproperty(voices) you can get all the voices alexa have
voices=engine.getProperty("voices")
#now  i choose index[1] from the list which is female voice and set it
engine.setProperty('voice',voices[1].id)

#dfs
def dfs(graph, start):
    stack, path=[start],[]
    while stack:
        vertex=stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for element in graph[vertex]:
            stack.append(element)
    return path
matrix={
    'KARACHI':['ISLAMABAD', 'MUREE'],
    'ISLAMABAD':['GILGIT', 'LAHORE'],
    'LAHORE':['GILGIT'],
    'MUREE':['LAHORE', 'HUNZA'],
    'GILGIT':['KARACHI'],
    'HUNZA':['LAHORE'],
    'KASHMIR':['MUREE', 'HUNZA', 'KAGHAN'],
    'KAGHAN':['LAHORE']
}




# this is the function of talk and text is the parameter which i will passing
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
# i use try for if i use microphone my function pass it
    try:

       with sr.Microphone() as source:
        print("listening....")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command = command.lower()
        # if alexa word is present in command it will print it otherwise it will not print command
        if "evren" in command:
            # this command ask to say something
            #engine.say(command)
            #remove alexa from command and say whatever you want to play
             command=command.replace("evren","")
            #whatever i talk alexa will print it
             print(command)
    except:
        pass
    return command

    # by run fuction, i can easily run alexa according to my commands

def run_alexa():
        #take command from user
        command=take_command()
        print(command)
        #by taking command i do some process by using it
        # if i want to play songs
        if 'play' in command:
            song = command.replace("play","")
            #it play the song
            talk("playing "+song)
            #by the help of it u can search song on youtube
            pywhatkit.playonyt(song)
            # ask time to alexa
        elif "time" in command:
            #datetime.now is for current time and ,strftime is for string format of time
            time=datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('current time is '+ time)
        elif "who the heck is" in command:
            #this will remove "who the heck is" from our command
            person=command.replace("who the heck is","")
            #this statement will give only 1 line summmary from wikipeadia
            info=wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif "date" in command:
            talk("sorry, i have a headache")
        elif "joke" in command:
            j=pyjokes.get_joke()
            talk(j)
            print(j)
        elif "name" in command:
            talk("My name is evren")
        elif "shortest route " in command:
          route="KARACHI"
          talk(dfs(matrix,route))
          print(dfs(matrix, route))
        
       
run_alexa()

