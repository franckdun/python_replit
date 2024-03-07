import random

def roll_dice():
    """
    Simule le lancer de trois dés à six faces.
    Retourne une liste contenant les résultats des trois dés.
    """
    return [random.randint(1, 6) for _ in range(3)]

def display_dice(dice):
    """
    Affiche les résultats des dés.
    """
    print("Résultats des dés :", dice)

def calculate_points(dice):
    """
    Calcule les points en fonction des résultats des dés.
    """
    return sum(dice) * 111

def play_421_with_points():
    """
    Fonction principale pour jouer au jeu 421 avec un système de points.
    """
    print("Bienvenue au jeu 421 avec un système de points !")
    total_points = 0
    while True:
        input("Appuie sur Entrée pour lancer les dés...")
        dice = roll_dice()
        display_dice(dice)
        points = calculate_points(dice)
        total_points += points
        print("Points obtenus pour ce tour :", points)
        print("Total des points :", total_points)
        if dice == [4, 2, 1]:
            print("Félicitations ! Tu as obtenu le 421 !")
            break
        else:
            print("Dommage, tu n'as pas obtenu le 421. Essaye encore !")

if __name__ == "__main__":
    play_421_with_points()
