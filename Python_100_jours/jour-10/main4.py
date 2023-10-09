myBillHTT = float(input("What was the bill?: "))
tip = int(input("what was the tip pourcentage on the bill?"))
cotientPart = myBillHTT/100
tip2 = cotientPart * tip
tip2 = round(tip2, 2)
myBillTTC = myBillHTT + tip2
print("mais ça fait TTC", myBillTTC,"€", "dons", tip2,"€ de pourboire" )
numberOfPeople = int(input("How many people?: "))
answer = myBillTTC / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
