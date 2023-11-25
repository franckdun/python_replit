import random

def jeu_devine_la_somme():

    credit = 1000 # Déclaration variable crédit initial.
  
    print(f"💰 Gagnez la cagnotte de {credit}$ trouvez la somme en moins de 12 tentatives. Quiter en tapant q .")  

    while credit > 0 : # Boucle principale 
      
        # Déclaration variable somme mystère.
        somme_mystere = random.randint(1, 1000)

        print(f"\nCrédit actuel : {credit} $.")

        try:
            while True: # Boucle de jeu
                choix = input("\nDevinez la somme entre 1 et 1000 : ")

                # Vérifie si le joueur veut quitter
                if choix.lower() == 'q':
                    print("Merci d'avoir joué ! 👋")
                    return

                choix = int(choix)

                # Vérifie si le choix est valide
                if 1 <= choix <= 1000:
                    # Incrémente le nombre de tentatives.
                    tentatives = 1

                    while choix != somme_mystere and tentatives < 5:
                        if choix < somme_mystere:
                            print(f"\nTentative n°{tentatives} : C'est plus !  ➕")
                        else:
                            print(f"\nTentative n°{tentatives} : C'est moins ! ➖")
                        tentatives += 1
                        choix = int(input("Devinez à nouveau : "))

                    if choix == somme_mystere :
                        print(f"Bravo ! Vous avez gagné {somme_mystere} $ en {tentatives} tentatives.")
                        credit += somme_mystere
                      
                    else:
                        print(f"\nDommage ! La somme était {somme_mystere}.")
                        credit -= somme_mystere

                    print(f"Crédit restant : {credit} $")

                    rejouer = input("Voulez-vous rejouer ? (y/n) : ")
                    if rejouer.lower() == 'y':
                        break
                    else:
                        print("Merci d'avoir joué ! 👋")
                        return

                else:
                    print("Veuillez entrer une somme valide entre 1 et 1000.")

        except ValueError:
            print("\nErreur de frappe recommencez !")
            print("Ou refaite q pour quitter le jeu.")
            
# Démarre le jeu
jeu_devine_la_somme()
