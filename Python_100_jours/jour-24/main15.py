import random

# Constantes
NUM_DICE = 3
TARGET_SCORE = 421

def display_dice_and_score(dice):
    """Affiche les résultats des dés et le score."""
    print("\nDés:", "  ".join([f"{i+1} > {dice[i]}" for i in range(NUM_DICE)]))
    score = sum(dice)
    print("Nombre créé:", convert_dice_to_number(dice))
    print("Score pour ce tour:", score, "points")
    return score

def convert_dice_to_number(dice):
    """Convertit les résultats des dés en un nombre entier."""
    return int(''.join(map(str, dice)))

def roll_dice():
    """Simule le lancer de trois dés à six faces."""
    return sorted([random.randint(1, 6) for _ in range(NUM_DICE)], reverse=True)

def reroll_dice(dice, choices):
    """Permet au joueur de relancer les dés sélectionnés."""
    for choice in choices:
        if choice in range(1, NUM_DICE + 1):
            dice[choice - 1] = random.randint(1, 6)
    return sorted(dice, reverse=True)

def play_turn():
    """Effectue un tour de jeu."""
    print("< NOUVEAU TOUR >")
    input("Appuie sur Entrée pour lancer les dés...")
    dice = roll_dice()
    score = display_dice_and_score(dice)
    return dice, score

def play_421():
    """Fonction principale pour jouer au jeu 421."""
    total_score = 0
    num_turns = 0
    
    print("Bienvenue au jeu 421 ! Pour gagner, obtiens 421 avec les dés ou fais le plus de points possible.\n")
    
    while True:
        num_turns += 1
        print(f"--- TOUR {num_turns} ---")
        dice, score = play_turn()
        total_score += score
        
        if score == TARGET_SCORE:
            print("Félicitations ! Tu as obtenu exactement 421 et gagné le jeu !")
            break
        
        choices = input("Quels dés veux-tu relancer ? (séparés par des espaces, 'all' pour tous, 'q' pour quitter): ").split()
        
        if 'q' in choices:
            print("Fin du jeu. Merci d'avoir joué !")
            break
        
        dice = reroll_dice(dice, [int(choice) for choice in choices if choice.isdigit()])
        score = display_dice_and_score(dice)
        total_score += score

    print(f"\nScore total: {total_score}, Tours joués: {num_turns}")

if __name__ == "__main__":
    play_421()
