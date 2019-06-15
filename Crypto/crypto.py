# start the crypto program, and introduce the user to choose between two options    
    
def startCrypto():    
    
    userOption = "0"

    print (" \n Choose an option :  \n")
    
    print (" \n 1 - Crypting a message  \n")
    print (" 2 - Decrypt a message  \n")
    print (" 3 - Leave the crypto program  \n")
        
    userOption = input("\n Waiting for an option : ")
        
    checking = False


    while checking == False:
    
        try:
        
            userOption = int(userOption)
        
            while int(userOption) <= 0 or int(userOption) >= 4 :
    
                userOption = input("\n An option between 1 and 2 i'm sure you can do this, try again  : ")
            
                
                
            if userOption == 1:
                
                checking = True
                crypto()
                break
        
            if userOption == 2:
        
                checking = True
                uncrypt()
                break
                
            if userOption == 3:
                
                checking = True
                print("\n Goodbye human. \n ")
                break
            
        
        
        except ValueError:
            
            checking = False
        
            userOption = input("\n Fuck off ! I need a number idiot... : ")

            
# Ensure it's a human, because we never know after all...            
def checking():

    # set your password here !
    
    password = input("\n Prove you are a human : ")

    
    if password == "i'm a human":
        
        startCrypto()
        
    else :
    
        print("\n Goodbye stupid. \n ")                




# This function crypt a message, for real !

def crypto ():
    
    message = input (" \n Type in your message : ")
    
    result = " ERROR : "    
    
    
    message = message.lower()
    
    for lettre in message:
        
        lettre = str(lettre)
        
        
        if lettre == " ":
            
            result = result + " "
        
        if lettre == "a" or lettre == "à" :
            
            result = result + "(0)"
            
        if lettre == "b" :
            
            result = result + "(1)"    
            
        if lettre == "c" or lettre == "ç"  :
            
            result = result + "(10)"
            
        if lettre == "d" :
            
            result = result + "(11)"
            
        if lettre == "e" or lettre == "é" or lettre == "è" or lettre == "ê" :
            
            result = result + "(100)"
            
        if lettre == "f" :
            
            result = result + "(101)"
            
        if lettre == "g" :
            
            result = result + "(110)"
            
        if lettre == "h" :
            
            result = result + "(111)"
            
        if lettre == "i" :
            
            result = result + "(1000)"
            
        if lettre == "j" or lettre == "î" or lettre == "ï" :
            
            result = result + "(1001)"
        
        
        if lettre == "k" :
            
            result = result + "(1010)"
            
        if lettre == "l" : 
            
            result = result + "(1100)"
            
        if lettre == "m" :
            
            result = result + "(1101)"
            
        if lettre == "n" :
            
            result = result + "(1110)"
            
        if lettre == "o" or lettre == "ô":
            
            result = result + "(1111)"
            
        if lettre == "p" :
            
            result = result + "(10000)"
            
        if lettre == "q":
            
            result = result + "(10001)"
            
        if lettre == "r":
            
            result = result + "(10010)"
            
        if lettre == "s" :
            
            result = result + "(10100)"
            
        if lettre == "t" :
            
            result = result + "(11000)"
            
        if lettre == "u" or lettre == "ù":
            
            result = result + "(11001)"
            
        if lettre == "v" :
            
            result = result + "(11010)"
            
        if lettre == "w":
            
            result  = result + "(11100)"
            
        if lettre == "x":
            
            result = result + "(11101)"
            
        if lettre == "y":
            
            result = result + "(11110)"
            
        if lettre == "z":
            
            result = result + "(11111)"
    
            
        
    print("\n An error has occured : \n ")        
    print (result)
    startCrypto()
    


# This function decrypt the crypting, no joke.

def uncrypt():
    
    message = input ("\n Type in your code : ")
    
    chain = ""
    
    result = ""
    
    for lettre in message:
        
        if lettre == " ":
            
            result = result + " "
        
        
        if lettre == "(":
            
            chain = ""
            
        if lettre == "0":
            
            chain = chain + "0"
            
        if lettre == "1":
            
            chain = chain + "1"
            
        if lettre == ")":
            
            result = result + ""
            
            if chain == "0":
            
                result = result + "a"
                
            if chain == "1":
            
                result = result + "b"    
            
            if chain == "10":
                
                result = result + "c"
                
            if chain == "11":
                
                result = result + "d"
                
            if chain == "100":
                
                result = result + "e"
            
            if chain == "101":
                
                result = result + "f"
                
            if chain == "110":
                
                result = result + "g"
                
            if chain == "111":
                
                result = result + "h"
                
            if chain == "1000":
                
                result = result + "i" 
                
            if chain == "1001":
                
                result = result + "j"
                
            if chain == "1010":
                
                result = result + "k"
                
            if chain == "1100":
                
                result = result + "l"
                
            if chain == "1101":
                
                result = result + "m"
                
            if chain == "1110":
                
                result = result + "n"
                
            if chain == "1111":
                
                result = result + "o"
                
            if chain == "10000":
            
                result = result + "p"
                
            if chain == "10001":
                
                result = result + "q"
                
            if chain == "10010":
                
                result = result + "r"    
            
            if chain == "10100":
                
                result = result + "s"
                
            if chain == "11000":
                
                result = result + "t"    
      
            if chain == "11001":
                
                result = result + "u"
            
            if chain == "11010":
                
                result = result + "v"
                
            if chain == "11100":
                
                result = result + "w"    
            
            if chain == "11101":
                
                result = result + "X"
            
            if chain == "11110":
                
                result = result + "Y"
            
            if chain == "11111":
                
                result = result + "z"
                
           
            
            chain = ""

    print("\n Completed : \n ")        
            
    print(result)
    
    startCrypto()
    
    


