import random

def roll_dice():
    """
    Simule le lancer de trois dés à six faces.
    Retourne une liste contenant les résultats des trois dés, triés du plus grand au plus petit.
    """
    return sorted([random.randint(1, 6) for _ in range(3)], reverse=True)

def display_dice(dice):
    """
    Affiche les résultats des dés.
    """
    print("\nRésultats des dés :", dice)
    # le résultat des dés = la somme des dés
    print("Points obtenus :", sum(dice))
  
    #print("Points obtenus :", points)
    

    if dice == [4, 2, 1]:
        print("Gagné !")
    
  

def convertice(dice):
    """
    Calcule les points en fonction des résultats des dés.
    """
    return int(''.join(map(str, dice)))#convertir la liste en chaine de caractères pour pouvoir la convertir en entier

def reroll_dice(dice, choice):
    """
    Permet au joueur de relancer les dés sélectionnés pour améliorer son score.
    """
    if choice == "all":
        return roll_dice()
    elif choice == "1":
        dice[0] = random.randint(1, 6)
    elif choice == "2":
        dice[1] = random.randint(1, 6)
    elif choice == "3":
        dice[2] = random.randint(1, 6)
    elif choice == "1 2":#si le joueur choisi 1 et 2
        dice[0] = random.randint(1, 6)
        dice[1] = random.randint(1, 6)
    elif choice == "1 3":
        dice[0] = random.randint(1, 6)
        dice[2] = random.randint(1, 6)
    elif choice == "2 3":
        dice[1] = random.randint(1, 6)
        dice[2] = random.randint(1, 6)
      
    return sorted(dice, reverse=True)#retourne la liste des dés triés du plus grand au plus petit

def play_421():
    """
    Fonction principale ;
      - présentation
      - demande de lancer les dés
      - affichage des résultats des dés
      - calcul des points
    """
    print("Pour gagner au jeu 421 !")
    print("Obtenir 421 avec les dés ou faire un score 421 en moins de tours posible.")

    nombre = 0  #  chiffre obtenu a partir des dés
    num_turns = 0  # Nombre de tours joués

    while True:#boucle infinie tan que le joueur ne gagne pas
        num_turns += 1  # Incrémenter le nombre de tours
        print(f"\nTour {num_turns} :")

        input("Appuie sur Entrée pour lancer les dés...")
        dice = roll_dice()#lancer les dés
        display_dice(dice)#afficher les résultats des dés

        points = convertice(dice)
        if points == 421:
            nombre += 1000
            print("\nFélicitations ! Tu as obtenu le 421 ! Tu as gagné 1000 points supplémentaires !")
        else:
            nombre == sum(dice)
            print("chiffre obtenu :", points)

        #print("Total des points :", total_points)

        if points == 421:
            break
        else:
            reroll_choice = input("\nVeux-tu relancer tous les dés (all) ou un dé spécifique (1, 2 ou 3) ? (all/1/2/3) sinon appuie sur Entrée : ")
            if reroll_choice in ["all", "1", "2", "3", "1 2", "1 3", "2 3"]:
                dice = reroll_dice(dice, reroll_choice)
              
                display_dice(dice)
            elif dice == [4, 2, 1]:
                print("Gagné !")
          
            else:
                display_dice(dice)
              #afficher les résultats des dés
              # affiche le score total du joueur pour ce tour
                points == sum(dice)
                print("Score :", sum(points), "points")
                print("Fin du tour.")
 
  
    #print("Total des points :", total_points)

if __name__ == "__main__":
    play_421()
