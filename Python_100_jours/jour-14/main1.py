#présentation du jeu
print("PIERRE FEUILLE CISEAUX GAME")
print()
print("les mouvement posibles sont; p pour pierre, f pour feuille et c pour ciseaux, puis faite entrer")
print()

#Permet de faire une saisie inconito
from getpass import getpass as input

#déclaration des variables
player1 = input("Player1 Quel est votre mouvement ?")
score1 = score1 + 0
player2 = input("Player2 Quel votre mouvement ?")
score2 = score2 + 0
print()

#Cas d'égalité
if player1 == "p" and player2 == "p":
  print("pierre contre pierre, égalité !")
elif player1 == "f" and player2 == "f":
  print("feuille contre feuille, égalité !")
elif player1 == "c" and player2 == "c":
  print("ciseaux contre ciseaux, égalité !")

#Cas gagnant player1
elif player1 == "p" and player2 == "c":
  print("pierre bat le ciseaux, player1 Gagné !")
  score1 = score1 + 1
elif player1 == "f" and player2 == "p":
  print("feuille bat la pierre, player1 Gagné !")
  score1 = score1 + 1
elif player1 == "c" and player2 == "f":
  print("ciseaux bat la feuille, player1 Gagné !")
  score1 = score1 + 1

#Cas gagnant player2
elif player1 == "p" and player2 == "f":
  print("feuille bat la pierre, player2 Gagné !")
  score2 = score2 + 1
elif player1 == "f" and player2 == "c":
  print("ciseaux bat la feuille, player2 Gagné !")
  score2 = score2 + 1
elif player1 == "c" and player2 == "p":
  print("pierre bat le ciseaux, player2 Gagné !")
  score2 = score2 + 1
else:
  print("je n'ai pas compris, recommencé")
  
#déclaration des variables
player1 = input("Player1 Quel est votre mouvement ?")
score1 = score1 
player2 = input("Player2 Quel votre mouvement ?")
score2 = score2 
print()