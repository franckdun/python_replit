# Fonction pour calculer l'intérêt mensuel
def calculer_interet_mensuel(capital, taux):
    return (capital / 100) * taux

# Entrée Utilisateur
capital_initial = input("Entrez le montant souhaité ? ")
# Conversion en flottant
capital = float(capital_initial)


#mensualite = float(input("Entrez le montant de la mensualité : "))
mensualite = 100 # payement mensuel

# Entrée administrateur
#taux = float(input("Entrez le taux d'intérêt mensuel : "))
taux = 5 # 5%

# Initialisation des variables
total_interets = 0
mois = 0 

#vérifier si le capital est supérieur a 500 euros
while capital > 500:

  # Affiche le solde de départ
  print(f"\nSolde initial {capital:.2f}€")

  # Boucle for pour calculer le nombre de mois de paiement
  for mois in range(1, 500):
      #foncion def 
      interet = calculer_interet_mensuel(capital, taux)
      capital += interet #solde moins interet
      total_interets += interet #interets cumulés
      capital -= mensualite #solde moins paiement

      # Vérifier si le capital est remboursé
      if capital <= 100:
          print(f"\nMois {mois}:")
          print(f"Payement {capital + interet:.2f}€ moins interets {interet:.2f}€")
          print(f"Solde    {capital:.2f}€")
          break

      # Afficher le paiement mensuel
      print(f"\nMois {mois}:")
      print(f"Payement {mensualite}€ moins interets {interet:.2f}€")
      print(f"Solde    {capital:.2f}€")

  # Afficher le résultat final
  pourcentage = (total_interets * 100) / float(capital_initial)
  print(f"\nDuréé du crédit {mois} mois ")
  print(f"Coût du crédit {total_interets:.2f}€")
  print(f"soit {pourcentage:.2f}% du capital initial.")

# affiche erreur si capital < 500
if capital < 500 and mois == 0:
  print("Désolé votre capital doit etre supérieur à 500€")
  