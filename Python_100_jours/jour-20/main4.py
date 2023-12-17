# Critères du crédit
capital = 1000
mensualite = 100
taux_mensuel = 5

# Initialisation des variables
total_paiement = 0
total_mois = 0 

# Boucle for pour calculer le nombre de mois de paiement
for mois in range( 1, 500):  # Utilisation d'une limite pour éviter une boucle infinie au cas où le prêt ne serait jamais remboursé
    interet_mensuel = (capital/100) * taux_mensuel
    capital += interet_mensuel
    total_paiement += interet_mensuel
    capital -= mensualite
    total_mois += 1

    # Vérifier si le capital est remboursé
    if capital <= 100:
        print(f"Mois {mois}:")
        print(f"Payement {capital + interet_mensuel:.2f}€ / Interets {interet_mensuel:.2f}€ / Solde {capital:.2f}€")
        break
      
    # Afficher le paiement mensuel
    print(f"Mois {mois}:")
    print(f"Payement {mensualite}€ / Interets {interet_mensuel:.2f}€ / Solde {capital:.2f}€\n")


# Afficher le résultat final
print(f"\n{total_mois} mois pour rembourser, cout du credit {total_paiement:.2f}€")
