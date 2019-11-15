import os




messages  = []

count = 0

def clear():

    if os.name == "nt":
        os.system('cls')   
    
    else:        
        os.system('clear')



def load():

    again = False

    global count

    while again is not True:
        
        addStuff = input("\n Type in some messages to display. Then type stop when it's enough. \n \n >>> ")

        if addStuff.upper() == "STOP":
            again = True
            clear()
            myOwnPrint(messages)

        else:

            messages.append(addStuff)
            count+=1



def myOwnPrint(*values, sep=" ", end="\n"):

    values = list(values)

    chain = ""

    for i, value in enumerate(values):
        
        values[i] = str(value)

        chain = chain + values[i] + sep
        
    chain = chain.replace('[', "\n ")
    chain = chain.replace(',','\n\n >>> End. \n\n') 
    chain = chain.replace(']', '\n \n >>> End.')
    chain += end

    print("\n You have " + str(count) + " messages.")
    
    print(chain, end="")



load()