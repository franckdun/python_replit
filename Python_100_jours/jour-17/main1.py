#👉 Jour 13 Défi
#Grade Générateur

#Ce projet va prendre un certain temps (et à la rigueur de la pensée) mais ne sera pas brillant une fois que vous avez travail!

#Vous allez demander à l'utilisateur de taper le nom d'un test, le score maximum qu'ils peuvent recevoir, et combien de points ils ont reçu. Par exemple, le test pourrait être appelé "Python" de Compétences et le score maximum est de 50 points, l'utilisateur reçoit 30 points 50 points possibles.

print("Exam Grade Calculator")
print()
exam = input("what is Name of exam ? ")
name = input("what is your name ? ")
if exam == "python" and name == "Bob":
  number = float(input("hi! bob, what is your Score ? "))
  number = round(number, 2)
  score = number*2 // 1
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

