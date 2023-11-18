#Erreurs courantes

#Tout d'abord, supprimez tout autre code de votre main.pydéposer. Copiez chaque extrait de code ci-dessous dans main.pyen cliquant sur l'icône de copie en haut à droite de chaque case de code. Ensuite, frappez runet voyez quelles erreurs se produisent. Corrigez les erreurs et appuyez sur runencore une fois jusqu'à ce que vous soyez sans erreur. Clique sur le ?? Answerpour comparer votre code au bon code.

#?? Qu'est-ce qui ne va pas ici ?

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit
print("The game is over, you've failed!")

#exitest une fonction et des besoins (). Au moment où vous ajoutez le ()vous remarquez le changement de couleur de exitdu blanc au jaune.

while True:
  print("You are in a coridoor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit ()
print("The game is over, you've failed!")