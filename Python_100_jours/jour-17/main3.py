#Erreurs courantes
#Corrigez les erreurs et appuyez sur run encore une fois jusqu'à ce que vous soyez sans erreur. 

#Erreur de nom

#👉 Quelle est l'erreur ici ?

counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

#while truedoit être while True.

#Remarquez que lorsque vous remplacez le « t » minuscule par un « T » majuscule, la couleur du mot change car Replit le reconnaît désormais comme une boucle booléenne.
#Erreur de syntaxe

#👉 Et celui-ci ? Que se passe-t-il lorsque vous frappez run?

counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

#Notez que le message d'erreur indique l'erreur de syntaxe "rupture en dehors de la boucle". Remarquez-vous comment les trois dernières lignes avant le bas printLes instructions ne font pas partie de la boucle car elles ne sont pas correctement indentées (regardez les lignes verticales) ?

#Mettez en surbrillance ces trois lignes de code et appuyez sur tab touchez une fois pour indenter ce code afin qu'il soit à l'intérieur de la boucle. 