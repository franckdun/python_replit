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

    if dice == [4, 2, 1]:
        print("Gagné !")
    
  

def calculate_points(dice):
    """
    Calcule les points en fonction des résultats des dés.
    """
    return int(''.join(map(str, dice)))

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
    elif choice == "1 2":
        dice[0] = random.randint(1, 6)
        dice[1] = random.randint(1, 6)
    elif choice == "1 3":
        dice[0] = random.randint(1, 6)
        dice[2] = random.randint(1, 6)
    elif choice == "2 3":
        dice[1] = random.randint(1, 6)
        dice[2] = random.randint(1, 6)
      
    return sorted(dice, reverse=True)

def play_421():
    """
    Fonction principale pour jouer au jeu 421.
    """
    print("Bienvenue au jeu 421 !")

    total_points = 0  # Total des points du joueur
    num_turns = 0  # Nombre de tours joués

    while True:
        num_turns += 1  # Incrémenter le nombre de tours
        print(f"\nTour {num_turns} :")

        input("Appuie sur Entrée pour lancer les dés...")
        dice = roll_dice()
        display_dice(dice)

        points = calculate_points(dice)
        if points == 421:
            total_points += 1000
            print("\nFélicitations ! Tu as obtenu le 421 ! Tu as gagné 1000 points supplémentaires !")
        else:
            total_points == points
            print("Points obtenus :", points)

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
                print("Fin du tour.")

    print("Total des points :", total_points)

if __name__ == "__main__":
    play_421()
