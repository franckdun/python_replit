#Tout d’abord, supprimez tout autre code de votre fichier main.py.  Copiez chaque extrait de code ci-dessous dans main.py en cliquant sur l'icône de copie en haut à droite de chaque zone de code.  Ensuite, cliquez sur Exécuter et voyez quelles erreurs se produisent.  Corrigez les erreurs et appuyez à nouveau sur Exécuter jusqu'à ce que vous n'ayez plus d'erreur.  Cliquez sur la Réponse pour comparer votre code au bon code.

print("100 Days of Code QUIZ")
print("How many can you answer correctly")
print()
ans1 = input("What language are we writing in ?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope!")
print()
ans2 = int(input("Which lesson number is this?"))
if (ans2 > 12):
  print("We're not quite that far yet")
elif (ans2 == 12):
  print("That's right!")
else:
  print("We've gone well past that!")

