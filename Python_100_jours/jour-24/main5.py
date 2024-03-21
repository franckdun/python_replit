import random

def roll_dice():
    """
    Simule le lancer de trois dés à six faces.
    Retourne une liste contenant les résultats des trois dés.
    """
    return sorted([random.randint(1, 6) for _ in range(3)], reverse=True)

def display_dice(dice):
    """
    Affiche les résultats des dés.
    """
    print("Résultats des dés :", dice)

def calculate_points(dice):
    """
    Calcule les points en fonction des résultats des dés.
    """
    return int(''.join(map(str, dice)))

def reroll_dice(dice, choice):
    """
    Permet au joueur de relancer les dés sélectionnés pour améliorer le score.
    """
    if choice == "all":
        return roll_dice()
    elif choice == "1":
        dice[0] = random.randint(1, 6)
    elif choice == "2":
        dice[1] = random.randint(1, 6)
    elif choice == "3":
        dice[2] = random.randint(1, 6)
    return sorted(dice, reverse=True)

def play_421_with_points_and_rerolls():
    """
    Fonction principale pour jouer au jeu 421 avec un système de points et la possibilité de relancer des dés.
    """
    print("Bienvenue au jeu 421 avec un système de points et des relances de dés !")
    total_points = 0
    while True:
        input("Appuie sur Entrée pour lancer les dés...")
        dice = roll_dice()
        display_dice(dice)
        points = calculate_points(dice)
        if points == 421:
            total_points += 1000
            print("Félicitations ! Tu as obtenu le 421 ! Tu as gagné 1000 points supplémentaires !")
        else:
            total_points += points
            print("Points obtenus pour ce tour :", points)
        print("Total des points :", total_points)
        if points == 421:
            break
        else:
            reroll_choice = input("Veux-tu relancer tous les dés (all) ou un dé spécifique (1, 2 ou 3) ? (all/1/2/3) : ")
            dice = reroll_dice(dice, reroll_choice)
            display_dice(dice)

if __name__ == "__main__":
    play_421_with_points_and_rerolls()
