# Calculateur de prêt indiquant le montant à rembourser pour un prêt de 1 000 $ avec un TAEG de 5 % sur 10 ans.

# Demander le montant à emprunter sur 10 ans
emprunte = int(input("Combien souhaitez-vous emprunter sur 10 ans ? "))

# Calcul du TAEG
taux_annuel = 0.05
taeg = emprunte * taux_annuel
print("Votre TAEG est de : ", taeg / 1000)

# Calcul du coût du crédit sur 10 ans
traites_annuelles = 10
montant_traites = emprunte / traites_annuelles
print("Traites de base sur 10 ans : ", montant_traites)

# Boucle for pour calculer le montant de chaque traite sur 10 ans
total_interet = 0
totaltraites = 0
for annee in range(1, traites_annuelles + 1):
    interet_annuel = montant_traites * taux_annuel
    montant_traites += interet_annuel
    total_interet += interet_annuel
    print(f"Traite n° {annee} : {montant_traites:.2f} $ dont {interet_annuel:.2f} $ de TAEG ajouté")

    totaltraites += montant_traites
# Calcul du montant total à rembourser sur 10 ans
montant_total = totaltraites - emprunte
print(f"Cout total du crédit sur 10 ans est de : {montant_total:.2f}")


