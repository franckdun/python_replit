#présentation du jeu
print("PIERRE-FEUILLE-CISEAUX")
print("Tapez une des lettres ci-dessous puis faites entré.")
print(" p   Pour pierre.")
print(" f   Pour feuille.")
print(" c   Pour ciseaux.")
print()

#Permet de faire une saisie inconito
from getpass import getpass as input

#--------- 1er TOUR ---------
print("Premier tour !")

#déclaration des variables
player1 = input("Player1 Quel est votre choix ?")
player2 = input("Player2 Quel votre choix ?")
score1 = 0
score2 = 0
print()

#Cas d'égalité
if player1 == "p" and player2 == "p":
    print("pierre contre pierre, égalité !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "f":
    print("feuille contre feuille, égalité !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "c":
    print("ciseaux contre ciseaux, égalité !")
    print("Score player1:", score1)
    print("Score player2:", score2)

#Cas gagnant player1
elif player1 == "p" and player2 == "c":
    score1 = score1 + 1
    print("La pierre écrase les ciseaux, player1 Gagnant !")
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
    print("La pierre écrase les ciseaux, player2 Gagnant !")
    print("Score player1:", score1)
    print("Score player2:", score2)

else:
    print("Je n'ai pas compris, recommencez")
print()

#--------- DEUXIEME TOUR ---------
#Présentation
print("Deuxième tour !")
if score1 > score2:
    print("Attention player2 si player1 gagne ce tour, Player1 aura gagné !")
elif score2 > score1:
    print("Attention player1 si player2 gagne ce tours, Player2 aura gagné !")

#déclaration des variables
player1 = input("Player1 Quel est votre choix ?")
print()
player2 = input("Player2 Quel votre choix ?")
print()

#Cas d'égalité
if player1 == "p" and player2 == "p":
    print("pierre contre pierre, égalité !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "f" and player2 == "f":
    print("feuille contre feuille, égalité !")
    print("Score player1:", score1)
    print("Score player2:", score2)
elif player1 == "c" and player2 == "c":
    print("ciseaux contre ciseaux, égalité !")
    print("Score player1:", score1)
    print("Score player2:", score2)

#Cas gagnant player1
elif player1 == "p" and player2 == "c":
    score1 = score1 + 1
    print("La pierre écrase les ciseaux, player1 est Gagnant !")
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
    print("La pierre écrase les ciseaux, player2 est Gagnant !")
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
    print("Match nul, bien joué !")
    print()
    print("Dernier tour !")
    #déclaration des variables
    player1 = input("Player1 Quel est votre choix ?")
    player2 = input("Player2 Quel votre choix ?")
    print()

    #Cas d'égalité
    if player1 == "p" and player2 == "p":
        print("pierre contre pierre, égalité !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "f" and player2 == "f":
        print("feuille contre feuille, égalité !")
        print("Score player1:", score1)
        print("Score player2:", score2)
    elif player1 == "c" and player2 == "c":
        print("ciseaux contre ciseaux, égalité !")
        print("Score player1:", score1)
        print("Score player2:", score2)

    #Cas gagnant player1
    elif player1 == "p" and player2 == "c":
        score1 = score1 + 1
        print("La pierre écrase les ciseaux, player1 Gagnant !")
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
        print("La pierre écrase les ciseaux, player2 Gagnant !")
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
