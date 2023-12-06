import random

def jeu_devine_la_somme():
    credit_initial = 1200
    
    print(f"?? Recevez {credit_initial}$ de crédit pour trouver une somme comprise entre 1 et 1000 en moins de 12 tentatives.")
    print("Quittez en tapant 'q'.")

    while True: # tant que le joueur n'a pas quitté
        credit = credit_initial #crédit en cours
        print(f"\nNouvelle partie ! Crédit actuel : {credit} $.")
        jouer = True # jouer en cours
      
        while jouer and credit > 0: # tant que jouer et crédit > 0
            somme_mystere = random.randint(1, 1000)
            tentatives = 1 #déclaration variable tentatives

            while tentatives < 12: # tant que tentatives < 12
                choix = input("Devinez la somme ? ")

                if choix.lower() == 'q':
                    print("Merci d'avoir joué ! ??")
                    return # quite la fonction

                try:
                    choix = int(choix) # conversion choix en entier

                    if choix == somme_mystere:
                        print(f"Bravo ! Vous avez gagné {somme_mystere} $ en {tentatives + 1} tentatives.")
                        credit += somme_mystere
                        break
                    elif choix < somme_mystere:
                        print("C'est plus  ?")
                        print(f"\nTentative n°{tentatives + 1}")
                    else:
                        print("C'est moins ?")
                        print(f"\nTentative n°{tentatives + 1}")

                    tentatives += 1

                except ValueError:
                    print(f"\nErreur de frappe, recommencez votre tentative n°{tentatives} ou tapez 'q' pour quitter le jeu.")

            else:
                print(f"\nDommage ! La somme était {somme_mystere}.")
                credit -= somme_mystere

            print(f"Crédit restant : {credit} $")
            rejouer = input("Voulez-vous rejouer ? (y/n) : ").lower()
            jouer = rejouer == 'y'

        if input("Voulez-vous quitter le jeu ? (y/n) : ").lower() == 'y':
            print("Merci d'avoir joué ! ??")
            break

jeu_devine_la_somme()
