import random

def jeu_devine_la_somme(): # Fonction qui gère le jeu 
    credit_initial = 1200 # Déclaration var credit_initial
    print("Deviner la somme entre 500 et 1500.")
    print("12 tentatives, une tentative coute 50$")
    print("Quittez à tout moment en tapant 'q'")
    print("Bonne chance !")

    while True: # tant que le joueur n'a pas quitté
        credit = credit_initial #crédit en cours
        print("\nNouvelle partie ! ")
        jouer = True # jouer vaut toujours vrai

        while jouer and credit > 0: #tant que jouer et crédit > 0
            somme_mystere = random.randint(500, 1500)
            tentatives = 1 #déclaration variable tentatives

            while tentatives < 13: # tant que tentatives < 13
                choix = input(f"Crédit {credit}$  Devinez la somme ? ")

                if choix.lower() == 'q':
                    print("Merci d'avoir joué !")
                    return # quite la fonction

                try: # bloc try gère les erreurs
                    credit -= 50 # Déduire 100 crédits à chaque tentative
                    tentatives += 1 # Incrémenter le nombre de tentatives   
                    choix = int(choix) # conversion choix en entier

                    if choix == somme_mystere:
                        tentatives -= 1 # décrémente 1 car on a la bonne somme
                        print(f"Bravo ! Vous avez gagné {somme_mystere} $ en {tentatives} tentatives.")
                        credit += somme_mystere
                        break

                    elif credit < 0:
                        credit = 0
                        print("Domage ! Plus de Crédit. Vous avez perdu ! ")
                        return

                    elif choix < somme_mystere:
                         print(f"Crédit {credit}$              C'est plus  ?")
                         print(f"\nTentative n°{tentatives}")
                    else:
                        print(f"Crédit {credit}$              C'est moins ?  ")
                        print(f"\nTentative n°{tentatives}")

                except ValueError: # bloc except gère les erreurs
                    credit += 50
                    tentatives -= 1
                    print(f"\nErreur de frappe, recommencez tentative n°{tentatives} ou tapez 'q' pour quitter le jeu.")
            else:
                print(f"\nDommage ! La somme était {somme_mystere}.")

            print(f"Crédit restant : {credit} $")
            rejouer = input("\nVoulez-vous rejouer ? (y/n) : ").lower()
            jouer = rejouer == 'y' # jouer devient vrai si on veut rejouer

        if input("Voulez-vous quitter le jeu ? (y/n) : ").lower() == 'y':
            print("Merci d'avoir joué !")
            break # quitte la boucle while

jeu_devine_la_somme()
