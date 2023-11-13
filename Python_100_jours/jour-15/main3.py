# Message d'introduction 
print("Bienvenue dans ce programme de devinette, pour sortir fait exit")
# Déclaration des variables
animal = input("3 chances, Quel animal fait Mmeuh! ?")
counter = 1
# Boucle while pour permettre plusieurs tentatives
while animal != "vache" and counter != 3 and animal != "exit" :
  print("essais", counter, ";")
  print("Non!", animal, "ne sais pas faire, Mmeuh!")
  counter = counter + 1
  animal = input("Quel est cet animal, Mmeuh!,Mmeuhhh!")
  #condition de sortie de boucle while
  if animal == "vache" :
     print("Mmeuh! Bon choix ! La vache meugle.")

  elif animal == "exit" :
    print("essais", counter, ";")
    print("Quoi! On s'arrête déjà!")
    
  elif counter == 3 :
     print("essais", counter, ";")
     print("Perdu, plus de chances !")
     
  

