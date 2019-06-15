# ! ! -> BREAK : Présentation du programme


print ("\n FizzBuzz est un programme qui vérifie si une suite de nombre est divisible par deux chiffres données.")

print ("\n Si le nombre en cours de traitement est divsible par X, on affiche Fizz.")

print ("\n Si le nombre en cours de traitement est divsible par Y, on affiche Buzz.")


# !! -> BREAK : On effectue la récupération des données nécessaire au déroulement du programme


def fizzbuzz():

# Ce booléen va nous permettre de déterminer si on n'as bien reçu les données nécessaires au programme.

    checking = False


# On attend le nombre X  
    userX = input(" \n  Pour commencer veuillez indiquer le premier diviseur : ")    


# S le nombre X n'est pas compatible on renvoie une nouvelle demande jusqu'a obtenir un nombre compatible

    while checking == False:
    
   
        
        try:
        
        # On essaye de convertir la valeur reçue sous forme d'un nombre entier.
            int(userX)
        
        
        # On vérifie que le nombre n'est pas inférieur à 0.
            while int(userX) <= 0:
    
                userX = input("\n Tu m'as pris pour un imbécile ?! : ")
            
            
        # Le nombre est compatible on passe au nombre suivant
            checking = True
        
    # Si le nombre n'est pas compatible on renvoie une demande     
        except ValueError:
            
            checking = False
            userX = input(" \n  Un nombre, c'est pas compliqué... : ")
        


        
    userY = input(" \n  Veuillez indiquer le second diviseur : ")


# On effectue une nouvelle vérification, le booleen doit passez à false
    checking = False        


# On pose une boucle qui nous assure la compatibilité du second diviseur
    while checking == False:
    
    
    
        try:
            int(userY)
        
            while int(userY) <= 0:
                
                userY = input(" \n Tu m'as pris pour un imbécile ?! : ")
        
            checking = True
        
        except ValueError:
        
            checking = False
            userY = input(" \n Genre tu sais pas écrire un nombre ? ")
        



    userRange = input(" \n Veuillez indiquer jusqu'à quelle nombre nous devons effectuer la division : ")

    checking = False

# On pose une boucle qui nous assure la compatibilité du nombre max
    while checking == False:
    
        try:
            int(userRange)
        
            while int(userRange) <= 0:
                
                userRange = input(" \n Tu m'as pris pour un imbécile ?! : ")
        
            checking = True
        
        except ValueError:
        
            checking = False
            userRange = input("\n Genre tu sais pas écrire un nombre ? : ")

# !! BREAK -> On va effectuer le fizzbuzz    

# Mesure de précaution on refait un cast
    userX = int(userX)        
    userY = int(userY) 
    userRange = int(userRange)

    listX = [] 
    listY = [] 
    listXY = [] 

    i = 1;
    
    while i < userRange:
        
        if i % userX == 0 and i % userY == 0:
            print("\n FizzBuzz !  " )
            print("-------------------")
            print(str(i) + " est divsible par " + str(userX) + " et par " + str(userY) + "\n")
            listXY.append(i)
            listX.append(i)
            listY.append(i)
            
        else:
            
            if i % userX == 0:
                print("\n Fizz ! ")
                print("------------")
                print(str(i) + " est divsible par " + str(userX) + "\n" )
                listX.append(i)
                
            if i % userY == 0:
                print("\n Buzz ! ")
                print("------------")
                print(str(i) + " est divsible par " + str(userX) + "\n" )
                listY.append(i)
            
        i = i + 1

        
    # !! BREAK -> On fais un rapport    
        
    print("\n Il y a " + str(len(listXY)) + " Nombre divisible par " + str(userX) + " et par " + str(userY) + ".")    
        
    for x in listXY:
        print("\n -- " + str(x))
        
    print("\n Il y a " + str(len(listX)) + " Nombre divisible par " + str(userX) + ".")    
        
    for x in listX:
        print("\n -- " + str(x))
        
    print("\n Il y a " + str(len(listY)) + " Nombre divisible par " + str(userY) + ".")    
        
    for x in listY:
        print("\n -- " + str(x))      
## END ##
