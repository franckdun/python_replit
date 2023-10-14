
# Ask the user for their name
nom_utilisateur = input("Salut ! Quel est ton nom ? ")

if nom_utilisateur == "Dave" or nom_utilisateur == "dave":
  print("Hi Dave !")
else:
  print("Hi !", nom_utilisateur)
  nouveau = input("tu es nouveau  dans le coin alors ?")
  if nouveau == "oui":
      print("alors enchanter de te rencontrer")
  elif nouveau == "non":
     print("ah bon! désolé je perd la mémoire")
  else:
     print("bizard ta réponse !")
   
# Ask the user for the current day of the week
jour_semaine = input("Quel jour est-ce aujourd'hui ? ")

# Ask for a few of the user's favorite things
activites_preferees = input("Que veux-tu faire aujourd'hui ? ")

# Convert the day of the week to lowercase for case-insensitive comparison
jour_semaine = jour_semaine.lower()

# Dictionary of activity for hitch day
if jour_semaine == "lundi":
  print(nom_utilisateur, "C'est un excellent jour pour;", activites_preferees,"mais va s'y molo on est que lundi.")
elif jour_semaine == "mardi":
  print("Bonne journée", nom_utilisateur, "! Le mardi est là, alors profite de", activites_preferees, ".")
elif jour_semaine == "mercredi":     print(nom_utilisateur, "! C'est mercredi, le jour parfait pour", activites_preferees,".")
elif jour_semaine == "jeudi":
  print(nom_utilisateur, "! Joyeux jeudi ! N'oublie pas de faire", activites_preferees,".")
elif jour_semaine == "vendredi":     print("Bonne journée",nom_utilisateur, "! C'est vendredi, tu devrais certainement faire", activites_preferees, ".")
elif jour_semaine == "samedi":       print(nom_utilisateur, " ! C'est samedi, le jour idéal pour", activites_preferees, ".")
elif jour_semaine == "dimanche" :
   print(nom_utilisateur, "! Passe une journée de dimanche relaxante avec", activites_preferees, ".")
else:
  print(nom_utilisateur, "je ne comprend pas ton charabia de",jour_semaine, ", mais", activites_preferees, "ça a l'air vraiment sympa.")

# Ask the user if they want an affirmation, joke, or insult
choix = input("Veux-tu une affirmation, une blague ou une insulte aujourd'hui ? ").lower()

# Generate the appropriate message based on the user's choice
if choix == "affirmation":
    print("Je ne peux pas générer une affirmation pour le jour", jour_semaine,". Essaye un jour valide.")
elif choix == "blague":
    print("Pourquoi l'ordinateur a-t-il eu froid ? Parce qu'il a la fenêtre ouverte !")
elif choix == "insulte":
    print("Désolé, je ne peux pas t'insulter. Je préfère répandre la positivité !")
else:
    print("Je ne comprends pas ta demande. Choisis entre affirmation, blague ou insulte sinon va te chercher un café pour te réveiller")



