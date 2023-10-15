#solution after correction
print("Welcome to Exam Grade Calculator")
print()
#declarion variables acces
name = input("Please, what's your name, Bobprof or Bobstudient ? ")
exam = input("what's Name of this day test ? ")
#conditions acces result exam
if exam == "day13" and name == "Bobprof" or name == "Bobstudient":
  #declaration variables float style
  Bobstudient= float(input("Hi Boby, it's all Ok! Give me your percent success score recived for this exercice ? "))
  #around 2 decimal
  Bobstudient= round(Bobstudient, 2)
  Bobprof= float(input("Now please, what's your percent satisfaction score give you for this exersice ? "))
  #around 2 decimal
  Bobprof= round(Bobprof, 2)
  #calcul moyenne around, decimal off 
  score = (Bobstudient + Bobprof) // 2
  #conditions result exam
  if (score >= 90):
    print("You got winned", score,"% which is a A+")
  elif (score >= 80):
    print("You got winned", score,"% which is a A")
  elif (score >= 70):
    print("You got winned", score,"% which is a B+")
  elif (score >= 60):
    print("You got winned", score,"% which is a B")
  elif (score >= 50):
    print("You got winned", score,"% which is a C+")
  elif (score >= 40):
    print("You got winned", score,"% which is a C")
  elif (score <= 40):
    print("Congrates you got D+ my friend !")
#End conditions acces result exam
else:
  print("You don't signed up program or you writing so bad,try again!")
   