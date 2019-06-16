# This module generate a random integer 
from random import randint

userVal = 0

userWin = 0

userLoose = 0

userEquals = 0




def ShiFuMi ():



    
    

    # Define an array with computers options
    computers = ["Pierre", "Papier", "Ciseaux"];
    
    def report ():
        
        global userWin
        global userLoose
        global userEquals
        
        userGame = userWin + userLoose + userEquals
        
        

        print("\n ---------------------------------------------")
        print("\n Partie jouer : " + str(userGame))
        print("\n Partie Gagné : " + str(userWin))
        print("\n Partie Perdue : " + str(userLoose))
        print("\n Partie match nul  : " + str(userEquals))
        print("\n ---------------------------------------------")
    
    
    # Define a function for the menu
    
    def menu ():
        
        print("\n ---------------------------------------------")
        print("\n Veuillez choisir une des options suivantes en tapant le numéro correspondant : ")
        
        print("\n 1 - Jouer une manche ")
        print("\n 2 - Résumé des scores ")
        print("\n 3 - Quitter ")
        
        userVal = input ("\n Sélectionner une option : ")
        print("\n ---------------------------------------------")
        
        try :
            
            userVal = int(userVal)
            
            if userVal > 0 and userVal < 4:
                
                if userVal == 1:
                    
                    selectPhase()
                    
                if userVal == 2:
                    print(" \n Rapport des parties : ")
                    report()
                    menu()
                    
                if userVal == 3:
                    print(" \n Au revoir, merci d'avoir jouer.")
                
            else:
                
                print("\n Le numéro de l'option doit être compris entre 1 et 3.")
                menu()
                
        except ValueError:
            
            print(" \n Veuillez tapez un nombre entier.")
            menu()
    

    
    
    
    def selectPhase():
        
        print("\n 1 - Pierre ")
        print("\n 2 - Papier ")
        print("\n 3 - Ciseaux ")
            
        userVal = input("\n Tapez 1, 2, 3  pour jouer :  ")
        print("\n ---------------------------------------------")
    
                  
        try :
            
            userVal = int(userVal)
                
            if userVal > 0 and userVal < 4:
                
                userVal = int(userVal)
                battlePhase(userVal)
                
                    
                
            
            # The value is an integer, but is not in the interval
            else :
                    
                print("\n Le  nombre doit être compris entre 1 et 3. ")
                selectPhase()
                
        # The value receveid from user is not an integer.        
        except ValueError:
                
            print("\n Tapez un nombre entier compris entre 1 et 3. ")
            selectPhase()
            
            
    def battlePhase(userVal):
        
        global userWin
        global userLoose
        global userEquals
        
        
        
        cpuVal = randint(0,2)
        cpuReturn = computers[cpuVal]
        
        
        
        if userVal == 1 and cpuVal == 0:
            
            print("\n Vous avez choisis la Pierre.")
            print("\n L'ordinateur choisis la Pierre.")
            print("\n")
            print("\n")
            print("\n \n Match nul !")
            print("\n")
            print("\n")
            
            userEquals = userEquals + 1
            userGame = UserGame + 1
            menu()
            
        if userVal == 1  and  cpuVal == 1:
            
            print("\n Vous avez choisis la Pierre.")
            print("\n L'ordinateur choisis le Papier.")
            print("\n")
            print("\n")
            print("\n \n Le papier triomphe de la Pierre, vous avez perdu. !")
            print("\n")
            print("\n")
            userLoose = userLoose + 1
            
            menu()
            
        if userVal == 1  and  cpuVal == 2:
            
            print("\n Vous avez choisis la Pierre.")
            print("\n L'ordinateur choisis les Ciseaux.")
            print("\n")
            print("\n")
            print("\n \n La Pierre écrase les Ciseaux, vous avez gagné !")
            print("\n")
            print("\n")
            userWin = userWin + 1
            menu()
            
        if userVal == 2  and  cpuVal == 0:
            
            print("\n Vous avez choisis le Papier.")
            print("\n L'ordinateur choisis la Pierre.")
            print("\n")
            print("\n")
            print("\n \n Le Papier triomphe de la Pierre, vous avez gagné !")
            print("\n")
            print("\n")
            userWin = userWin + 1
            menu()
            
        if userVal == 2  and  cpuVal == 1:
            
            print("\n Vous avez choisis le Papier.")
            print("\n L'ordinateur choisis le Papier.")
            print("\n")
            print("\n")
            print("\n \n Match nul !")
            print("\n")
            print("\n")
            userEquals = userEquals + 1
            menu()
            
        if userVal == 2  and  cpuVal == 2:
            
            print("\n Vous avez choisis le Papier.")
            print("\n L'ordinateur choisis les Ciseaux.")
            print("\n")
            print("\n")
            print("\n Les Ciseaux découpent le Papier, vous avez perdu !")
            print("\n")
            print("\n")
            
            userLoose = userLoose + 1
            menu()
                
        if userVal == 3  and cpuVal == 0:
            
            print("\n Vous avez choisis les Ciseaux.")
            print("\n L'ordinateur choisis la Pierre.")
            print("\n")
            print("\n")
            print("\n \n La Pierre écrase les Ciseaux, vous avez perdu ! ")
            print("\n")
            print("\n")
            userLoose = userLoose + 1
            report()
            menu()
            
        if userVal == 3  and  cpuVal == 1:
            
            print("\n Vous avez choisis les Ciseaux.")
            print("\n L'ordinateur choisis le Papier.")
            print("\n")
            print("\n")
            print("\n \n Les Ciseaux découpent le Papier, vous avez gagné !")
            print("\n")
            print("\n")
            userWin = userWin + 1
            menu()
            
        if userVal == 3  and  cpuVal == 2:
            
            print("\n Vous avez choisis les Ciseaux.")
            print("\n L'ordinateur choisis les Ciseaux.")
            print("\n")
            print("\n")
            print("\n \n Match nul !")
            print("\n")
            print("\n")
            userEquals = userEquals + 1
            menu()
            
                
                
            

            
    
    
    
    
    # Call this function for launch the game.
    menu()
    
    
ShiFuMi()    

    