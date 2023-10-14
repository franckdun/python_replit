commande = input("Que souhaitez-vous commander : une pizza ou un hamburger ? ")
if commande == "hamburger":
   print("Merci.")
   fromage = input("Voulez-vous du fromage ?")
   if fromage == "oui":
     print("bien, avec fromage.")
   else: 
     print("Ce n'est pas du fromage.")
elif commande == "pizza":
   print("bien, une pizza et...")
   garnitures = input("Voulez-vous du pepperoni dessus ?")
   if garnitures == "oui":
     print("bien, avec pepperoni")
   else:
     print("bien, Votre pizza       sans garnitures.")
else:
  print("désolé il n'y en a plus, il faut venir plutot")