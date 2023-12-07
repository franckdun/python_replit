# Calculateur de prêt indiquant le montant à rembourser pour un prêt de 1 000 $ avec un TAEG de 5 % sur 10 ans.

# Demander le montant à emprunter sur 10 ans
emprunte = int(input("Combien souhaitez-vous emprunter sur 10 ans ? "))

# Calcul du TAEG
taux = 0.05 # 5% de l'empreint


# Calcul du coût du crédit sur 10 ans
ans = 10 # nombre d'années
payement = emprunte / ans # calcul du montant pour une années

# Calcul du montant à rembourser la 1re année, TAEG à 0 %
print(f"Traite n° 1 : {payement:.2f}")

# Boucle for pour calculer le montant de chaque traite sur 10 ans
total_interet = 0
totaltraites = 0
for annee in range(2, ans + 1): #pour chaque annee dans la liste.la liste traite de 1 ans à 10 ans mais en commençant à 2 (car sans la traite de base)
    interet = payement * taux # interet calculé a chaque tour avec la nouvelle valeur de payement foix le taux
    payement += interet # 100 + 5 = 105 on ajoute a chaque tour de boucle
    total_interet += interet # a chaque tour on ajoute le montant de l'interet à la somme total des interets
    print(f"Payement n° {annee} : {payement:.2f} $ dont TAEG {interet:.2f} $")

    totaltraites += payement #total des payements
# Calcul du montant des intérets sur 10 ans
totalinteret = totaltraites - emprunte
print(f"Cout total crédit : emprunt {emprunte} interets {totalinteret:.2f} total {totaltraites:.2f} $")


