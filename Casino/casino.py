import random


# global variables 

wallet = 0

game = 0

gameWin = 0

gameLoss = 0

bigPrice = 0


# Take as parameter a boolean, if he is false we skip introduction, if is true we display all the menu with the introduction.

def menu(full):
   
    check = False
   

    if full:
        print("\n Nous allons jouer au jeu de la roulette, sélectionner une option et entrez le numéro correspondant. \n")
    
    print("\n  ------------------------------------------------------------------------ \n")
    print("\n 1 - Régles du jeu. \n ")
    print("\n 2 - Consulter votre portefeuille et l'historique de vos parties. \n")
    print('\n 3 -  Proposer votre mise. \n')
    print('\n 4 - Quitter le casino.')
    print("\n  ------------------------------------------------------------------------ \n")
    

    global wallet
    global game
    global gameWin
    global gameLoss
    global bigPrice

    while check == False:

        userOption = input("\n Veuillez choisir une option... \n")

        try:

            userOption = int(userOption)

            if userOption > 4 or userOption < 1:
            
                print('\n Veuillez choisir un nombre compris entre  1 et 4.\n ')




            else:

                check = True

                if wallet < 100:

                    print('\n Désolé vous n\'avez plus d\'argent, mais la vie continue en dehors du casino !')

                elif userOption == 1:
                    
                    print('\n Placez une mise sur un numéro compris entre 0 et 49, les chiffres pairs sont de couleur noires, les chiffres impairs sont de couleur rouges. \n')
                    print('\n La roulette va tourner et atteindre un numéro aléatoire, si ce numéro est le votre vous récupérez trois fois votre mise !')
                    print('\n Si votre numéro est de même couleur que celui sélectionner par la roulette vous récupérez votre mise. ')
                    print('\n Si votre numéro n\'est pas de la même couleur, et n\'est pas égale à celui de la roulette vous perdez votre mise. \n')
                    input("Appuyez sur une touche pour continuer...")

                    menu(False)

                elif userOption == 2:
                    print('\n >>> Votre porte monnaie actuel est de : ' + str(wallet) + "$")

                    print('\n >>> Vous avez misez ' + str(game) + " fois.")
                    print('\n >>> Vous avez tripler votre mise ' + str(bigPrice) + " fois.")
                    print('\n >>> Vous avez récupérez votre mise ' + str(gameWin) + " fois.")
                    print('\n >>> Vous avez perdu votre mise ' + str(gameLoss) + " fois.")

                    if bigPrice > 0:
                        bigPricePercent = bigPrice * 10 / game * 10
                        print('\n Vous remportez de l¼argent dans ' + str(bigPricePercent) + "% des parties jouées.")

                    if gameWin > 0:
                        
                        winPercent = gameWin * 10 / game * 10

                        print('\n Vous récupérez votre mise dans ' + str(winPercent) + '% des parties jouées.')

                    if gameLoss > 0:

                        lossPercent = gameLoss * 10 / game * 10

                        print('\n Vous perdez votre mise dans ' + str(lossPercent) + "% des parties jouées.")

                    if wallet > 5000:
                        print('\n Vous avez gagnez ' + str(wallet - 5000) + "$ de plus que votre somme de départ !")

                    if wallet < 5000:
                        print('\n Vous avez perdu ' + str(5000 - wallet ) + "$ par rapport à votre somme de départ...")


                    menu(False)

                elif userOption == 3:
                    getBet()
                        

                elif userOption == 4:
                    print('Aurevoir, merci de votre visite.')   
            

        except ValueError:
            print(" \n Cette option n'est pas valable, sélectionnez un chiffre compris entre 1 et 4.")     



# Provide a bet 

def getBet():

    check = False

    global wallet

    while check == False:

        print('\n >>> Porte-monnaie : ' + str(wallet) + "\n")

        userOption = input('\n Placez une mise minimum de 100$ : ')

        try:

            userOption = int(userOption)

            if userOption <= 100:
                print('\n Votre mise doit être supérieur ou égale à 100$')
                

            if userOption > wallet:

                print('\n Désolé, vous n\'avez pas les fonds nécessaires pour une telle mise.')
                print('\n >>> Votre porte-monnaie actuelle est de : ' + str(wallet) + "$")

            if userOption <= wallet and userOption >= 100:
               
                wallet = wallet - userOption
                check = True
                getNumber(userOption)  
                

        except ValueError:
            print("Désolé, ce montant n'est pas valable.")



# Take as parameter the value of bet. Provide a number to put the bet

def getNumber(bet):
    
    global wallet

    print('\n >>> Votre porte-monnaie actuel est de : ' + str(wallet) + "$")

    check = False

    while check == False:

        userOption = input("\n Sur quel numéro  désirez vous placer votre mise ? : ")

        try:

            userOption = int(userOption)

            if userOption > 49 or userOption < 0:
                print('\n Veuillez sélectionner un numéro compris entre 0 et 49 : ')
            
            if userOption < 50 and userOption >= 0:
                check = True
                resolveBet(bet,userOption,random.randint(0, 49))   


        except ValueError:
            print('\n Ce numéro n\'est pas valable !') 




# Take as parameter the value of the bet, the value of user number selected, the random value of the spinner.

def resolveBet(userBet,userNumber,spinResult):

    global wallet
    global game
    global gameWin
    global gameLoss
    global bigPrice

    print('\n Nous avons un numéro ! Le numéro gagnant est le : ' + str(spinResult))

    game+=1 

    if userNumber == spinResult:
        price = userBet * 3
        wallet = wallet + price
        bigPrice+=1
        print('\n Vous avez gagnez le numéro gagnant, Vous récupérez trois votre mise, bien joué !')
        print('\n >>> Votre porte-monnaie actuel est de : ' + str(wallet) + "$")
        menu(False)

    elif userNumber % 2 == 0 and spinResult % 2 == 0:
        print("\n Votre numéro est de la même couleur ! Vous récupérez votre mise. ")
        wallet = wallet + userBet
        gameWin+=1
        print('\n >>> Votre porte-monnaie actuel est de : ' + str(wallet) + "$")
        menu(False)

    elif userNumber % 2 != 0 and spinResult % 2 != 0 :   
        print("\n Votre numéro est de la même couleur ! Vous récupérez votre mise. ")
        wallet = wallet + userBet
        gameWin+=1
        print('\n >>> Votre porte-monnaie actuel est de : ' + str(wallet) + "$")
        menu(False) 

    else:
        gameLoss+= 1
        print('\n Pas de chance votre numéro n\'est pas de la même couleur... ')
        menu(False)    
            


# Start the casino from a single call of this function  :)

def init():
    
    print("\n Bienvenue au Casino, nous vous offrons une mise de départ de 5000$ ! \n")
   
    global wallet
    wallet = 5000

    print(' Bonne chance, et amusez vous bien ! \n ')
    input("\n Appuyez sur enter pour continuer... \n ")
    menu(True)



    
    




init()

