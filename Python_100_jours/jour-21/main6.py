import random

def jeu_tables_multiplication():
    # Paramètres configurables
    niveaux_difficulte = {
        1: {'erreurs': 3, 'victoire_requise': 3},
        2: {'erreurs': 2, 'victoire_requise': 5},
        3: {'erreurs': 1, 'victoire_requise': 6}
    }

    print("Bienvenue au jeu d'apprentissage des tables de multiplication !")

    # Demande à l'utilisateur s'il veut choisir une table spécifique
    choix_table = input("Voulez-vous réviser toutes les tables (T) ou une table spécifique (S) ? ").upper()

    # Vérifie le choix de l'utilisateur
    if choix_table == 'T':
        tables = list(range(2, 11))
    elif choix_table == 'S':
        # Demande à l'utilisateur de choisir une table spécifique
        table = int(input("Choisissez la table de multiplication que vous voulez réviser (1-10) : "))

        # Vérifie si la table choisie est valide
        if not 1 <= table <= 10:
            print("Veuillez choisir une table de multiplication entre 1 et 10.")
            return

        tables = [table]
    else:
        print("Veuillez choisir 'T' pour toutes les tables ou 'S' pour une table spécifique.")
        return

    # Demande à l'utilisateur de choisir le niveau de difficulté
    niveau_difficulte = int(input("Choisissez le niveau de difficulté (1-3) : "))

    # Vérifie si le niveau de difficulté choisi est valide
    if niveau_difficulte not in niveaux_difficulte:
        print("Veuillez choisir un niveau de difficulté parmi 1, 2, ou 3.")
        return

    # Récupère les paramètres appropriés en fonction du niveau de difficulté
    erreurs_restantes = niveaux_difficulte[niveau_difficulte]['erreurs']
    victoire_requise = niveaux_difficulte[niveau_difficulte]['victoire_requise']

    print(f"\nSuper ! Vous avez choisi le niveau {niveau_difficulte} de difficulté.")
    print("Commençons le jeu.\n")

    score = 0

    # Pose une question pour chaque table choisie
    for i in range(2, 11):
        # Génère aléatoirement les multiplicateurs pour rendre le jeu plus varié
        multiplicateur = random.randint(2, 11)

        if choix_table == 'T':
            # Génère aléatoirement les tables pour rendre le jeu plus varié
            table = random.randint(2, 10)
        else:
            # Utilise la table spécifique choisie par l'utilisateur
            table = tables[0]

        while erreurs_restantes > 0:
            # Pose la question à l'utilisateur
            user_input = input(f"{i}. Combien font {multiplicateur} x {table} ? ")

            # Vérifie si la réponse de l'utilisateur est un nombre entier
            try:
                reponse = int(user_input)
            except ValueError:
                print("Veuillez entrer un nombre entier.")
                continue  # Recommence la boucle si la réponse n'est pas un nombre entier

            # Vérifie la réponse
            if reponse == multiplicateur * table:
                print("Bravo ! C'est la bonne réponse.")
                score += 1
                break  # Sort de la boucle si la réponse est correcte
            else:
                print(f"Dommage. La réponse correcte était {multiplicateur} x {table} = {multiplicateur * table}.")
                erreurs_restantes -= 1
                print(f"Il vous reste {erreurs_restantes} essais.")

        # Affiche le score partiel après chaque question
        print(f"Votre score partiel est de {score} sur {i}.\n")

        # Vérifie si le joueur a atteint le nombre de bonnes réponses requis pour la victoire
        if score == victoire_requise:
            print("Félicitations ! Vous avez atteint le nombre requis de bonnes réponses. Vous avez gagné !")
            return

    # Affiche le score final si le joueur n'a pas gagné
    print(f"Fin du jeu ! Votre score total est de {score} sur {len(tables) * 10}.")

# Appelle la fonction du jeu
jeu_tables_multiplication()
