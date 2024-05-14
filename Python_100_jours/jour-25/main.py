import random

# Constantes
NUM_DICE = 3 # Nombre de dés
X = 6 # Nombre de facés d'un dé
TARGET_SCORE = X * NUM_DICE # Score cible

def display_dice_and_score(dice):
  """Affiche les résultats des dés et le score."""
  print("\n", "  ".join([f"Dé {i+1} -> {dice[i]}" for i in range(NUM_DICE)]),
        "\n")
  score = sum(dice)
  print("Nombre Sxb obtenu -> ", convert_dice_to_number(dice), "\n")
  print("Score : +", score, "points\n")
  return score


def convert_dice_to_number(dice):
  """Convertit les résultats des dés en un nombre entier."""
  return int(''.join(map(str, dice)))


def roll_dice():
  """Simule le lancer de trois dés à six faces."""
  return sorted([random.randint(1, X) for _ in range(NUM_DICE)], reverse=True)


def reroll_dice(dice, choices):
  """Permet au joueur de relancer les dés sélectionnés."""
  for choice in choices:
    if choice in range(1, NUM_DICE + 1):
      dice[choice - 1] = random.randint(1, X)
  return sorted(dice, reverse=True)


def play_turn():
  """Effectue un tour de jeu."""

  input("Appuie entrer, lance les dés.. ")
  dice = roll_dice()
  score = display_dice_and_score(dice)
  return dice, score


def play_007():
  """Fonction principale pour jouer au jeu."""
  total_score = 0
  num_turns = 0

  print(
    "Bienvenue !\nVoici le générateur de statistiques\npour un personnage de jeu vidéo."
  )
  if NUM_DICE > 0: #LIVE
    print("Dé 1 niveau de vie du pessonage.")
  if NUM_DICE > 1: #POWER
    print("Dé 2 niveau de force du personnage.")
  if NUM_DICE > 2: #PROTECTION
    print("Dé 3 niveau de protection du personnage.")
  if NUM_DICE > 3: #REGEN
    print("Dé 4 niveau de régénération du personnage.")
  if NUM_DICE > 4: #ARM
    print("Dé 5 niveau d'arme du personnage.")
  if NUM_DICE > 5: #DEFENCE
    print("Dé 6 niveau de défence du personnage.")
  if NUM_DICE > 6: #SORT
    print("Dé 6 niveau de sorts du personnage.")
    
  # affiche les résultats des dés 
  print("si vous obtenez", convert_dice_to_number({X}),  convert_dice_to_number({X}),  convert_dice_to_number({X}),"Sxb\nVous avez gagné!")
  
  print("Faire 'q' pour quitter le jeu.\n")

  while True:
    num_turns += 1
    print(f"<<<<< NOUVELLE STAT N°{num_turns} >>>>>\n")
    dice, score = play_turn()
    total_score += score

    if convert_dice_to_number(dice) == TARGET_SCORE:
      print(f"Félicitations ! Tu as obtenu exactement {TARGET_SCORE} tu as gagné !")
      break
        
    print("Tu peux relancer les dés, ils serons rangés par ordre décroissant.")
    
    choices = input(
      "Quels dés veux-tu relancer ?\n(sépare tes choix par un espace)\nFaire 'all' pour tous les dés \nFaire 'q' pour quiter :"
    ).split()

    if "all" in choices:
      #relance les 3 dés aléatoirement
      dice = roll_dice()

    if 'q' in choices:
      print("\nFin du jeu. Merci d'avoir joué !")
      break

    dice = reroll_dice(dice,
                       [int(choice) for choice in choices if choice.isdigit()])
    score = display_dice_and_score(dice)
    total_score += score

    if convert_dice_to_number(dice) == TARGET_SCORE:
      print("Félicitations ! Tu as obtenu exactement 421 TU EST EN PLAINE FORME !")
      break

    reroll_dice(dice, choices)

  print(f"\nScore total: {total_score}, Tours joués: {num_turns}")


if __name__ == "__main__":
  play_007()
