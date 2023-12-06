#Instruction du jeu
print("PIERRE-FEUILLE-CISEAUX")
print("Tapez une lettre ci-dessous puis faites entré.")
print("   P  pour Pierre.")
print("   F  pour Feuille.")
print("   C  pour Ciseaux.")
print("   Q  pour Quiter le jeu.")

#Permet de faire une saisie inconito
from getpass import getpass as input

# déclaration des variables
tour = 0
score1 = 0
score2 = 0

while True:

    tour += 1
    print(f"\nTOUR n°{tour}")
  
    if (score1 >= 3):
        print("----- Resultat final -----")
        print("Gagnant du match Player1, bravo!")
        break
    elif (score2 >= 3):
        print("----- Resultat final -----")
        print("Gagnant du match Player2, bravo!")
        break  
    elif (score1 == 2 ) and (score2 != 2 ):
        print("Player2 rétablissez l'égalité sinon c'est perdu! ")
    elif (score2 == 2 ) and (score1 != 2 ):
        print("Player1 rétablissez l'égalité sinon c'est perdu! ")
    elif (score2 == 2 ) and (score1 == 2 ):
        print("Attention dernier tour, bonne chance !")
  
    # Déclaration des variables avec saisie en minuscules pour faciliter la comparaison
    player1 = input("Votre choix Player1 ?").lower()
    player2 = input("Votre choix Player2 ?").lower()
    print()
  
    #Cas d'égalité
    if (player1 == "p") and (player2 == "p") :
        print("Pierre contre Pierre !")       
    elif player1 == "f" and player2 == "f":
        print("Feuille contre Feuille !")       
    elif player1 == "c" and player2 == "c":
        print("Ciseaux contre Ciseaux !")
        
    #Cas gagnant player1
    elif player1 == "p" and player2 == "c":
        score1 = score1 + 1
        print("Pierre écrase Ciseaux, Gagnant player1 !")         
    elif player1 == "f" and player2 == "p":
        score1 = score1 + 1
        print("Feuille enveloppe Pierre, Gagnant player1 !")
    elif player1 == "c" and player2 == "f":
        score1 = score1 + 1
        print("Ciseaux découpe Feuille, Gagnant player1 !")
        
    #Cas gagnant player2
    elif player1 == "p" and player2 == "f":
        score2 = score2 + 1
        print("Feuille enveloppe Pierre, Gagnant player2 !")       
    elif player1 == "f" and player2 == "c":
        score2 = score2 + 1
        print("Ciseaux découpe Feuille, Gagnant player2 !")       
    elif player1 == "c" and player2 == "p":
        score2 = score2 + 1
        print("Pierre écrase Ciseaux, Gagnant player2 !")
      
    #Cas de sortie du jeu et erreurs de frappes
    elif player1 == "q" or player2 == "q":
        print("Vous avez quitté, merci d'avoir joué !")
        exit()
    else:
        print("Je n'ai pas compris, recommencez !")
        tour -= 1
        continue
      
    #Affichage scores et égalités
    print(f"SCORE: Player1 = {score1}   Player2 = {score2}")
    if (score2 == score1 ):
       print("Players égalité !")