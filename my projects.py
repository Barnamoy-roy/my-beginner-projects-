
#rock paper scissors game
#simple use of if statements and user inputs

import random as rd
import pyttsx3                             #importing random module and text to speech module pyttsx3;
engine = pyttsx3.init()                    #initalizing it and assigning it to a variable
engine.setProperty("rate", 120)            #setting the speed of the speaker 120 is wpm

computer_in = ["r", 'p', 's']
computer = rd.choice(computer_in)          #using random module to give the computer input

user = input("please enter your input \nr for rock, p for paper and s for scissors: ")
if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):   #setting the conditions for the player to win
    engine.say("uh oh damn i lost and you won!!")                  #the computer say this if the player wins
    engine.runAndWait()                                            #this command is important to say the above phrase from txt to speech
else:
    engine.say("ha ha ha i won again u loser!!")                   #if the player loses then this phrase is spoken and the same run and wait fucntion
    engine.runAndWait()