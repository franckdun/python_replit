# Fonction pour calculer l'intérêt mensuel
import imaplib

def calculer_interet_mensuel(capital, taux):
    return (capital / 100) * taux

# Présentation des règles du calculateur de crédit
print("Bienvenue chez Petit Crédit.")
print("Intérêt mensuel sur mensualité fixé à 5%.")
print("Tapez'x' pour quitter.")

# Gestion de la saisie utilisateur avec une boucle
while True:
    # Entrée utilisateur pour le capital initial
    capital_initial = input("\nEntrez un montant de 500€ à 10000€ maximum ? ")

    # Vérification de la saisie utilisateur
    if capital_initial.lower() == 'x':
        print("Sortie du programme.")
        break

    try:
        capital = float(capital_initial)
        if 500 <= capital <= 10000:
            break  # Sortir de la boucle si l'entrée est valide
        else:
            print("Le montant emprunté doit être entre 500€ et 10000€. Réessayez.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Choix du type de crédit (à échéance fixe ou libre)
while True:
    choix_credit = input("Mensualités fixes(1) ou Durée fixe(2) ? ")

    # Vérification de la saisie utilisateur
    if choix_credit.lower() == 'x':
        print("Sortie du programme.")
        exit()

    if choix_credit == "1":
        # Crédit à échéance fixe
        mensualite = float(input("\n(1) Entrez le paiement mensuel souhaité : "))
        mois = None  # Pas besoin de spécifier la durée dans ce cas
        break
    
    elif choix_credit == "2":
        # Crédit à échéance libre
        mois = int(input("\n(2) Entrez la durée maximum en mois : "))
        mensualite = (capital / mois)*2
        mensualite = max(100, mensualite)  # Assurer que la mensualité est au moins de 100€
        break

    else:
        print("Choix invalide. Veuillez choisir 1 ou 2.")

# Initialisation des variables
taux = 5  # Taux d'intérêt mensuel fixé à 5%
total_interets = 0
capital_restant = capital  # Pour suivre le capital restant

# Affichage du solde initial
print(f"\nSolde initial : {capital:.2f}€")

# Boucle for pour calculer le nombre de mois de paiement
for mois in range(1, mois + 1) if mois else range(1, 500):
    # Calcul des intérêts et mise à jour du capital
    interet = calculer_interet_mensuel(capital_restant, taux)
    total_interets += interet
    capital_restant += interet
      
    # Réduction du capital restant si une mensualité est spécifiée
    if mensualite:  
        capital_restant -= mensualite

    # Vérification si le capital est remboursé
    if capital_restant <= 100 or capital_restant <= mensualite:
        print(f"\nMois {mois}:")
        print(f"Payement {min(mensualite, capital_restant + interet):.2f}€ moins intérêts {interet:.2f}€")
        print("\n--------- Crédit remboursé ! ---------")
        break

    if mois >= 499 :
        print("Désolé, payement mensuel insufisant, recommencez !")
        exit()

    # Affichage des détails mensuels
    print(f"\nMois {mois}:")
    print(f"Payement {mensualite:.2f}€ moins intérêts {min(interet, mensualite):.2f}€")
    print(f"Solde     {capital_restant:.2f}€")

# Affichage du résultat final
pourcentage = (total_interets * 100) / float(capital_initial)
print(f"\nDurée du crédit : {mois} mois ")
print(f"Coût du crédit : {capital_initial} + {total_interets:.2f} d'intérêts")
print(f"Soit {pourcentage:.2f}% du capital initial.")
