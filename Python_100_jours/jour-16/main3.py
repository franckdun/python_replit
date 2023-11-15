#Erreurs courantes

#Tout d'abord, supprimez tout autre code de votre main.pydéposer. Copiez chaque extrait de code ci-dessous dans main.pyen cliquant sur l'icône de copie en haut à droite de chaque case de code. Ensuite, frappez runet voyez quelles erreurs se produisent. Corrigez les erreurs et appuyez sur runencore une fois jusqu'à ce que vous soyez sans erreur. Clique sur le 👀 Answerpour comparer votre code au bon code.
#Erreur de nom

#👉 Quelle est l'erreur ici ?

counter = 0
while true:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

while truedoit être while True.

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

#Mettez en surbrillance ces trois lignes de code et appuyez sur tabtouchez une fois pour indenter ce code afin qu'il soit à l'intérieur de la boucle. 