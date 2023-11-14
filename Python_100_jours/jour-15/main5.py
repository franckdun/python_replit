import random

# Listes de bruits, animaux et appellations.
sounds = ["Ouaf Ouaf", "Miaou", "Cocorico", "Meuh", "Rouah"]
animals = ["chien", "chat", "coq", "vache", "lion"]
termbrui = ["aboiement", "miaulement", "cocorico", "meuglement", "rugissement"]

# Tableau pour garder une trace des questions posées
questions_posees = []

# Initialisation du compteur
counter = 0

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

    # Vérification de la devinette
    if devinette == animal_attendu:
        print(f"Bravo ! Tu as deviné le {termbrui_attendu} de {animal_attendu}.")
        counter = 0  # Réinitialise le compteur en cas de bonne réponse
        
    elif devinette.lower() == "exit":
        print(f"Essais {counter + 1}. Quoi! On s'arrête déjà!")
        break  # Sort de la boucle si l'utilisateur veut quitter

    else:
        print("Désolé, raté!")
        counter += 1
else:
    print("Tentatives épuisées. Perdu, plus de chances !")

print("Fin du jeu.")
print("Merci d'avoir joué !")
