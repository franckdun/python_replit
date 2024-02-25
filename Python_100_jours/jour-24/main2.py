def whichCake(ingredient):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
    

whichCake(input("What is your favorite cake?"))

whichCake(input("sinon un autre choix de favorite cake ?"))

whichCake(input("Encore un dernier choix ?")) 

#un autre exercice sur la meme page 
"""
def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  else:
    print(number2, "is bigger")

biggerNumber (18, 33)
"""
#un autre exercice sur la meme page 
"""
def pizza_order(garniture1, garniture2):
  if garniture1 == "pepperoni" or "anchoix" :
    print(garniture1, "est un excellent choix")
  else:
    print(garniture1, " y en a plus, prenez autre chose ")
  print(garniture2, "ça a l'air délicieux, bien meilleur que", garniture1)
  
garniture1 =  input("Nommer une garniture de pizza ")
garniture2 = input("Nommez une deuxième garniture de pizza. ")

pizza_order(garniture1, garniture2)

"""