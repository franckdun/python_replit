
print("PIERRE FEUILLE CISEAUX GAME")
print()
#Permet de faire une saisie inconito
from getpass import getpass as input
getpass = input("Choisisez votre mouvement, P F ou C ")

player1 = input("Choisisez votre mouvement, P F ou C ")
player2 = input("Choisisez votre mouvement, P F ou C ")

#Cas d'�galit�
if player1 == "P" and player2 == "P"
	print("�galit�")
elif player1 == "F" and player2 == "F"
	print("�galit�")
elif player1 == "C" and player2 == "C"
	print("�galit�")
	
#Cas gagnant player1
if player1 == "P" and player2 == "C"
	print("player1 Gagn�")
elif player1 == "F" and player2 == "P"
	print("player1 Gagn�")
elif player1 == "C" and player2 == "F"
	print("player1 Gagn�")
	
#Cas gagnant player2
if player1 == "P" and player2 == "F"
	print("player2 Gagn�")
elif player1 == "F" and player2 == "C"
	print("player2 Gagn�")
elif player1 == "C" and player2 == "P"
	print("player2 Gagn�")