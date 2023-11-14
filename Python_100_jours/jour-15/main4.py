import random

# Liste bruits, animaux et appélations.
sounds = ["Ouaf Ouaf", "Miaou", "Cocorico", "Meuh", "Rouah"]
animals = ["chien", "chat", "coq", "vache", "lion"]
termbrui = ["aboiement", "miaulement", "cocorico", "meuglement", "rugissement"]

# Choix aléatoire d'un animal et de son bruit
indice_sound = random.randint(0, len(sounds) - 1)
sound_choisi = sounds[indice_sound]
animal_attendu = animals[indice_sound]
termbrui_attendu = termbrui[indice_sound]

# Message instructions
print("si vous dépassez de 3 essais, le jeu se termine.")
print("Devine le bruit de l'animal !")
# Initialisation de la variable de devinette
devinette = ""
# Initialisation compteur
counter = 0
# Boucle while permetant plusieurs tentatives
while counter != 3 and devinette != "exit":
    
    print("Tentative", counter, ":")
    # Demande de deviner le bruit
    devinette = input(f"Qui fait le bruit {sound_choisi} ? ")

    # Vérification de la devinette
    if devinette == animal_attendu :
        print("Bravo ! Tu as deviné le", termbrui_attendu, 'de', animal_attendu)
      
    # vérification de compteur
    elif counter == 3 :
        print("Tentative", counter, "Perdu, plus de chances!")
        print("Perdu, plus de chances !") 
      
    elif devinette == "exit" :
        print("essais", counter, ";")
        print("Quoi! On s'arrête déjà!")

  
    else:
        print("Désolé, essaie encore.")
        counter += 1
print("fin du jeu")
        
