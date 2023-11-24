import random
import time

def jeu_tour_etages():
    print("Jeu de la Tour 🏰")

    # Déclaration variable étage mystère.
    etage_mystere = random.randint(1, 1000)

    # Déclaration variable tentatives.
    tentatives = 0

    print("Bienvenue dans la tour de 1000 étages.")
    print("Vous êtes actuellement au rez-de-chaussée.")

    while True:
        # try / except pour traiter les erreurs d'entrée.
        try:
            choix = input("\nSélectionnez un étage (ou entrez 'q' pour quitter) : ")

            # Vérifie si le joueur veut quitter
            if choix.lower() == 'q':
                print(f"Vous vous arrêtez à l'étage {etage_mystere}.")
                print("Merci d'avoir joué ! 👋")
                return

            # choix converti en int
            choix = int(choix)

            # Incrémente le nombre de tentatives.
            tentatives += 1

            # Compare le choix avec l'étage mystère.
            if choix < etage_mystere:
                print(f"Vous montez à l'étage n°{choix}... Encore plus haut ! 🏢")
            elif choix > etage_mystere:
                print(f"Vous descendez à l'étage n°{choix}... Encore plus bas ! ⬇️")
            else:
                print(f"Félicitations ! Vous êtes arrivé à l'étage {etage_mystere} en {tentatives} tentatives ! 🎉")
                time.sleep(1)  # Délai d'une seconde pour l'effet de pause

                # Demande si rejouer.
                rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()

                # Si choix différent de 'o', quitte le jeu.
                if rejouer != 'o':
                    print("Merci d'avoir joué ! 👋")
                    return
                else:
                    print("Vous redémarrez au rez-de-chaussée... 🔄")
                    time.sleep(1)  # Délai d'une seconde pour l'effet de pause

                    # Génère un nouvel étage mystère et réinitialise les tentatives.
                    etage_mystere = random.randint(1, 1000)
                    tentatives = 0
                    print("Nouvel étage généré. Bonne chance ! 🏰")

        except ValueError:
            print("Veuillez entrer un numéro d'étage valide. 🤔")

# Démarre le jeu
jeu_tour_etages()
