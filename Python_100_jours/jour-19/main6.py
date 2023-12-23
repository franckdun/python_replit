# Fonction pour calculer l'intérêt mensuel
def calculer_interet_mensuel(capital, taux):
    return (capital / 100) * taux

# Présentation des règles du calculateur de crédit
print("Bienvenue chez Petit Crédit.")

print(" Empreint supérieur à 100€.")
print(" Mensualités supérieur à 50€.")
print(" Intérêt mensuel fixé à 5%.")

# Gestion de la saisie utilisateur avec une boucle
while True:
    # Entrée utilisateur pour le capital initial
    capital_initial = input("\nEntrez le montant souhaité ? ")
    # Vérification de la saisie utilisateur
    mensualite = input("Entrez la mensualité souhaité ? ")

    # Vérification de la validité de l'entrée
    try:
        mensualite = float(mensualite)
        if mensualite < 50:
            print("La mensualité doit être supérieur à 50€.") 
            continue
        capital = float(capital_initial)
        if capital > 99:
            break  # Sortir de la boucle si l'entrée est valide
        else:
            print("Le capital doit être supérieur à 500€. Réessayez.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Initialisation des variables

taux = 5  # Taux d'intérêt mensuel fixé à 5%
total_interets = 0 # conteur intérêts
mois = 0 # conteur nombre 

# Affichage du solde initial
print(f"\nSolde initial : {capital:.2f}€")

# Boucle for pour calculer le nombre de mois de paiement
for mois in range(1, 500):
    # Calcul des intérêts et mise à jour du capital
    interet = calculer_interet_mensuel(capital, taux)
    capital += interet
    total_interets += interet
    capital -= mensualite

    # Vérification si le capital est remboursé
    if capital <= 100:
        print(f"\nMois {mois}:")
        print(f"Payement {capital + interet:.2f}€ moins intérêts {interet:.2f}€")
        print("Crédit remboursé !")
        break

    # Affichage des détails mensuels
    print(f"\nMois {mois}:")
    print(f"Payement {mensualite}€ moins intérêts {interet:.2f}€")
    print(f"Solde    {capital:.2f}€")

# Affichage du résultat final
pourcentage = (total_interets * 100) / float(capital_initial)
print(f"\nDurée du crédit : {mois} mois ")
print(f"Coût du crédit : {total_interets:.2f}€")
print(f"Soit {pourcentage:.2f}% du capital initial.")
