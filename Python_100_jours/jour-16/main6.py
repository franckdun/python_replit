# Chanson
paroles_chanson = """
Dans son manteau rouge et blanc 
sur un traîneau porté par le vent

Il descendra par la cheminée 
petit garçon, il est l'heure d'aller se coucher

Tes yeux se voilent 
écoute les étoiles

Tout est calme, reposé 
entends-tu les clochettes tintinnabuler

Et demain matin , petit garçon 
tu trouveras dans tes chaussons

Tous les jouets dont tu as rêvé 
petit garçon il est l'heure d'aller se coucher

Tes yeux se voilent 
écoute les étoiles

Tout est calme, reposé 
Entends tu les clochettes tintinnabuler

Et demain matin , petit garçon 
tu trouveras dans tes chaussons

Tous les jouets dont tu as rêvé 
petit garçon il est l'heure d'aller se coucher

Tes yeux se voilent 
écoute les étoiles

Tout est calme, reposé 
entends tu les clochettes tintinnabuler

Et demain matin , petit garçon 
tu trouveras dans tes chaussons

Tous les jouets dont tu as rêvé 
petit garçon il est l'heure d'aller se coucher """

# Liste des mots à trouver dans chaque paragraphe
mots_a_trouver = ["blanc", "cheminée", "voilent", "clochettes", "demain", "jouets", "yeux" , "reposé", "matin", "rêvé", "écoute", "tintinnabuler", "chaussons", "coucher"]

# Séparation des paragraphes de la chanson par 2 
paragraphes_chanson = paroles_chanson.split('\n\n')

# Règles du jeu
regles_du_jeu = """
Connaissez-vous la chanson 'Petit garçon' !
Trouvez les mots manquants de la chanson. 
3 chances de se tromper.
Tapez 'QUITE' pour sortir du jeu.\n
"""

# Initialisation des variables
indice_paragraphe = 0
chances = 3
score = 0

# Affichage initial des règles
print(regles_du_jeu)

# Boucle while True 
while True:
    # Affichage du paragraphe du mot à retirer
    mots_paragraphe = paragraphes_chanson[indice_paragraphe].split()
    #Relie le mot à trouver a son paragraphe
    mot_a_trouver = mots_a_trouver[indice_paragraphe]
    #Remplace et ajuste le nombre de underscores dans le mot à trouver
    paragraphe_affichage = " ".join("_ " * len(mot_a_trouver) if mot == mot_a_trouver else mot for mot in mots_paragraphe)
    # Affichage du paragraphe
    print(paragraphe_affichage)

    # Demande à l'utilisateur de compléter le mot manquant et indique le nombre de lettres du mot_a_trouver
    reponse_utilisateur = input(f"\nMot en {len(mot_a_trouver)} lettres: ")

    # Vérification validation réponse (en minuscule)
    if reponse_utilisateur.lower() == mot_a_trouver.lower():
        # incrémente le score de 1 et affiche un message de victoire
        score += 1
        print(f" 🎉 Correct! Score: {score} points\n")
        indice_paragraphe += 1
    # Vérifie si le joueur veux quitter le jeu
    elif reponse_utilisateur.lower() == 'quite':
        print(f"Merci d'avoir joué ! Ton score final est de {score} points.")
        # quitte le jeu
        break
    # Décrémente les chances si la réponse est fausse
    else:
        print(f"❌ Incorrect. Le mot correct était : {mot_a_trouver}\n")
        chances -= 1
        # Affichage des chances restantes
        print(f"💔 Crédit chances: {chances}   (Pour sortir faire 'QUITE')\n")
    # Demande à l'utilisateur s'il souhaite quitter le jeu

    # Incrémente le paragraphe pour passer à la question suivante
    indice_paragraphe += 1

    # Vérification de la fin de la chanson
    if indice_paragraphe == len(paragraphes_chanson):
        print("🎉Félicitations, tu as complété toute la chanson !")
        print(f"Ton score est de {score} points.")
        break

    # Vérification du nombre de chances restantes
    if chances == 0 :
      print(f"💔 Score: {score} points. Désolé, tu as perdu !")
      break
#Tape ok pour voir la chanson en entier
ok = input("Tape ok pour voir la chanson en entier : ")
if ok == "ok":
  #Affiche la chanson
  print("\nParoles de PETIT GARCON.")
  print(paroles_chanson)
else:
  print("Au revoir")