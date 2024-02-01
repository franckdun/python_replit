import random

def jeu_tables_multiplication():
    print("Bienvenue au jeu d'apprentissage des tables de multiplication !")

    # Demande à l'utilisateur de choisir une table de multiplication
    table = int(input("Choisissez la table de multiplication que vous voulez réviser (1-10) : "))

    # Vérifie si la table choisie est valide
    if not 1 <= table <= 10:
        print("Veuillez choisir une table de multiplication entre 1 et 10.")
        return

    print(f"\nSuper ! Vous avez choisi la table de multiplication {table}.\n")

    score = 0

    # Pose 10 questions à l'utilisateur
    for i in range(1, 11):
        # Génère aléatoirement les multiplicateurs pour rendre le jeu plus varié
        multiplicateur = random.randint(1, 10)

        # Pose la question à l'utilisateur
        user_input = input(f"{i}. Combien font {multiplicateur} x {table} ? ")

        # Vérifie si la réponse de l'utilisateur est un nombre entier
        try:
            reponse = int(user_input)
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            return

        # Vérifie la réponse
        if reponse == multiplicateur * table:
            print("Bravo ! C'est la bonne réponse.\n")
            score += 1
        else:
            print(f"Dommage. La réponse correcte était {multiplicateur} x {table} = {multiplicateur * table}.\n")

    # Affiche le score final
    print(f"Fin du jeu ! Votre score est de {score} sur 10.")

# Appelle la fonction du jeu
jeu_tables_multiplication()
