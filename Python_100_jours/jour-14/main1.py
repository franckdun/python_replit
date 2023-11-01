#👉 Jour 14 Défi

print("PIERRE FEUILLE CISEAUX GAME")
print()
exam = input("Choisisez votre mouvement, P F ou C ")
Player1 = input("jour 1 , Quel est votre choix de mouvement ? ")
Player2 = input("jour 2 , Quel est votre choix de mouvement ? ")

if exam == "python" and name == "Bob":
  if (score >= 90):
    print("you got", score,"% which is a A")
  elif (score >= 80):
    print("you got", score,"% which is a A-")
  elif (score >= 70):
    print("you got", score,"% which is a B")
  elif (score >= 60):
    print("you got", score,"% which is a B-")
  elif (score >= 50):
    print("you got", score,"% which is a C")
  elif (score >= 40):
    print("you got", score,"% which is a C-")
  else:
    print("dont worry, you can replay exam")
else:
  print("you don't sign up to this program")

