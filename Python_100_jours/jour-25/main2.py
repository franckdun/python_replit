import random

# Constantes
TARGET_SCORE = 421  # Score cible


def display_dice_and_score(dice, characteristics):
    """Affiche les résultats des dés, les caractéristiques et le score."""
    print("\n",
          "  ".join([f"Dé {i + 1} -> {dice[i]}" for i in range(len(dice))]),
          "\n")
    score = sum(dice)
    print("Caractéristiques du personage :")
    for i, char in enumerate(characteristics):
        print(f"{char}: {dice[i]}")
    print("\nNombre Sxb obtenu -> ", convert_dice_to_number(dice), "\n")
    print("Score : +", score, "points\n")
    return score


def convert_dice_to_number(dice):
    """Convertit les résultats des dés en un nombre entier."""
    return int(''.join(map(str, dice)))


def roll_dice(num_dice, num_faces):
    """Simule le lancer de dés avec un nombre donné de dés et de faces."""
    return sorted([random.randint(1, num_faces) for _ in range(num_dice)],
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

    print(
        "Bienvenue dans le générateur de statistiques pour un personnage de jeu vidéo."
    )
    print(
        "Vous allez créer un personnage en attribuant des valeurs à différents paramètres."
    )

    num_dice = int(input("Combien de dés souhaitez-vous utiliser ? "))
    num_faces = int(input("Combien de faces chaque dé aura-t-il ? "))
    print("Les dés vont générer des valeurs entre 1 et", num_faces)

    print("\nDéfinissez maintenant les caractéristiques de votre personnage :")
    character_name = input("Nom du personnage : ")

    characteristics = []
    for i in range(num_dice):
        characteristic_name = input(f"Nom de la caractéristique {i+1} : ")
        characteristics.append(characteristic_name)
        print(f"Caractéristique {i+1}: {characteristic_name}")

    print("\nDébut du jeu...\n")

    while True:
        num_turns += 1
        print(f"<<<<< TOUR {num_turns} >>>>>\n")
        dice, score = play_turn(num_dice, num_faces, characteristics)
        total_score += score

        if convert_dice_to_number(dice) == TARGET_SCORE:
            print(
                f"Félicitations ! Tu as obtenu exactement {TARGET_SCORE} tu as gagné !"
            )
            break

        choices = input(
            "Quels dés voulez-vous relancer ? (séparez vos choix par un espace, 'all' pour tous les dés, 'q' pour quitter): "
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
            print(
                "Félicitations ! Tu as obtenu exactement 421 TU EST EN PLEINE FORME !"
            )
            break

    print(f"\nScore total: {total_score}, Tours joués: {num_turns}")


if __name__ == "__main__":
    play_007()
