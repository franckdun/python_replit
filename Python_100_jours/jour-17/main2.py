#La commande Continuer

#Le continue La commande arrête l’exécution du code dans la boucle et recommence en haut de la boucle. Essentiellement, nous voulons ramener l'utilisateur à la question initiale.

#Ajouter continue va relancer le code depuis le début et poser à nouveau la première question : "Allez-vous à gauche ou à droite ?".

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

#Le else L'instruction fait référence à toute entrée autre que gauche ou droite (haut ou échap). Puisque l'utilisateur est gagnant, nous ne voulons pas utiliser break ou cela dirait qu'ils ont échoué.

#Alors comment faire pour que ça s'arrête ? 