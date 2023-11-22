# Affichage des instructions du jeu
# Pour lancer le jeu, tapez dans la console :
# Premier joueur remportant trois matchs gagne la partie.

print("JEU PIERRE-FEUILLE-CISEAUX")
print("Tape une lettre ci-dessous puis appuie sur Entrée.")
print("   P  pour (✊) Pierre")
print("   F  pour (🤚) Feuille")
print("   C  pour (✌️ ) Ciseaux")
print("   Q  pour (❌) Quitter le jeu")

# Import de la fonction getpass pour une saisie incognito
from getpass import getpass as input

# Initialisation des variables
tour = 0  # Nombre de tours
score1 = 0  # Score du joueur 1
score2 = 0  # Score du joueur 2
choices = {"p": "✊ Pierre", "f": "🤚 Feuille", "c": "✌️ Ciseaux", "q": "❌ Quitter le jeu !" } 
# Dictionnaire des choix 

# Boucle principale du jeu
while True:
    # Incrémentation du nombre de tour
    tour += 1
    # Affiche le nombre de tour
    print(f"\nTOUR n°{tour}")

    # Vérification des conditions de fin de partie
    if score1 >= 3:
        print("--------- Résultat final -------------")
        print("Player1 remporte la partie 🏆, bravo !")
        # Sortie de la boucle principale
        break
      
    elif score2 >= 3:
        print("--------- Résultat final -------------")
        print("Player2 remporte la partie 🏆, bravo !")
        # Sortie de la boucle principale
        break
      
    # Affiche des commentaires sur les scores  
    elif score1 == 2 and score2 != 2:
        print("Player2, réduisez le score sinon c'est perdu ! ")
    elif score2 == 2 and score1 != 2:
        print("Player1, réduisez le score sinon c'est perdu ! ")
    elif score2 == 2 and score1 == 2:
        print("Attention dernier tour, bonne chance !")

    # Saisie des choix des joueurs
    player1 = input("Choix de Player1 ? ").lower()
    player2 = input("Choix de Player2 ? ").lower()
    print()

    # Vérification des entrées et calcul des résultats
    # Cas d'égalité
    if player1 == player2:
        print(f"{choices[player1]} contre {choices[player2]}, match nul !")
   # Cas où Player1 gagne  
    elif (player1 == "p" and player2 == "c") or (player1 == "f" and player2 == "p") or (player1 == "c" and player2 == "f"):
        # Incrémentation score1
        score1 += 1
        # Affichage choix avec résultat dictionnaire
        print(f"{choices[player1]} gagne contre {choices[player2]}, match gagnant Player1 !")

    # Cas où Player2 gagne
    elif (player2 == "p" and player1 == "c") or (player2 == "f" and player1 == "p") or (player2 == "c" and player1 == "f"):
        # Incrémentation score2
        score2 += 1
        # Affichage choix avec résultat dictionnaire
        print(f"{choices[player1]} perd contre {choices[player2]}, match gagnant Player2 !")

    # Gestion de la sortie du jeu
    if player1 == "q" or player2 == "q":
        print(f"Player1 à choisi {choices[player1]} et Player2 à choisi {choices[player2]}")
        print("Merci d'avoir joué !")
        # Sortie du programme
        exit()
      
    # Gestion des erreurs de saisie  
    elif player1 not in ['p', 'f', 'c'] or player2 not in ['p', 'f', 'c']:
        print("Je n'ai pas compris, recommencez !")
        # Décrémentation du nombre de tour et retour au début de la boucle
        tour -= 1
        # reprise de la boucle au départ
        continue

    # Affichage des scores
    print(f"SCORE: Player1 = {score1}   Player2 = {score2}")
    # Afffiche égalité score
    if score2 == score1:
        print("Égalité !")
