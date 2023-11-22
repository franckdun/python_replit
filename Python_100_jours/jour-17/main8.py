# Instruction du jeu.
# Pour lancer le jeu, tapez dans la console :
# Premier joueur remportant trois matchs gagne la partie.

print("GAME PIERRE-FEUILLE-CISEAUX")
print("Tapez une lettre ci-dessous puis faites entré.")
print("   P  pour (✊) Pierre")
print("   F  pour (🤚) Feuille")
print("   C  pour (✌️ ) Ciseaux")
print("   Q  pour (❌) Quitter le jeu")

# Permet de faire une saisie incognito
from getpass import getpass as input

# Déclaration des variables
tour = 0 # Nombre de tour de jeu
score1 = 0 # Score du joueur 1
score2 = 0 # Score du joueur 2
p = "✊ Pierre"
f = "🤚 Feuille"
c = "✌️ Ciseaux"
# Boucle principale Tant que
while True:
    # incrémentation du nombre de tour
    tour += 1
    print(f"\nTOUR n°{tour}")
    # Si score1 supérieur ou égal à 3 
    if score1 >= 3:
        print("----- Résultat final -----")
        print("Gagnant de la partie Player1 🏆, bravo !")
        break
    # Si score2 supérieur ou égal à 3
    elif score2 >= 3:
        print("----- Résultat final -----")
        print("Gagnant de la partie Player2 🏆, bravo !")
        break
    # si score1 égal 2 et score2 différent de 2
    elif score1 == 2 and score2 != 2:
        print("Player2, rétablissez le score sinon c'est perdu ! ")
    # si score2 égal 2 et score1 différent de 2
    elif score2 == 2 and score1 != 2:
        print("Player1, rétablissez le score sinon c'est perdu ! ")
    # si score1 égal score2 
    elif score2 == 2 and score1 == 2:
        print("Attention dernier tour, bonne chance !")

    # Déclaration des variables avec saisie en minuscules pour faciliter la comparaison
    player1 = input("Votre choix Player1 ? ").lower()
    player2 = input("Votre choix Player2 ? ").lower()
    print()

    # Cas d'égalité
    if player1 == "p" and player2 == "p":
        print(f"{p} contre {p}, match nul !")
    elif player1 == "f" and player2 == "f":
        print(f"{f} contre {f}, match nul !")
    elif player1 == "c" and player2 == "c":
        print(f"{c} contre {c}, match nul !")

    # Cas gagnant player1
    elif player1 == "p" and player2 == "c":
        score1 += 1
        print(f"{p} écrase {c}, match gagnant Player1 !")
    elif player1 == "f" and player2 == "p":
        score1 += 1
        print(f"{f} enveloppe {p}, match gagnant Player1 !")
    elif player1 == "c" and player2 == "f":
        score1 += 1
        print(f"{c} découpe {f}, match gagnant Player1 !")

    # Cas gagnant player2
    elif player1 == "p" and player2 == "f":
        score2 += 1
        print(f"{p} enveloppée par {f}, match gagnant Player2 !")
    elif player1 == "f" and player2 == "c":
        score2 += 1
        print(f"{f} découpée par {c}, match gagnant Player2 !")
    elif player1 == "c" and player2 == "p":
        score2 += 1
        print(f"{c} écrasé par {p}, match gagnant Player2 !")

    # Cas de sortie du jeu et erreurs de frappes
    elif player1 == "q" or player2 == "q":
        print("Vous avez quitté, merci d'avoir joué !")
        exit()
    else:
        print("Je n'ai pas compris, recommencez !")
        tour -= 1
        continue

    # Affichage scores et égalités
    print(f"SCORE: Player1 = {score1}   Player2 = {score2}")
    if score2 == score1:
        print("Players égalité !")
