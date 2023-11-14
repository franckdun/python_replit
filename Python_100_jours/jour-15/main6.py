import random

# Listes de bruits, animaux et appellations.
sounds = ["Ouaf Ouaf", "Miaou", "Cocorico", "Meuh", "Rouah", "Houhou", "Croa Croa", "Bzz Bzz", "Cri-cri", "Hi Han"]
animals = ["chien", "chat", "coq", "vache", "lion", "hibou", "grenouille", "abeille", "criquet", "cheval"]
termbrui = ["aboiement", "miaulement", "cocorico", "meuglement", "rugissement", "hululement", "coassement", "bourdonnement", "cri-cri", "hennissement"]

# Tableau pour garder une trace des questions posées
questions_posees = []

# Initialisation du compteur
counter = 0
score = 0
question = 0

# Présentation des règles du jeu
print("Bienvenue au jeu des bruits d'animaux!")
print("Tu dois deviner quel animal fait le bruit donné.")
print("Si tu réussis, tu gagnes un point. Si tu échoues trois fois, le jeu se termine.")
print("Si tu veux quitter à tout moment, tape 'exit'. Bonne chance!")

# Boucle while pour permettre plusieurs tentatives
while counter < 3:
    # Choix aléatoire d'un animal et de son bruit (évite les répétitions)
    indice_sound = random.randint(0, len(sounds) - 1)
    while indice_sound in questions_posees:
        indice_sound = random.randint(0, len(sounds) - 1)

    sound_choisi = sounds[indice_sound]
    animal_attendu = animals[indice_sound]
    termbrui_attendu = termbrui[indice_sound]

    # Ajout de l'indice au tableau des questions posées
    questions_posees.append(indice_sound)

    # Demande à l'utilisateur de deviner le bruit
    devinette = input(f"Tentative {counter + 1}: Qui fait le bruit {sound_choisi} ? ")

    # ajoute 1 au compteur question
    question += 1

    # Vérification de la devinette
    if devinette == animal_attendu:
        print(f"Bravo ! Tu as deviné le {termbrui_attendu} de {animal_attendu}.")
        counter = 0  # Réinitialise le compteur en cas de bonne réponse
        score += 1   # Incrémente le score

    elif devinette.lower() == "exit":
        print(f"Tentative {counter + 1}. Quoi! On s'arrête déjà!")
        break  # Sort de la boucle si l'utilisateur veut quitter

    else:
        print("Désolé, raté!")
        counter += 1
else:
    print("Tentatives épuisées. Perdu, plus de chances !")

print(f"Fin du jeu. Ton score final est de {score} bonnes réponses sur {question} questions.")
print("Merci d'avoir joué !")
print("Au revoir !")