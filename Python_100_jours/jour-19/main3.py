# imports module random
import random

# Le mot-clé "def" pour définir une fonction. créer un bloc de code qui peut être appelé et exécuté ultérieurement.
def jeu_nombre_mystere():
  
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
                print("Merci d'avoir joué !")
                return

            # choix converti en int
            choix = int(choix)

            # Incrémente le nombre de tentatives.
            tentatives += 1

            # Compare le choix avec le nombre mystère.
            if choix < nombre_mystere:
                print(f"Tentative n°{tentatives} C'est plus !")
            elif choix > nombre_mystere:
                print(f"Tentative n°{tentatives} C'est moins !")
            else:
                print(f"Bravo, tu as trouvé en {tentatives} tentatives !")

                # Demande si rejouer.
                rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()

                # Si choix différent de 'o', quitte le jeu.
                if rejouer != 'o':
                    print("Merci d'avoir joué !")
                    return
                else:
                    # Génère un nouveau nombre mystère et réinitialise les tentatives.
                    nombre_mystere = random.randint(1, 1000)
                    tentatives = 0

        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Instructions du jeu
print("Jeu du Nombre Mystère")
print("Devine un nombre entre 1 et 1000.")
print("Entre 'q' à tout moment pour quitter.")
print("Bonne chance !")

# Démarre le jeu
jeu_nombre_mystere()
