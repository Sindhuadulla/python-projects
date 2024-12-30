
import pyttsx3
from PyDictionary import PyDictionary 

class Speaking:
 
    def speak(self, audio):
       
        # Having the initial constructor of pyttsx3 
        # and having the sapi5 in it as a parameter
        engine = pyttsx3.init('sapi5')
         
        # Calling the getter and setter of pyttsx3
        voices = engine.getProperty('voices')
         
        # Method for the speaking of the assistant
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()
    
class pyptoject:
    def Dictionary(self):
        speak = Speaking()
        dic = PyDictionary()
        speak.speak("Which word do u want to find the meaning madam")
         
        # Taking the string input
        query = str(input())
        word = dic.meaning(query)
       
        if word: 
            print(word)
            print(len(word))
            for state in word:
                print(word[state])
                speak.speak("the meaning  is" + str(word[state]))
        else:
            print("Sorry, no meanings found for the word.")
            speak.speak("Sorry, no meanings found for the word.")
 
 
if __name__ == '__main__':
    pyptoject()
    pyptoject.Dictionary(self=None)

from nltk.corpus import wordnet

class PyProject:
    def Dictionary(self):
        speak = Speaking()
        speak.speak("Which word do you want to find the meaning of, sir?")
        
        # Taking input from the user
        query = str(input())
        synsets = wordnet.synsets(query)
        
        if synsets:
            print("Found meanings:")
            for syn in synsets:
                print(syn.name(), syn.definition())
                speak.speak("The meaning of " + query + " is " + syn.definition())
        else:
            print("Sorry, no meanings found for the word.")
            speak.speak("Sorry, no meanings found for the word.")
