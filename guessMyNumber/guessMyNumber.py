# PART 1 -- > Some Modules import.

import sys
import os
import random

# PART 2 -- >  Placeholder variables.

tips = [[0,"none"],[0,"none"],[0,"none"]]

attempts = 0
goal = random.randint(1,99)
score = 0


# PART 3 -- >  Define functions to formating text

newLine = "\n"

def newLinePrint(param):
    print(newLine + param)

def clear():

    if os.name == "nt":
        os.system('cls')   
    
    else:        
        os.system('clear')
    

def scriptBreaker():
    print(newLine)
    input("Type in Enter to continue...")
    print(newLine)
    clear()    

def frame (param):
    
    print(newLine)
    print('|------------------------------------------------------------|' + newLine)
    print('|                                                            |' + newLine)
    print('|                  ' + param.center(24) + '                  |' + newLine)
    print('|                                                            |' + newLine) 
    print('|------------------------------------------------------------|' + newLine)
    scriptBreaker()


# PART 4 -->  Functions that allow the operation of the program


# We use this function to determine and display if the random number can be divided by an integer from 2 to 9 selected by user
# We set the value of tips array in this case, we keep the value of the tips submitted, and provide boolean, the both in the same array

def reset():
    tips = [[0,"none"],[0,"none"],[0,"none"]]
    attempts = 0
    goal = random.randint(1,99)


def resolveTips():
    
    global goal

    check = False

    count = 0

    for element in tips:

        if element[0] != 0:
            count+=1

    newLinePrint("You already used, " + str(count) + " tips.")

    newLinePrint(str( 3 - count) + " tips left.")

    newLinePrint(" >>> Type in X if you want to go back to the menu. ")

    if count - 3 != 0:

        while check == False:

            try:
                request = input(newLine + "Which number do you want to use as tips ? : >>> " )

                if isinstance(request, str):
                    
                    if len(request) >= 0:

                        if request[0].upper() == "X":
                            check = True
                            getMenu()
                            break

                request = int(request)
                
                while int(request) <= 1 or int(request) > 9:
                    print(newLine)
                    request = input("Value Error :: You must provide an integer number. This number should be from 2 to 9 or Type X for leave. >>> ")
                    request = int(request)
                
                check = True
                clear()

                if goal % request == 0:
                    newLinePrint(str(request) + " is divisible by the number you looking for.")
                    tips[count - 1][1] = True
                
                else:
                    newLinePrint(str(request) + " is not divisible by the number you looking for.")   
                    tips[count - 1][1] = False

                tips[count - 1].pop(0)
                tips[count - 1].insert(0,request)
                newLinePrint("")
                input("Press Enter to continue...")
                getMenu()


            except ValueError:
                newLinePrint("Value Error :: You must provide an integer number. This number should be from 2 to 9 or Type X for leave.") 


    else:
        newLinePrint("")
        newLinePrint("Sorry, No tips available.")
        newLinePrint("")
        input("Press Enter to continue...")
        clear()
        getMenu()

# We use this function to display informations about tips used.

def logTips():

    count = 0

    for element in tips:

        if element[0] != 0:

            count+=1

    newLinePrint("You already used, " + str(count) + " tips.")

    for element in tips:
        
        if element[0] != 0 and element[1] == True:

            newLinePrint("The number you looking for is divisible by : " + str(element[0]) + ".")

        if element[0] != 0 and element[1] == False:
            newLinePrint("The number you looking for is not divisible by : " + str(element[0]) + ".")

    newLinePrint(" ")
    input("Press Enter to continue...")
    clear()
    getMenu()




# This function take as parameter the result of getMenu(), with this required integer parameter we're able to know what the user want to do, and doing it.

