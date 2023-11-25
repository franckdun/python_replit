#Lorsque l’utilisateur trouve le nombre, le jeu s’arrête.
#affiche le nombre de tentatives nécessaires pour trouver le nombre.
#demande à l’utilisateur s’il souhaite rejouer.
#Le programme s’arrête lorsque l’utilisateur choisit de ne plus jouer.
#affiche le nombre de tentatives nécessaires pour trouver le nombre.

# Importation module random
import random

#déclaration variable nombre aléatoire.
nombre = random.randint(1,1000)

#déclaration variable tentatives.
tentatives = 0

#déclaration variable choix.
choix = "" #valeur vide

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
    choix = "" #valeur vide
  
    #boucle principale while, (tant que) v.choix est différent de v.nombre alétoire. 
    while choix != nombre:
      
        #déclaration valeur de v.choix en int.
        #bloc try gére les erreurs
        try:
          choix = int(input("\nDevinez le nombre : "))
        #bloc except gére les exéptions
        except ValueError:
          print("Veuillez entrer un nombre valide.")
          #retour répétition boucle
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
            
            # Demande si rejouer.
            print(":\nVoulez-vous rejouer ? (o/n)")
            # Déclaration variable retour/sortir.
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
                break
print("Merci d'avoir joué !")