import random

# Simule le lancer de trois dés.
# Retourne une liste contenant les résultats des trois dés.
def roll_dice():

  # Générer trois nombres aléatoires entre 1 et 6 et les stocke dans une liste [] 
  # "reverse" range les dés du plus grand au plus petit.
  return sorted([random.randint(1, 6) for _ in range(3)], reverse=True)

# Afficher le résultat du lancer de trois dés.
def display_dice(dice):
  print("\nRésultats des dés :", dice)

# Calcule les points en fonction des résultats des dés.
def calculate_points(dice):
  # Converti la liste en une chaîne de caractères, converti en un entier.
  return int(
    ''.join(map(str, dice))
  )  

#  Permet au joueur de relancer les dés sélectionnés pour améliorer le score.
def reroll_dice(dice, choice):
  
  if choice == "all":
    return roll_dice()
  elif choice == "1":
    dice[0] = random.randint(1, 6)
  elif choice == "2":
    dice[1] = random.randint(1, 6)
  elif choice == "3":
    dice[2] = random.randint(1, 6)

  # Afficher le résultat du lancer de dés.
  return sorted(dice, reverse=True)

# Fonction principale
def play_421():
  
  print(
    "Bienvenue au jeu 421 !")

  # Initialiser le score du joueur à 0.
  total_points = 0 # Total des points du joueur.
  num_turns = 0  # Nombre de tours joués

  # Boucle principale du jeu.
  while True:
    num_turns += 1  # Incrémenter le nombre de tours
    # Afficher le nombre de tours joués.
    print(f"\nTour {num_turns} :")
    
    input("Appuie sur Entrée pour lancer les dés...")
    dice = roll_dice()
    
    # Afficher les résultats des dés
    display_dice(dice)
    
    # Calculer les points en fonction des résultats des dés
    points = calculate_points(dice)
    if points == 421 or dice == 421 :
      total_points += 1000
      print(
        "\nFélicitations ! Tu as obtenu le 421 ! Tu as gagné 1000 points supplémentaires !"
      )

    # Afficher le score actuel du joueur.
    else:
      points == dice
      
      print("Points obtenus :", points)
    
    
    if points == 421:
      break
      
    else:
      reroll_choice = input(
        "\nVeux-tu relancer tous les dés (all) ou un dé spécifique (1, 2 ou 3) ? (all/1/2/3) sinon entrer simplement : "
      )
      dice = reroll_dice(dice, reroll_choice)
      display_dice(dice)

      points = calculate_points(dice)

      print("Points obtenus :", points)
      


if __name__ == "__main__":
  play_421()