def resolveOption(option: int):
    
    if option == 1:
        resolveAttempt()


    if option == 2:
        resolveTips()

    if option == 3:
        logTips()

    if option == 4:
        newLinePrint("The rules are pretty simple, the computer think about a random number from 0 to 99.")
        newLinePrint("You have to find which number it is, for help you to perform this goal you can asking for tips.")
        newLinePrint("You get three tips for the current number you have to find. \nWhen you use tips the computer should told you if the number you choosed can divide the number you're trying to guess.")
        newLinePrint("You can attempt three time to find the number, proposing the number you think computer has in his mind, \nand then the computer should told you if the number you purpose is higher or less than is number.")
        newLinePrint("If you find the number you win the game, and you can try again until you loose, the count of numbers you find define your end score.")
        newLinePrint("If you used all your attempts, and you did not find the number you lost, the game ends and you get your final score.")
        newLinePrint(" ")
        input("\n Type in Enter to continue...")
        getMenu()

    if option == 5:
        reset()
        global score
        score = 0
        getMenu()
        newLinePrint("Successfully reset.")

    if option == 6:

        newLinePrint("Goodbye.")
        sys.exit(0)


# This function resolve an attemp to find the number.

def resolveAttempt():

    global attempts
    global goal

    attempts+=1

    check = False

    if attempts < 4:

        newLinePrint(" >>> Type in X if you want to go back to the menu. ")

        while check == False:
        
            try:
            
                response = input(newLine + "Select the number you think the computer think about " + newLine + newLine + " >>> ")


                # Exit from the function.
                if isinstance(response, str):
                    
                    if len(response) >= 0:

                        if response[0].upper() == "X":
                            check = True
                            getMenu()
                            break

                response = int(response)

                while response > 99 or response < 1:
                        
                    response = input(newLine + "Please, can you just select an number from 1 to 99 or Type X ? " + newLine + newLine + " >>> ")  
                    response = int(response)

                if response < goal:
                    newLinePrint("Your number is inferior from mine.")
                    scriptBreaker()
                    getMenu()

                if response > goal:
                    newLinePrint("Your number is superior from mine.")
                    scriptBreaker()
                    getMenu()

                if response == goal:
                    newLinePrint("Well played, you win this one.")

                    if attempts == 0:
                        score+=3000
                    
                    if attempts == 1:
                        score+=2000

                    if attempts == 2:
                        score+=1000    

                    newLinePrint("Your score increased game, a new number is available to guess, your tips and attempts has been reset.")    
                   

                check = True
        
            except ValueError:

                newLinePrint("Please, can you just select an number from 1 to 99 ?")

             

    else:
        newLinePrint("Sorry, you already used all your attempts, and you fail. Goodbye.")

# This function called after the introduction, allow to the user to choose an option to use the program. The most important thing is to get an integer between 0 > 5.
# We have to return this parameter and provide it to the call of function named resolveOption(parameter) 

def getMenu():


    global attempts

    
    if attempts > 2:
        newLinePrint("I think you just loose this one, well nice try. Goodbye.")
        input(newLine + " >>> You just have to press Enter to be kicked out.")
        newLinePrint("Ps : the number you looking for was " + str(goal))
        sys.exit(0)
    
    userOption = 0

    clear()

    newLinePrint("------------------------------------------------")

    newLinePrint("|     Please, select an option by number       |")
    print("|     __________________________________       |")
    newLinePrint("|  1- Make an attempt.                         |")
    newLinePrint("|  2- Use tips.                                |")
    newLinePrint("|  3- Show tips already used.                  |")
    newLinePrint("|  4- Show rules.                              |")
    newLinePrint("|  5- New game.                                |")
    newLinePrint("|  6- Leave the program.                       |")
    newLinePrint("------------------------------------------------")
    newLinePrint(newLine + "Score >>> " + str(score))


    newLinePrint(" ")
        
    userOption = input("Select an option by type in an number >>> ")


    check = False

    while check == False:


        try:

            userOption = int(userOption)

            while int(userOption) <= 0 or int(userOption) >= 6:
                print(newLine)
                userOption = input("Value Error :: Please, select an option by type in a number >>> ")
                
            check = True
            clear()
            resolveOption(userOption)   

        except ValueError:

            check = False
            print(newLine)
            userOption = input("Value Error :: Please, select an option by type in a number >>> ")






# PART 5 --> Simply, Introduction and beginning of program.

frame(" Guess My Number ")

newLinePrint("Hello, this program is named guessMyNumber because it's a simple stuff where you try to guess which number computer thinking about.")
input( newLine + "Type in Enter to continue.")
newLinePrint("For each number you trying to guess, you can ask if he is divisible by three different value from 0 to 9.")
newLinePrint("Well it's time to play !")
input( newLine + "Type in Enter to continue.")

getMenu()

