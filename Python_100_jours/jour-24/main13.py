import random
def presentation():
    print("Pour gagner au jeu 421 !")
    print("Obtiens 421 avec les dés.")
    print("Oubien fait 421 points.")
    print("Quitter le jeu, tapez 'q'.\n")

def réglement_game():
    print("Relancer tous les dés (all)")
    print("Relancer certains dés (1), (2), etc) ?")
    print("Relancer deux dés (1 2), (1 3), etc) ?")
    

def Turns_num(num_turns):
    num_turns += 1 #Incrémente nombre de tours
    print(f"< TOUR  n° {num_turns} >\n")
    return num_turns

def roll_dice():
    """Simule le lancer de trois dés à six faces.
    Retourne une liste contenant les résultats des trois dés, triés du plus grand au plus petit.
    """
    return sorted([random.randint(1, 6) for _ in range(3)], reverse=True)

def display_dice_and_score(dice):
    """Affiche les résultats des dés et.
    """
    print("\n>", convert_dice_to_number(dice), "\n")
  
    score = sum(dice)# calcule la somme des dés
    return score
  
def convert_dice_to_sum(dice):
    score = sum(dice)# calcule la somme des dés
    print("+", score, "Points\n")# affiche la somme des dés
    return score

def convert_dice_to_number(dice):
    """Convertit les résultats des dés en un nombre entier.
    """
    return int(''.join(map(str, dice)))

def reroll_dice(dice, choice):
    """Permet au joueur de relancer les dés sélectionnés pour améliorer son score.
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
    """Fonction principale pour jouer au jeu 421.
    """
    #declarations des variables
    total_score = 0  # Score total du joueur
    num_turns = 0  # Nombre de tours joués
  
    presentation()# Affiche la présentation du jeu
    Turns_num(num_turns)# Affiche le numéro du tour

    while True:
        
        try:
            input("Lancer les dés... (Entrer)")
            dice = roll_dice()  # Lancer les dés
            current_score = display_dice_and_score(dice)# Afficher résultats dés 
            total_score += current_score  # Ajouter le score du tour au score total

            if 421 == convert_dice_to_number(dice):
                print("Incroyable ! Félicitations !")
                print("Vous avez obtenu 421 du premier coup !")
                break

            print("Relancer tous les dés (all)")
            print("Relancer certains dés (1), (2), etc) ?")
            print("Relancer deux dés (1 2), (1 3), etc) ?")
            
            print("\nDés:  1 >", dice[0], "   2 >", dice[1], "   3 >", dice[2])
                      
            try:
              reroll_choice = input("\nChanger les dés ? > ")
              
            except ValueError:
              print("Choix invalide. Veuillez réessayer.")
              continue 
              
            if reroll_choice.lower() == "q":
                print("Fin du jeu. Merci d'avoir joué !")
                break

            if reroll_choice in ["all", "1", "2", "3", "1 2", "1 3", "2 3"]:
                dice = reroll_dice(dice, reroll_choice)
              
                display_dice_and_score(dice)
              
                current_score = convert_dice_to_sum(dice)  # Afficher les nouveaux résultats des dés et le score du joueur
              
                if 421 == convert_dice_to_number(dice):
                  print("Félicitations ! Tu as obtenu le 421 !")
                  print(f"Tu as gagné en {num_turns} tours !")
                  break 
                
            # vérifie que joueur na pas fait une faute de frappe
            else:
                print("Choix invalide. Veuillez réessayer.")
                continue
              
            num_turns += 1  # Incrémenter le nombre de tours  
            Turns_num(num_turns)# Affiche le numéro du tour
          
        except KeyboardInterrupt:
            print("\nFin du jeu. Merci d'avoir joué !")
            break
        except ValueError:
            print("Choix invalide. Veuillez réessayer.")
            continue

    print("\nScore total:", total_score, "      Tours total:", num_turns + 1 )  
    # Afficher score total et le nombre de tours totaux
  
if __name__ == "__main__":
    play_421()
