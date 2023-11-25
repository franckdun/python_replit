#Nous allons construire un jeu de devinettes « Devinez le nombre ». Ce jeu consiste à choisir un nombre aléatoire entre 1 et 1000 et demander à l’utilisateur de le deviner. Lorsque l’utilisateur trouve le nombre, le jeu s’arrête.

#Le programme devra afficher le nombre de tentatives nécessaires pour trouver le nombre.

#Le programme devra demander à l’utilisateur s’il souhaite rejouer.

#Le programme devra s’arrêter lorsque l’utilisateur choisit de ne plus jouer.

#Le programme devra afficher le nombre de tentatives nécessaires pour trouver le nombre.

# Importation module random
import random
#déclaration variable nombre aléatoire.
nombre = random.randint(1,1000)
#déclaration variable tentatives.
tentatives = 0
#déclaration variable choix.
choix = ""
#déclaration variable boléene jouer.
jouer = True

#Instructions du jeu
print("Jeu du Nombre Mystère") 
print("Devinez un nombre entre 1 et 1000.")
print("Bonne chance !")

#boucle principale while
while jouer == True:
    #déclaration variable nombre aléatoire.
    nombre = random.randint(1,1000)
    #déclaration variable tentatives utilisateur.
    tentatives = 0
    #déclaration variable choix utilisateur.
    choix = ""
  
    #boucle principale while, tant que choix est différent du nombre alétoire. 
    while choix != nombre:
        #déclaration valeur de choix en int.
        #bloc try pour gérer les erreurs
        try:
          choix = int(input("\nDevinez le nombre : "))  
        except ValueError:
          print("Veuillez entrer un nombre valide.")
          continue
          
        # Incrémente nombre tentatives.
        tentatives += 1
      
        # Si choix inférieur au nombre.
        if choix < nombre:
            # Affiche nombre tentatives.
            print(f"Tentative n°{tentatives} C'est plus !")
          
        # Si choix supérieur au nombre.
        elif choix > nombre:
            print(f"Tentative n°{tentatives} C'est moins !")
        
        # Si choix égal au nombre.
        elif (choix == nombre):
            print("Bravo, vous avez trouvé en", tentatives, "tentatives ! ")
            print()
            # Demande si rejouer.
            print("Voulez-vous rejouer ? (o/n)")
            # Déclaration variable pour sortir.
            choix = input()
            # Si choix = o relance la boucle.
            if choix == "o":
                jouer = True
                # réinitialise tentatives
                tentatives = 0
          
            # Si choix = autre change valeur de jouer.
            else:
                jouer = False
                print("Merci d'avoir joué !")
