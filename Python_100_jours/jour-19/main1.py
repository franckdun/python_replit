#Calculateur de prêt indiquant le montant que vous devez pour un prêt de 1 000 $ avec un TAEG de 5 % (TAEG pour taux annuel en pourcentage) sur 10 ans.

#chaque année, le montant a devoir augmente de 5 %.

#calcule du coup du credits sur 10 ans.

#combien voulez-vous empreinter sur 10 ans ?
empreint = int(input("Combien voulez-vous empreinter sur 10 ans ? "))
ta = empreint /100
taeg = ta * 5
print("Votre TAEG est de : ", taeg / 1000)

coup = empreint/ 10
print("Votre coup du credits sur 10 ans est de : ", coup)
#boucle for pour calculer le montant du coup du credits sur 10 ans a payer par an.

for counter in range(10):
    
    an = counter + 1
    interet = coup * 0.05
    coup = coup + coup * 0.05
    interet = coup * 0.05
    print("Traite n°", an, ": ", coup, "dons", interet, "€" )
  
#total intérêt annuel sur 10 ans.
total = interet * 10
print("Total intérêt annuel sur 10 ans : ", total)

#calcule du montant du coup du credits sur 10 ans.
montant = coup * 10 - empreint
print("Votre montant est de : ", montant)
