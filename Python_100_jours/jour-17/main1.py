#Une autre triche

#Jusqu'à présent, nous avons utilisé breakdans le while Trueboucle. breakquitte complètement la boucle et exécute la prochaine ligne de code non indentée. Cependant, vous souhaiterez peut-être arrêter le code et recommencer la boucle depuis le haut. (C'est idéal pour créer des jeux !)

#Dans le code ci-dessous, le jeu s'exécute et il est demandé à l'utilisateur s'il souhaite aller à gauche ou à droite. Si l'utilisateur choisit de partir, il tombe à mort et breakexpulsera l'utilisateur de la boucle. C'est le jeu.

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break

#Eh bien, c'est un peu nul et pas différent de ce que nous avons appris au jour 16... maintenant pour la triche.


