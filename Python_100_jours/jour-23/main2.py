import random

def jouer_devine_la_somme(credit_initial=1200, cout_tentative=50, nombre_tentatives=12, min_somme=500, max_somme=1500):
    """
    Fonction qui gère le jeu Devine la Somme.

    Args:
    - credit_initial (int): Le crédit initial du joueur. Par défaut: 1200.
    - cout_tentative (int): Le coût d'une tentative en crédit. Par défaut: 50.
    - nombre_tentatives (int): Le nombre de tentatives autorisées. Par défaut: 12.
    - min_somme (int): La valeur minimale de la somme à deviner. Par défaut: 500.
    - max_somme (int): La valeur maximale de la somme à deviner. Par défaut: 1500.
    """

    # Affichage des règles du jeu avec les paramètres par défaut
    print(f"Deviner la somme entre {min_somme} et {max_somme}.")
    print(f"{nombre_tentatives} tentatives, une tentative coûte {cout_tentative}$.")
    print("Quittez à tout moment en tapant 'q'.")
    print("Bonne chance !")

    # Boucle principale du jeu
    while True:
        credit = credit_initial  # Initialisation du crédit du joueur

        print("\nNouvelle partie ! ")
        jouer = True  # Initialisation de la variable de contrôle de jeu
        # Boucle de jeu
        while jouer and credit > 0:
            somme_mystere = random.randint(min_somme, max_somme)  # Génération de la somme mystère

            tentatives_restantes = nombre_tentatives  # Initialisation du nombre de tentatives restantes

            # Boucle de devinette
            while tentatives_restantes > 0:
                choix = input(f"Crédit {credit}$  Devinez la somme ? ")

                if choix.lower() == 'q':  # Sortie du jeu si le joueur tape 'q'
                    print("Merci d'avoir joué !")
                    return

                try:
                    credit -= cout_tentative  # Déduction du coût de la tentative du crédit du joueur
                    choix = int(choix)

                    if choix == somme_mystere:  # Si le choix est correct
                        print(f"Bravo ! Vous avez gagné {somme_mystere} $ en {nombre_tentatives - tentatives_restantes + 1} tentatives.")
                        credit += somme_mystere  # Ajout de la somme mystère au crédit du joueur
                        break
                    elif credit < cout_tentative:  # Si le joueur n'a plus de crédit
                        credit = 0
                        print("Dommage ! Plus de Crédit. Vous avez perdu ! ")
                        return
                    elif choix < somme_mystere:  # Si le choix est inférieur à la somme mystère
                         print(f"Crédit {credit}$              C'est plus !")
                    else:  # Si le choix est supérieur à la somme mystère
                        print(f"Crédit {credit}$              C'est moins !")

                    print(f"\nTentatives restantes : {tentatives_restantes - 1}")  # Affichage du nombre de tentatives restantes
                    tentatives_restantes -= 1  # Décrémentation du nombre de tentatives restantes

                except ValueError:  # Gestion des erreurs de saisie
                    credit += cout_tentative  # Remboursement du coût de la tentative
                    print("\nErreur de frappe, recommencez ou tapez 'q' pour quitter le jeu.")

            else:  # Si le joueur a épuisé toutes ses tentatives
                print(f"\nDommage ! La somme était {somme_mystere}.")

            rejouer = input("\nVoulez-vous rejouer ? (y/n) : ").lower()  # Demande au joueur s'il souhaite rejouer
            jouer = rejouer == 'y'  # Mise à jour de la variable de contrôle de jeu

        if input("Voulez-vous quitter le jeu ? (y/n) : ").lower() == 'y':  # Demande au joueur s'il souhaite quitter le jeu
            print("Merci d'avoir joué !")
            break

# Exemple d'utilisation avec les paramètres par défaut
jouer_devine_la_somme()
