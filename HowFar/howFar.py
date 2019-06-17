# How far can you go ( Howfar) is a program where you should fine the solution for continue 




# BREAKPOINT :: Here type all the levels




def lvl1 ():
    
    userOption = input("\n Where do we start ? : ")
    
    
    while userOption != "0":
        userOtion = input("\n Were do we start ? :")
        
    print("\n Level complete ! ")
    print("\n Your rank is  : Not stupid.")    
    

















# BREAKPOINT :: Beginning of the program 

# Step 1 : A broken captcha !


checking = input ("\n Prove your a human : ")

while checking != "I'm a human":
    
    checking = input("\n Prove your a human ")
    
    
# Need to know which level is accepted


print("\n Initializing ... ")
print("\n Waiting for a response. ")



print ("\n 1 - Start ")
print ("\n 2 - Leave ")


def getLvl ():
    
    userOption = input("\n Waiting user response :  ")
    try:
        
        userOption = int(userOption)
        
        if userOption > 0 and userOption < 4:
            
            
            if userOption == 1:
                
                print("\n Stage 1 : ")
                lvl1()
                
            if userOption == 2:
                print("\n GoodBye Human.")
                
            if userOption == 3:
                
                
                
                # BREAKPOINT :: Here we can submit a password to access a specidied level .
                userOption = input (" \n FATAL ERROR : user try to skip lvl : " )
            
        else :
            
            print("\n ERROR : This value is not in the interval .")
            getLvl()
            
            

        
    except ValueError:
        
        print("\n Value Error data should be an integer")
        getLvl()

# Calling this function for launch the program :
getLvl()



    


