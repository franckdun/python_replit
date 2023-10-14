gdg = int(input("Pour connaitre quel est votre Génération, entrez votre année de naissance ?"))
if gdg <= 1925 :
  print("impossible de savoir")
elif gdg <= 1946 :
  print("Les traditionalistes")
elif gdg <= 1964 :
  print("Les Baby-Boomers")
elif gdg <= 1981 :
  print("La Génération X")
elif gdg <= 1995 :
  print("Millenials")
elif gdg <= 2015 :
  print("La Génération Z ")
else :
  print("imposible de savoir")