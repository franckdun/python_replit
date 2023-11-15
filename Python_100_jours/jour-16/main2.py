#Arrête ça

#Il existe un moyen d'arrêter la boucle avec le mot break. Cela quitte la boucle et arrête tout le code à ce stade. Même s'il y a plus de code écrit après breakc'est à l'intérieur de la boucle.

#Après break, l'ordinateur sort de la boucle et passe à la non indentée suivante. ligne de code

#👉 Essayons-le

#Runle code ci-dessous et remarquez comment la boucle continuera jusqu'à break. Ensuite, la ligne suivante de code non indenté sera exécutée.

while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I 