import random

def jeu_devine_la_somme():
    credit_initial = 1000
    print(f"💰 Gagnez la cagnotte de {credit_initial}$ en trouvant la somme en moins de 5 tentatives. Quittez en tapant 'q'.")

    while True:
        credit = credit_initial
        somme_mystere = random.randint(1, 1000)
        print(f"\nCrédit actuel : {credit} $.")

        jouer = True
        while jouer and credit > 0:
            tentatives = 0
            while tentatives < 5:
                try:
                    choix = int(input("\nDevinez la somme entre 1 et 1000 : "))

                    if choix == somme_mystere:
                        print(f"Bravo ! Vous avez gagné {somme_mystere} $ en {tentatives + 1} tentatives.")
                        credit += somme_mystere
                        break
                    elif choix < somme_mystere:
                        print(f"\nTentative n°{tentatives + 1} : C'est plus !  ➕")
                    else:
                        print(f"\nTentative n°{tentatives + 1} : C'est moins ! ➖")

                    tentatives += 1

                except ValueError:
                    print("\nErreur de frappe, recommencez votre tentative ou tapez 'q' pour quitter le jeu.")

            else:
                print(f"\nDommage ! La somme était {somme_mystere}.")
                credit -= somme_mystere

            print(f"Crédit restant : {credit} $")
            rejouer = input("Voulez-vous rejouer ? (y/n) : ").lower()
            jouer = rejouer == 'y'

        if input("Voulez-vous quitter le jeu ? (y/n) : ").lower() == 'y':
            print("Merci d'avoir joué ! 👋")
            break

if __name__ == "__main__":
    jeu_devine_la_somme()
