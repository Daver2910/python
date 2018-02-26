# Developer :   David Redmond
# Date :        08/02/2018
# Program name: Varvara's Adventure

import random
import time

name = ""
path = ""

def displayMain():
    print ("Welcome to the morning Adventure")
    time.sleep(2)
    print ("the best text-based computer game since 1985")
    time.sleep(2)
        
def nameCollect():
    global name
    name = raw_input('What is your name?\n'+ str(name))
    return name
        
def welcome():
    print ('Hello ' + name + ', Let play a little game.')
    time.sleep(2)
    print ("It's the morning, you wake up, you are alone in the apartment, David is in work.")
    time.sleep(2)
    print ('As you make the coffee, you notice that you feel hungry')
    time.sleep(2)
    print ('Do you search the kitchen for food? or Have shoot a complete stranger?')
    time.sleep(3)

def choiceStr2():
    global path
    while path != 'food' and path != 'shoot':      # input validation, to make sure only 2 options are available.
        path = raw_input("Which option do you choose? (food or shooting): "+ str(path))
    return path

def optionDecision(choiceStr2):
    if path == 'shooting':
        print ('Good answer, you are are not so brave!!')
        time.sleep(3)
        print ('as you search for food the kettle boils and you make coffee')
        time.sleep(3)
        print ('Just then there is a know on the door, You go to the door and see its the Turkish neighbour')
        
    else:
        print ('you walk outside and look for the first man you see to shoot him!!')
        time.sleep(3)
        print ('The first man you see is the old guy next door.... you try to shoot him!')
        time.sleep(3)
        print ('he kicks your butt')

displayMain()
nameCollect()
welcome()
choiceStr2()
optionDecision(choiceStr2)



input('Press ENTER to exit ')

      
