import random

def jeu_tables_multiplication():
    print("Bienvenue au jeu d'apprentissage des tables de multiplication !")

    # Demande à l'utilisateur s'il veut choisir une table spécifique
    choix_table = input("Voulez-vous réviser toutes les tables (T) ou une table spécifique (S) ? ").upper()

    # Vérifie le choix de l'utilisateur
    if choix_table == 'T':
        tables = list(range(1, 11))
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

    print("\nSuper ! Commençons le jeu.\n")

    score = 0

    # Pose une question pour chaque table choisie
    for table in tables:
        for i in range(1, 11):
            # Génère aléatoirement les multiplicateurs pour rendre le jeu plus varié
            multiplicateur = random.randint(1, 10)

            while True:
                # Pose la question à l'utilisateur
                user_input = input(f"{i}. Combien font {multiplicateur} x {table} ? ")

                # Vérifie si la réponse de l'utilisateur est un nombre entier
                try:
                    reponse = int(user_input)
                    break  # Sort de la boucle si la réponse est un nombre entier
                except ValueError:
                    print("Veuillez entrer un nombre entier.")

            # Vérifie la réponse
            if reponse == multiplicateur * table:
                print("Bravo ! C'est la bonne réponse.")
                score += 1
            else:
                print(f"Dommage. La réponse correcte était {multiplicateur} x {table} = {multiplicateur * table}.")

            # Affiche le score partiel après chaque question
            print(f"Votre score partiel est de {score} sur {i}.\n")

    # Affiche le score final
    print(f"Fin du jeu ! Votre score total est de {score} sur {len(tables) * 10}.")

# Appelle la fonction du jeu
jeu_tables_multiplication()
