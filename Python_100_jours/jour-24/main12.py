import random

def roll_dice():
    """
    Simule le lancer de trois dés à six faces.
    Retourne une liste contenant les résultats des trois dés, triés du plus grand au plus petit.
    """
    return sorted([random.randint(1, 6) for _ in range(3)], reverse=True)

def display_dice_and_score(dice):
    """
    Affiche les résultats des dés et le score du joueur.
    """
    print("\nDé1 =", dice[0], "\nDé2 =", dice[1], "\nDé3 =", dice[2])

    print("\nRésultats des dés auto_rangés :", convert_dice_to_number(dice))
    score = sum(dice)
    print("Point obtenu :", score)
    return score

def convert_dice_to_number(dice):
    """
    Convertit les résultats des dés en un nombre entier.
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
    print("Pour gagner, obtiens 421 avec les dés ou fais le meilleur score en moins de tours possibles.")

    total_score = 0  # Score total du joueur
    num_turns = 0  # Nombre de tours joués

    while True:
        num_turns += 1  # Incrémenter le nombre de tours
        print(f"\nTour {num_turns} :")
        print("Pour quitter, tapez 'q' ou 'Q' à tout moment.\n")

        input("Appuie sur Entrée pour lancer les dés...\n")
        dice = roll_dice()  # Lancer les dés
        current_score = display_dice_and_score(dice)  # Afficher les résultats des dés et le score du joueur

        total_score += current_score  # Ajouter le score du tour au score total

        print("\nScore total:", total_score, "Nombre de Tours:", num_turns)  # Afficher le score total du joueur et le nombre de tours

        if current_score == 421 or convert_dice_to_number(dice) == 421:
            print("\nFélicitations ! Tu as obtenu le 421 ! Tu as gagné 1000 points supplémentaires !")
            total_score += 1000  # Ajouter 1000 points supplémentaires pour avoir obtenu 421

        print("\nRelancer tous les dés (all) ou certains seulement ?")
        print("Pour quitter, tapez 'q' ou 'Q'.\n")

        reroll_choice = input("Quel dé veux-tu relancer ? (all/1/2/3/1 2/1 3/2 3) : ")

        if reroll_choice.lower() == "q":
            print("Fin du jeu. Merci d'avoir joué !")
            break

        if reroll_choice in ["all", "1", "2", "3", "1 2", "1 3", "2 3"]:
            dice = reroll_dice(dice, reroll_choice)
            current_score = display_dice_and_score(dice)  # Afficher les nouveaux résultats des dés et le score du joueur

    # Afficher le nombre de tour total
    print(f"\nNombre total de tours : {num_turns}")
    print("Score final :", total_score)

if __name__ == "__main__":
    play_421()
