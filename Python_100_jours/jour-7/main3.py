print ("Êtes-vous un superfan de 'The Big Bang Theory' ou un faux fan ?")
print ()
print("Répondez à ces questions pour le savoir.")

Lunettes = input("Est-ce que quelqu'un porte des lunettes ?")
if Lunettes == "oui":
   print("Correct!")
else:
   print("Faux!")
   WhoGlasses = input("Et qui porte des lunettes ?")
   if WhoGlasses == "Léonard":
     print("Vous l'avez compris")
   else:
     print("Réessayez!")