#Quel animal veux-tu ? : Vache
#déclaration variabl
animal = input("3 chances, Quel animal ? fait 'Mmeuh!'")
counter = 1
if animal == "vache" :
  print("Mmeuh! Bon choix")
elif animal != "vache":
  exit = " "
  while exit != "vache" :
    print("essais1 ;", animal, "ne sais pas faire, Mmeuh!")
    exit = input("Quel est cet animal, Mmeuh!,Mmeuhhh!")
    counter += 1
    print("essais", counter)
    if counter == 3 :
      print("Tu n'as pas trouvé l'animal en 3 essais, Mmeuh! dit la vache")
      exit = "vache"
      
    
#Une vache meugle.
#Voulez-vous sortir ? : non
#Quel animal voulez-vous ? : Un lémurien tacheté
#Ummm... le lémurien nain devient awooga.
#Voulez-vous sortir ? : oui
