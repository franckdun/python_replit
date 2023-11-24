import random
import time

def jeu_nombre_mystere():
    print("Jeu du Nombre Mystère 🎮")
    print("Devine un nombre entre 1 et 1000.")
    print("Entre 'q' à tout moment pour quitter.")
    print("Bonne chance ! 🍀")

    # Déclaration variable nombre aléatoire.
    nombre_mystere = random.randint(1, 1000)

    # Déclaration variable tentatives.
    tentatives = 0

    # Boucle principale while
    while True:
        # try / except pour traiter les erreurs d'entrée.
        try:
            choix = input("\nDevine le nombre : ")

            # Vérifie si le joueur veut quitter
            if choix.lower() == 'q':
                print(f"Le nombre mystère était {nombre_mystere}.")
                print("Merci d'avoir joué ! 👋")
                return

            # choix converti en int
            choix = int(choix)

            # Incrémente le nombre de tentatives.
            tentatives += 1

            # Compare le choix avec le nombre mystère.
            if choix < nombre_mystere:
                print(f"Tentative n°{tentatives}... C'est plus !  ➕")
            elif choix > nombre_mystere:
                print(f"Tentative n°{tentatives}... C'est moins ! ➖")
            else:
                print(f"Bravo, tu as trouvé en {tentatives} tentatives ! 🎉")
                time.sleep(1)  # Délai d'une seconde pour l'effet de pause

                # Demande si rejouer.
                rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()

                # Si choix différent de 'o', quitte le jeu.
                if rejouer != 'o':
                    print("Merci d'avoir joué ! 👋")
                    return
                else:
                    print("Génération d'un nouveau nombre mystère... 🔄")
                    time.sleep(1)  # Délai d'une seconde pour l'effet de pause

                    # Génère un nouveau nombre mystère et réinitialise les tentatives.
                    nombre_mystere = random.randint(1, 1000)
                    tentatives = 0
                    print("Nouveau nombre généré. Bonne chance ! 🍀")

        except ValueError:
            print("Veuillez entrer un nombre valide. 🤔")

# Démarre le jeu
jeu_nombre_mystere()
