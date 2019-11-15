import os
import random


newLine = "\n"
animals = ["Dog", "Kitten","Hawk","Worm","Horse","Pig"]
stuff = ["Anxious",'Angry','Sad','Weird','Happy']

def newLinePrint(param):
    print(newLine + param)

def clear():

    if os.name == "nt":
        os.system('cls')   
    
    else:        
        os.system('clear')


def frame (param):
    
    print(newLine)
    print('|------------------------------------------------------------|' + newLine)
    print('|                                                            |' + newLine)
    print('|                  ' + param.center(24) + '                  |' + newLine)
    print('|                                                            |' + newLine) 
    print('|------------------------------------------------------------|' + newLine)
    print(newLine)
    input("\n Appuyez sur Enter pour continuer...")
    clear() 

def getName():
    getRandomAnimals = random.randint(0,len(animals) -1)
    getRandomStuff = random.randint(0,len(stuff) -1)
    print( newLine + " >>> " + stuff[getRandomStuff] + animals[getRandomAnimals] + str(random.randint(0,999)))
    response = input("Want another one ? : (Yes / No)" + newLine)
    if response[0].upper() == "Y":
        clear()
        getName()

    else:
        print('Goodbye.')


frame("Random Pseudo Generator.")

getName()


