import random

def jeu_tables_multiplication():
    # Paramètres configurables
    niveaux_difficulte = {
        1: {'table1', 'erreurs': 3, 'victoire_requise': 3},
        2: {'table2', 'erreurs': 2, 'victoire_requise': 5},
        3: {'table2', 'erreurs': 1, 'victoire_requise': 6}
    }

    # Tables administratives
    tables_admin = {
        'table1': list(range(2, 10)),
        'table2': list(range(2, 12)),
        'table3': list(range(2, 15))
    }

    print("Bienvenue au jeu d'apprentissage des tables de multiplication !")

    # Demande à l'utilisateur s'il veut choisir toutes les tables ou une table spécifique
    choix_table = input("Voulez-vous réviser toutes les tables (T) ou une table spécifique (S) ? ").upper()

    # Vérifie le choix de l'utilisateur
    if choix_table == 'T':
        # Demande à l'utilisateur de choisir le niveau de table
        niveau_table = int(input("Choisissez le niveau de table (1-3) : "))

        # Vérifie si le niveau de table choisi est valide
        if niveau_table not in range(1, 4):
            print("Veuillez choisir un niveau de table parmi 1, 2, ou 3.")
            return

        tables = tables_admin[f'table{niveau_table}']
    elif choix_table == 'S':
        # Demande à l'utilisateur de choisir une table spécifique
        table = int(input("Choisissez la table de multiplication que vous voulez réviser : "))

        # Vérifie si la table choisie est valide
        if table not in range(2, 16):
            print("Veuillez choisir une table de multiplication entre 2 et 15.")
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
    print(f"Vous devez obtenir {victoire_requise} bonnes réponses pour gagner.")
    print("A chaque erreur, vous perdrez 1 point.")
    print(f"Cependant, vous avez {erreurs_restantes} chances d'erreurs.")
    print("Facile, bonne chance!")

    print("Commençons le jeu !\n")

    score = 0

    # Pose une question pour chaque table choisie
    for i in range(2, 11):
        # Génère aléatoirement les multiplicateurs pour rendre le jeu plus varié
        multiplicateur = random.randint(2, 11)

        if choix_table == 'T':
            # Génère aléatoirement les tables pour rendre le jeu plus varié
            table = random.choice(tables)
        else:
            # Utilise la table spécifique choisie par l'utilisateur
            table = tables[0]

        while erreurs_restantes > 0:
            # Pose la question à l'utilisateur
            user_input = input(f"{i - 1}. Combien font {multiplicateur} x {table} ? ")

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
                if erreurs_restantes > 0:
                    print("Essayez encore !")  # Ajout d'une invite pour essayer à nouveau
                score -= 1  # On ne déduit le score que si la réponse est incorrecte

        # Affiche le score partiel après chaque question
        print(f"Votre score actuel est de {score} bonnes réponses sur {i - 1}.\n")

        # Vérifie si le joueur a atteint le nombre de bonnes réponses requis pour la victoire
        if score == victoire_requise:
            print("Félicitations ! Vous avez atteint le nombre requis de bonnes réponses. Vous avez gagné !")
            print(f"Fin du jeu ! Votre score total est de {score} sur {i - 1}.")
            return

    # Affiche le score final si le joueur n'a pas gagné
    print(f"Fin du jeu ! Votre score total est de {score} sur {i - 1}.")

# Appelle la fonction du jeu
jeu_tables_multiplication()
