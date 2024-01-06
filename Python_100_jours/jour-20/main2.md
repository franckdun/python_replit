Essayons-le

Le premier nombre de cette plage, 100, est la valeur de départ. Le deuxième nombre de cette plage, 110, est la valeur de fin (n'oubliez pas de toujours mettre le nombre de fin à un de plus que l'endroit où vous voulez finir).

👉 Quel numéro le code sera-t-il exécuté en premier ? Quel numéro sera le dernier ? Runle code et découvrez-le.

for i in range(100, 110):
  print(i)
  
run:
  
100
101
102
103
104
105
106
107
108
109

👉 Qu'espérez-vous imprimer avec la gamme ci-dessous ? Runet découvrir.

for i in range(1, 7):
  print("Day", i)
 
run:
 
Day 1
Day 2
Day 3
Day 4
Day 5
Day 6

Avez-vous remarqué que le compteur s'est arrêté au « Jour 6 » ? Modifiez la valeur de fin pour qu'elle soit un de plus que le dernier nombre que vous souhaitez afficher --- dans ce cas, 8 car nous voulons afficher 7 jours de la semaine.

for i in range(1, 8):
  print("Day", i)

👉 Que se passe-t-il lorsque vous runce code ?

print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)
  
run:

Thirteen Times Table
1 x 13 = 13
2 x 13 = 26
3 x 13 = 39
4 x 13 = 52
5 x 13 = 65
6 x 13 = 78
7 x 13 = 91
8 x 13 = 104
9 x 13 = 117
10 x 13 = 130
11 x 13 = 143
12 x 13 = 156

Ajoutons des incréments à notre gamme. 