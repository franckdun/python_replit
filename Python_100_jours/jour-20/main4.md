Erreurs courantes

Tout d'abord, supprimez tout autre code de votre main.pydéposer. Copiez chaque extrait de code ci-dessous dans main.pyen cliquant sur l'icône de copie en haut à droite de chaque case de code. Ensuite, frappez runet voyez quelles erreurs se produisent. Corrigez les erreurs et appuyez sur runencore une fois jusqu'à ce que vous soyez sans erreur. Clique sur le 👀 Answerpour comparer votre code au bon code.

for i in range (10, 0):
  print(i)
  
solution:

for i in range (10, 0, -1):
  print(i)

La troisième valeur du rangela fonction, incrément, est manquante. Il faut ajouter un incrément de -1faire marche arrière. Sans l'incrément écrit, l'ordinateur applique la valeur par défaut de +1.

Sans l'incrément indiqué, nous disons à l'ordinateur : "commencez à 10, continuez jusqu'à 0 et ajoutez-en un à chaque fois". Cela ne peut pas être fait, donc rien ne fonctionnera à moins que nous ajoutions un incrément.

