import random

def lancer_de():
    """
    Fonction pour lancer trois dés et les afficher dans l'ordre décroissant.
    Retourne le total des points obtenus avec les trois dés.
    """
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    de3 = random.randint(1, 6)

    print("Les dés sont : ", de1, de2, de3)

    # Trie les dés dans l'ordre décroissant
    des_tries = sorted([de1, de2, de3], reverse=True)
    print("Les dés dans l'ordre décroissant : ", des_tries)

    return sum(des_tries)

def jeu_421_multi():
    """
    Fonction principale pour jouer au jeu 421 contre un autre joueur ou l'ordinateur.
    """
    choix_mode = input("Choisissez le mode de jeu (1: contre l'ordinateur, 2: contre un autre joueur): ")

    if choix_mode == "1":
        print("Vous avez choisi de jouer contre l'ordinateur.")
        jeu_421_vs_ordi()
    elif choix_mode == "2":
        print("Vous avez choisi de jouer contre un autre joueur.")
        jeu_421_multi_joueurs()
    else:
        print("Choix invalide. Veuillez saisir '1' pour jouer contre l'ordinateur ou '2' pour jouer contre un autre joueur.")

def jeu_421_vs_ordi():
    """
    Fonction pour jouer au jeu 421 contre l'ordinateur.
    """
    manches_joueur = 0
    manches_ordi = 0

    while manches_joueur < 3 and manches_ordi < 3:
        print("\nNouvelle manche !")

        # Calcul du chiffre à battre par le joueur
        chiffre_a_battre = lancer_de()
        print("Le chiffre à battre est :", chiffre_a_battre)

        # Tour du joueur
        print("\nC'est à ton tour !")
        total_points_joueur = jouer_tour()

        # Tour de l'ordinateur
        print("\nC'est au tour de l'ordinateur !")
        total_points_ordi = lancer_de()

        # Détermination du gagnant de la manche
        if total_points_joueur == 421:
            print("Félicitations ! Tu as gagné cette manche !")
            manches_joueur += 1
        elif total_points_ordi == 421:
            print("L'ordinateur a gagné cette manche.")
            manches_ordi += 1
        elif total_points_joueur == chiffre_a_battre:
            print("Félicitations ! Tu as battu le chiffre à battre et gagné cette manche !")
            manches_joueur += 1
        elif total_points_ordi == chiffre_a_battre:
            print("Dommage ! L'ordinateur a battu le chiffre à battre et gagné cette manche.")
            manches_ordi += 1
        elif total_points_joueur < 421 and (total_points_ordi > 421 or total_points_ordi < total_points_joueur):
            print("Félicitations ! Tu as obtenu un meilleur score que l'ordinateur et gagné cette manche !")
            manches_joueur += 1
        elif total_points_ordi < 421 and (total_points_joueur > 421 or total_points_joueur < total_points_ordi):
            print("Dommage ! L'ordinateur a obtenu un meilleur score que toi et gagné cette manche.")
            manches_ordi += 1
        else:
            print("Cette manche est nulle.")

    if manches_joueur == 3:
        print("Bravo ! Tu as remporté la partie contre l'ordinateur !")
    elif manches_ordi == 3:
        print("Désolé, l'ordinateur a remporté la partie.")
    else:
        print("La partie est annulée.")

def jeu_421_multi_joueurs():
    """
    Fonction pour jouer au jeu 421 contre un autre joueur.
    """
    # La logique de jeu contre un autre joueur reste la même que dans la version précédente

def jouer_tour():
    """
    Fonction pour gérer le tour d'un joueur.
    Retourne le total des points obtenus lors du tour.
    """
    total_points = 0
    essais_restants = 3

    while essais_restants > 0:
        choix = input("Joueur, voulez-vous lancer les dés ? (o/n): ").lower()
        if choix == "o":
            total_points += lancer_de()
            print("Total de vos points :", total_points)
            essais_restants -= 1
        elif choix == "n":
            break
        else:
            print("Choix invalide. Veuillez saisir 'o' pour oui ou 'n' pour non.")

    return total_points

# Appel de la fonction pour choisir le mode de jeu
jeu_421_multi()
