import random

def jeu_devine_la_somme(): # Fonction qui g�re le jeu 
    credit_initial = 1200 # D�claration var credit_initial
    print("Deviner la somme entre 500 et 1500.")
    print("12 tentatives, une tentative coute 50$")
    print("Quittez � tout moment en tapant 'q'")
    print("Bonne chance !")

    while True: # tant que le joueur n'a pas quitt�
        credit = credit_initial #cr�dit en cours
        print("\nNouvelle partie ! ")
        jouer = True # jouer vaut toujours vrai

        while jouer and credit > 0: #tant que jouer et cr�dit > 0
            somme_mystere = random.randint(500, 1500)
            tentatives = 1 #d�claration variable tentatives

            while tentatives < 13: # tant que tentatives < 13
                choix = input(f"Cr�dit {credit}$  Devinez la somme ? ")

                if choix.lower() == 'q':
                    print("Merci d'avoir jou� !")
                    return # quite la fonction

                try: # bloc try g�re les erreurs
                    credit -= 50 # D�duire 100 cr�dits � chaque tentative
                    tentatives += 1 # Incr�menter le nombre de tentatives   
                    choix = int(choix) # conversion choix en entier

                    if choix == somme_mystere:
                        tentatives -= 1 # d�cr�mente 1 car on a la bonne somme
                        print(f"Bravo ! Vous avez gagn� {somme_mystere} $ en {tentatives} tentatives.")
                        credit += somme_mystere
                        break

                    elif credit < 0:
                        credit = 0
                        print("Domage ! Plus de Cr�dit. Vous avez perdu ! ")
                        return

                    elif choix < somme_mystere:
                         print(f"Cr�dit {credit}$              C'est plus  ?")
                         print(f"\nTentative n�{tentatives}")
                    else:
                        print(f"Cr�dit {credit}$              C'est moins ?  ")
                        print(f"\nTentative n�{tentatives}")

                except ValueError: # bloc except g�re les erreurs
                    credit += 50
                    tentatives -= 1
                    print(f"\nErreur de frappe, recommencez tentative n�{tentatives} ou tapez 'q' pour quitter le jeu.")
            else:
                print(f"\nDommage ! La somme �tait {somme_mystere}.")

            print(f"Cr�dit restant : {credit} $")
            rejouer = input("\nVoulez-vous rejouer ? (y/n) : ").lower()
            jouer = rejouer == 'y' # jouer devient vrai si on veut rejouer

        if input("Voulez-vous quitter le jeu ? (y/n) : ").lower() == 'y':
            print("Merci d'avoir jou� !")
            break # quitte la boucle while

jeu_devine_la_somme()
