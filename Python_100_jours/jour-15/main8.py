# Importation méthode choix aléatoires random
import random

# Listes de bruits.
sounds = ["Ouaf Ouaf", "Miaou", "Cocorico", "Meuh", "Rouah", "Houhou", "Croa Croa", "Bzz Bzz", "Cri-cri", "Hi Han"]
# Liste de animaux.
animals = ["chien", "chat", "coq", "vache", "lion", "hibou", "grenouille", "abeille", "criquet", "cheval"]
# Liste de types de cris.
termbrui = ["aboiement", "miaulement", "cocorico", "meuglement", "rugissement", "hululement", "coassement", "bourdonnement", "cri-cri", "hennissement"]

# Tableau pour garder une trace des questions posées
questions_posees = []

# Initialisation compteur
counter = 0  # Compteur des tentatives
score = 0    # Compteur du score
question = 0 # Compteur des questions posées

# Présentation des instructions du jeu
print("Bienvenue au jeu des bruits d'animaux!")
print("Deviner quel animal fait le bruit donné.")
print("Si tu réussis la question, tu gagnes un point.")
print("Si tu échoues trois tentatives, le jeu se termine.")
print("Pour quitter à tout moment, tape 'exit'. Bonne chance!\n")

# Boucle while pour permettre plusieurs tentatives
while counter < 3:
    # Déclaration aléatoire variable bruit
    indice_sound = random.randint(0, len(sounds) - 1)
    # Tant que l'animal n'a pas été choisi dans la liste des questions posées, recommencer la boucle et le choix aléatoire
    while indice_sound in questions_posees:
        indice_sound = random.randint(0, len(sounds) - 1)
    # Correspondances des choix aléatoires de variables bruits aux variables animal et cris des listes.
    sound_choisi = sounds[indice_sound]
    animal_attendu = animals[indice_sound]
    termbrui_attendu = termbrui[indice_sound]

    # Ajout de l'indice au tableau des questions posées
    questions_posees.append(indice_sound)

    # Demande à l'utilisateur de deviner le bruit
    devinette = input("Tentative {}: Quel animal fait le bruit {} ? ".format(counter + 1, sound_choisi))

    # Ajoute 1 au compteur question
    question += 1

    # Vérification de la devinette en convertissant en minuscules grâce à la fonction .lower()
    if devinette.lower() == animal_attendu:
        print("Bravo ! Tu as deviné le {} de {}.\n".format(termbrui_attendu, animal_attendu))
        counter = 0  # Réinitialise tentative
        score += 1   # Incrémente le score
    elif devinette.lower() == "exit":
        # Retire la dernière question
        question -= 1
        print("Tentative {}: Quoi! On s'arrête déjà!\n".format(counter + 1))
        break  # Sort de la boucle si l'utilisateur veut quitter
    else:
        print("Désolé, raté! Essaye encore.\n")
        # Ajoute 1 au compteur tentative
        counter += 1

    # Ajout du résultat du score pour chaque réponse
    print("Score: {}/{}".format(score, question))

# Sortie de la boucle while
else:
    print("Tentatives épuisées. Perdu, plus de chances !")

# Affichage du score final
print("Fin du jeu. Ton score final est de {} bonnes réponses sur {} questions.".format(score, question))
print("Merci d'avoir joué !")
