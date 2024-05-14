import random

# Constantes
TARGET_SCORE = 666  # Score cible
DEFAULT_CHARACTERISTICS = [
    "Life", "Power", "Protect", "Regen", "Ward", "Chance", "Spell", "Metamorphose"
]

# Codes de couleur ANSI
COLOR_RED = '\033[91m'
COLOR_YELLOW = '\033[93m'
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'


def display_dice_and_score(dice, characteristics):
    """Affiche les résultats des dés, les caractéristiques et le score."""
    print("\n",
          "  ".join([f"Dé {i + 1} -> {dice[i]}" for i in range(len(dice))]),
          "\n")
    score = sum(dice)
    print("Caractéristiques du personnage :")
    for i, char in enumerate(characteristics):
        color = COLOR_RESET
        if dice[i] > 5:
            color = COLOR_YELLOW
        elif dice[i] > 3:
            color = COLOR_RED
        elif dice[i] <= 3:
            color = COLOR_GREEN
        print(f"{char}: {color}{dice[i]}{COLOR_RESET}")
    print("\nNombre Sxb obtenu -> ", convert_dice_to_number(dice), "\n")
    print("Valeur carte : ", score, "Manas\n")
    return score


def convert_dice_to_number(dice):
    """Convertit les résultats des dés en un nombre entier."""
    return int(''.join(map(str, dice)))


def roll_dice(num_dice, num_faces):
    """Simule le lancer de dés avec un nombre donné de dés et de faces."""
    return sorted([random.randint(0, num_faces) for _ in range(num_dice)],
                  reverse=True)


def reroll_dice(dice, choices, num_faces):
    """Permet au joueur de relancer les dés sélectionnés."""
    for choice in choices:
        if choice in range(1, len(dice) + 1):
            dice[choice - 1] = random.randint(1, num_faces)
    return sorted(dice, reverse=True)


def get_user_input(prompt, valid_options):
    """Obtient une entrée valide de l'utilisateur."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Entrée invalide. Veuillez réessayer.")


def play_turn(num_dice, num_faces, characteristics):
    """Effectue un tour de jeu."""
    input("Appuie sur entrée pour lancer les dés.. ")
    dice = roll_dice(num_dice, num_faces)
    score = display_dice_and_score(dice, characteristics)
    return dice, score


def play_007():
    """Fonction principale pour jouer au jeu."""
    total_score = 0
    num_turns = 0

    print("Générateur de carte personnage.")

    num_dice = int(input("Définir le nombre dés de capacités? "))
    print("Définir le nombre de faces augmente les valeurs des capacités")
    print("la valeur de la carte en Manas")
    num_faces = int(input("Combien de faces chaque dé de capacité aura-t-il? "))
    print("\n", num_dice, "dés de caracteristiques vont générer des valeurs de 0 a", num_faces)

    print("\nDéfinissez maintenant les caractéristiques de votre personnage :\n")
    character_name = input("Nom du personnage? ")

    characteristics = []
    for i in range(num_dice):
        characteristic_name = input(f"Nom de la caractéristique n°{i + 1} ? (nom par défaut avec Entrée): ")
        if not characteristic_name:
            characteristic_name = DEFAULT_CHARACTERISTICS[i % len(DEFAULT_CHARACTERISTICS)]
        characteristics.append(characteristic_name)
        print(f"Caractéristique {i + 1}: {characteristic_name}")

    print("\nDébut du jeu...\n")

    while True:
        num_turns += 1
        print(f"Generate << {character_name} >> N°{num_turns}\n")
        dice, score = play_turn(num_dice, num_faces, characteristics)
        total_score += score

        if convert_dice_to_number(dice) == TARGET_SCORE:
            print(f"Félicitations ! {character_name} as obtenu la carte {TARGET_SCORE} niveau Légende, puissante!")
            break

        choices = input(
            "Quels dés voulez-vous relancer pour modifier les valeur des capacités ? (séparez vos choix par un espace, 'all' pour tous les dés, 'q' pour quitter): "
        ).split()

        if "all" in choices:
            # relance tous les dés aléatoirement
            dice = roll_dice(num_dice, num_faces)

        if 'q' in choices:
            print("\nFin du jeu. Merci d'avoir joué !")
            break

        dice = reroll_dice(
            dice, [int(choice) for choice in choices if choice.isdigit()],
            num_faces)
        score = display_dice_and_score(dice, characteristics)
        total_score += score

        if convert_dice_to_number(dice) == TARGET_SCORE:
            print(f"Félicitations ! {character_name} as obtenu la carte {TARGET_SCORE} la plus rare !")
            break

    print(f"\nScore valeur Mana création: {total_score}, nombre de générations : {num_turns}")


if __name__ == "__main__":
    play_007()
