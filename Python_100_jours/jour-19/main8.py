# Fonction pour calculer l'intérêt mensuel
def calculer_interet_mensuel(capital, taux):
    return (capital / 100) * taux

# Présentation des règles du calculateur de crédit
print("Bienvenue chez Petit Crédit.")
#print("Montant emprunté doit être supérieur à 100€.")
print("Intérêt mensuel sur mensualité fixé à 5%.")

# Gestion de la saisie utilisateur avec une boucle
while True:
    # Entrée utilisateur pour le capital initial
    capital_initial = input("\nEntrez un montant de 100€ a 10000€ maximum ? ")

    # Vérification de la validité de l'entrée
    try:
        capital = float(capital_initial)
        if capital > 100:
            break  # Sortir de la boucle si l'entrée est valide
        else:
            print("Le montant emprunté doit être supérieur à 100€. Réessayez.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Choix du type de crédit (à échéance fixe ou libre)
while True:
    choix_credit = input("Mensualités fixes(1) ou Durée fixe(2) ? ")

    if choix_credit == "1":
        # Crédit à échéance fixe
        mensualite = float(input("\n(1)Entrez payement mensuel souhaitée ? "))
        mois = None  # Pas besoin de spécifier la durée dans ce cas
        break
      
    elif choix_credit == "2":
        # Crédit à échéance libre
        mois = int(input("\n(2) Entrez la durée maximum en mois : "))
        mensualite = capital / mois
        if mensualite < 100:
            mensualite = 100
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
    capital_restant += interet #conteur intérets + capital
    total_interets += interet  #conteur intérets

    # Réduction du capital restant si une mensualité est spécifiée
    if mensualite:
      capital_restant -= mensualite

    # Vérification si le capital est remboursé
    if capital_restant <= 100 or capital_restant <= mensualite:
        print(f"\nMois {mois}:")
        print(f"Payement {mensualite:.2f}€ moins intérêts {interet:.2f}€")
        print("Crédit remboursé !")
        break

    # Affichage des détails mensuels
    print(f"\nMois {mois}:")
    print(f"Payement {mensualite:.2f}€ moins intérêts {interet:.2f}€")
    capital_restant -= mensualite
    print(f"Solde     {capital_restant:.2f}€")

# Affichage du résultat final
pourcentage = (total_interets * 100) / float(capital_initial)
print(f"\nDurée du crédit : {mois} mois ")
print(f"Coût du crédit : {capital_initial} + {total_interets:.2f} d'intérêts")
print(f"Soit {pourcentage:.2f}% du capital initial.")
