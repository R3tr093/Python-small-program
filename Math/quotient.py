print ("Quotient est un programme qui permet de réaliser la table de multiplication de deux facteurs variables.")


userNumber = input(" Pour commencer veuillez indiquer le nombre dont vous souhaitez connaitre la table de multiplication : ")




checking = False


    

    
while checking == False:
    
   
        
    try:
        
        int(userNumber)
        
        while int(userNumber) <= 0:
    
            userNumber = input(" Tu m'as pris pour un imbécile ?! : ")
            
            
            
        checking = True
        
        
    except ValueError:
            
        checking = False
        userNumber = input(" Un nombre, c'est pas compliqué... : ")
        


        
userRange = input(" Indiquer jusqu'ou nous devons multplier votre nombre : ")

checking = False        



while checking == False:
    
    
    
    try:
        int(userRange)
        
        while int(userRange) <= 0:
                
            userRange = input(" Tu m'as pris pour un imbécile ?! : ")
        
        checking = True
        
    except ValueError:
        
        checking = False
        userRange = input(" Genre tu sais pas écrire un nombre ? ")
        


userNumber = int(userNumber)        
userRange = int(userRange)

i = 0

while i <= userRange :
    print(str(i) + " x " + str(userNumber) + " = " + str(userNumber * i))
    i = i + 1
    

    
    