#jeu de test mathématique
#le joueur doit répondre à des questions sur une table de mathématique qu'il choisit
#le joueur a un score qui est affiché à la fin du jeu

#déclaration des variables
table = int(input("Quelle table de multiplication voulez-vous réviser ? "))
score = 0
for i in range(1, 11):
  print(i, "x", table, "= ")
  reponse = int(input(""))
  if reponse == i * table:
    print("Bravo !")
    score += 1
  else:
    print("Mauvaise réponse. La réponse était", i * table)
print("Votre score est de", score, "sur 10")