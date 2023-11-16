# Chanson
paroles_chanson = """
Dans son manteau rouge et blanc ,
sur un traîneau porté par le vent

Il descendra par la cheminée ,
petit garçon, il est l'heure d'aller se coucher

Tes yeux se voilent ,
écoute les étoiles

Tout est calme, reposé ,
entends-tu les clochettes tintinnabuler

Et demain matin , petit garçon ,
tu trouveras dans tes chaussons

Tous les jouets dont tu as rêvé ,
petit garçon il est l'heure d'aller se coucher

Tes yeux se voilent ,
écoute les étoiles

Tout est calme, reposé ,
Entends tu les clochettes tintinnabuler

Et demain matin , petit garçon ,
tu trouveras dans tes chaussons

Tous les jouets dont tu as rêvé ,
petit garçon il est l'heure d'aller se coucher

Tes yeux se voilent ,
écoute les étoiles

Tout est calme, reposé ,
entends tu les clochettes tintinnabuler

Et demain matin , petit garçon ,
tu trouveras dans tes chaussons

Tous les jouets dont tu as rêvé ,
petit garçon il est l'heure d'aller se coucher """

# Liste des mots à trouver dans chaque paragraphe
mots_a_trouver = ["blanc", "cheminée", "voilent", "clochettes", "demain", "jouets", "yeux" , "reposé", "matin", "rêvé", "écoute", "tintinnabuler", "chaussons", "coucher"]

# Séparation des paragraphes de la chanson
paragraphes_chanson = paroles_chanson.split('\n\n')

# Règles du jeu
regles_du_jeu = """
Comment apprendre la chanson 'Petit garçon' !
Trouvez les mots manquants de la chanson. 
3 chances de se tromper par paragraphe.
Tapez 'quite' pour sortir du jeu.\n
"""

# Initialisation des variables
indice_paragraphe = 0
chances = 3
score = 0

# Affichage initial des règles
print(regles_du_jeu)

# Boucle principale
while True:
    # Affichage du paragraphe sans le mot à retirer
    mots_paragraphe = paragraphes_chanson[indice_paragraphe].split()
    mot_a_trouver = mots_a_trouver[indice_paragraphe]
    paragraphe_affichage = " ".join("_ _ _ _" if mot == mot_a_trouver else mot for mot in mots_paragraphe)
    print(paragraphe_affichage)

    # Demande à l'utilisateur de compléter le mot manquant
    reponse_utilisateur = input("\nComplète le mot manquant : ")

    # Vérification de la réponse
    if reponse_utilisateur.lower() == mot_a_trouver.lower():
        score += 1
        print(f"\n Correct! Score: {score} points\n")
        indice_paragraphe += 1
        
    elif reponse_utilisateur.lower() == 'quite':
        print(f"Merci d'avoir joué ! Ton score final est de {score} points.")
        break
    else:
        print(f"Incorrect. Le mot correct était : {mot_a_trouver}\n")
        chances -= 1
        # Affichage des chances restantes
        print(f"crédit chances: {chances} ")
        # Demande à l'utilisateur s'il souhaite quitter le jeu
        print("'quite' pour quitter.\n")

    # Vérification de la fin de la chanson
    if indice_paragraphe == len(paragraphes_chanson):
        print("Félicitations, tu as complété toute la chanson !")
        print(f"Ton score est de {score} points.")
        break

    # Réinitialisation des chances pour le prochain paragraphe
    chances = 3 if chances == 0 else chances

    