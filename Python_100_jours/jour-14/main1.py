#pr�sentation du jeu
print("PIERRE-FEUILLE-CISEAUX")
print("Tapez une des lettres ci-dessous puis faites entr�.")
print(" p   Pour pierre.")
print(" f   Pour feuille.")
print(" c   Pour ciseaux.")
print()

#Permet de faire une saisie inconito
from getpass import getpass as input

#--------- 1er TOUR ---------
print("Premier tour !")

#d�claration des variables
player1 = input("Player1 Quel est votre choix ?")
player2 = input("Player2 Quel votre choix ?")
score1 = 0
score2 = 0
print()

#Cas d'�galit�
if player1 == "p" and player2 == "p":
    print("pierre contre pierre, �galit� !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "f":
    print("feuille contre feuille, �galit� !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "c":
    print("ciseaux contre ciseaux, �galit� !")
    print("Score player1:", score1)
    print("Score player2:", score2)

#Cas gagnant player1
elif player1 == "p" and player2 == "c":
    score1 = score1 + 1
    print("La pierre �crase les ciseaux, player1 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "p":
    score1 = score1 + 1
    print("La feuille enveloppe la pierre, player1 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "f":
    score1 = score1 + 1
    print("Les ciseaux coupent la feuille, player1 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)

#Cas gagnant player2
elif player1 == "p" and player2 == "f":
    score2 = score2 + 1
    print("La feuille enveloppe la pierre, player2 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "c":
    score2 = score2 + 1
    print("Les ciseaux coupent la feuille, player2 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "p":
    score2 = score2 + 1
    print("La pierre �crase les ciseaux, player2 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)

else:
    print("Je n'ai pas compris, recommencez")
print()

#--------- DEUXIEME TOUR ---------
#Pr�sentation
print("Deuxi�me tour !")
if score1 > score2:
    print("Attention player2 si player1 gagne ce tour, Player1 aura gagn� !")
elif score2 > score1:
    print("Attention player1 si player2 gagne ce tours, Player2 aura gagn� !")

#d�claration des variables
player1 = input("Player1 Quel est votre choix ?")
print()
player2 = input("Player2 Quel votre choix ?")
print()

#Cas d'�galit�
if player1 == "p" and player2 == "p":
    print("pierre contre pierre, �galit� !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "f":
    print("feuille contre feuille, �galit� !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "c":
    print("ciseaux contre ciseaux, �galit� !")
    print("Score player1:", score1)
    print("Score player2:", score2)

#Cas gagnant player1
elif player1 == "p" and player2 == "c":
    score1 = score1 + 1
    print("La pierre �crase les ciseaux, player1 est Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "p":
    score1 = score1 + 1
    print("La feuille enveloppe la pierre, player1 est Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "f":
    score1 = score1 + 1
    print("Les ciseaux coupent la feuille, player1 est Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)

#Cas gagnant player2
elif player1 == "p" and player2 == "f":
    score2 = score2 + 1
    print("La feuille enveloppe la pierre, player2 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "c":
    score2 = score2 + 1
    print("Les ciseaux coupent la feuille, player2 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "p":
    score2 = score2 + 1
    print("La pierre �crase les ciseaux, player2 est Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)

else:
    print("Je n'ai pas compris, recommencez")

#--------- TROIXIEME TOUR ---------

print()
if (score1 > score2):
    print("Player1 est Gagnant du match, bravo!")
elif (score2 > score1):
    print("Player2 est Gagnant du match, bravo!")
else:
    print("Match nul, bien jou� !")
    print()
    print("Dernier tour !")
    #d�claration des variables
    player1 = input("Player1 Quel est votre choix ?")
    player2 = input("Player2 Quel votre choix ?")
    print()

    #Cas d'�galit�
    if player1 == "p" and player2 == "p":
        print("pierre contre pierre, �galit� !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "f" and player2 == "f":
        print("feuille contre feuille, �galit� !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "c" and player2 == "c":
        print("ciseaux contre ciseaux, �galit� !")
        print("Score player1:", score1)
        print("Score player2:", score2)

    #Cas gagnant player1
    elif player1 == "p" and player2 == "c":
        score1 = score1 + 1
        print("La pierre �crase les ciseaux, player1 Gagnant !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "f" and player2 == "p":
        score1 = score1 + 1
        print("La feuille enveloppe la pierre, player1 Gagnant !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "c" and player2 == "f":
        score1 = score1 + 1
        print("Les ciseaux coupent la feuille, player1 Gagnant !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    #Cas gagnant player2
    elif player1 == "p" and player2 == "f":
        score2 = score2 + 1
        print("La feuille enveloppe la pierre, player2 Gagnant !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "f" and player2 == "c":
        score2 = score2 + 1
        print("Les ciseaux coupent la feuille, player2 Gagnant !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "c" and player2 == "p":
        score2 = score2 + 1
        print("La pierre �crase les ciseaux, player2 Gagnant !")
        print("Score player1:", score1)
        print("Score player2:", score2)
print()
print("----- Resultat final -----")
if (score1 > score2):
    print("Player1 est le gagnant du match, bravo!")
elif (score2 > score1):
    print("Player2 est le gagnant du match, bravo!")
else:
    print("Je n'ai pas compris, recommencez")
