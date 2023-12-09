# Fonction pour calculer l'intérêt mensuel
def calculer_interet_mensuel(capital, taux):
    return (capital / 100) * taux

# Entrée Utilisateur
capital = float(input("Entrez le montant du capital : "))
#mensualite = float(input("Entrez le montant de la mensualité : "))
mensualite = 100

# Entrée administrateur
#taux = float(input("Entrez le taux d'intérêt mensuel : "))
taux = 5

# Initialisation des variables
total_interets = 0
mois = 0 

# Boucle for pour calculer le nombre de mois de paiement
for mois in range(1, 500):
    interet = calculer_interet_mensuel(capital, taux)
    capital += interet
    total_interets += interet
    capital -= mensualite
    mois += 1

    # Vérifier si le capital est remboursé
    if capital <= 100:
        print(f"Mois {mois}:")
        print(f"Payement {capital + interet:.2f}€ / Interets {interet:.2f}€ / Solde {capital:.2f}€")
        break

    # Afficher le paiement mensuel
    print(f"Mois {mois}:")
    print(f"Payement {mensualite}€ / Interets {interet:.2f}€ / Solde {capital:.2f}€\n")

# Afficher le résultat final

print(f"\n{mois} mois pour rembourser, coût du crédit {total_interets:.2f}€")

