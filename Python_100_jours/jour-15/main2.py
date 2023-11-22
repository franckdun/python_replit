#Quel animal veux-tu ? : Vache
#déclaration variabl
animal = input("Quel est cet animal, Mmeuh! ?")

if animal == "vache":
  print("Mmeuh! Bon choix")
else :
  print(animal, "ne sais pas faire, Mmeuh!")
  exit = " "
  
while exit != "vache":
  exit = input("Quel est cet animal, Mmeuh!,Mmeuhhh! ?")
  
#Une vache meugle.
#Voulez-vous sortir ? : non
#Quel animal voulez-vous ? : Un lémurien tacheté
#Ummm... le lémurien nain devient awooga.
#Voulez-vous sortir ? : oui
