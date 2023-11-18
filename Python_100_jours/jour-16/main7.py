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
regles_du_jeu ="""🎶 Connaissez-vous la chanson de Petit Garçon ? 
Trouve les mots manquants de la chanson. 
3 chances de se tromper.
Tapez 'quite' pour sortir du jeu.\n"""

# Initialisation des variables
indice_paragraphe = 0
chances = 3
score = 0

# Affichage initial des règles
print(regles_du_jeu)

# Boucle principale
while True:
    # Affichage du paragraphe du mot à retirer
    mots_paragraphe = paragraphes_chanson[indice_paragraphe].split()
    mot_a_trouver = mots_a_trouver[indice_paragraphe]
    # Construction de la représentation avec des underscores pour les lettres non trouvées
    paragraphe_affichage = " ".join("_ " * len(mot_a_trouver) if mot == mot_a_trouver else mot for mot in mots_paragraphe)

    # Affichage du paragraphe
    print(paragraphe_affichage)

    # Demande à l'utilisateur de compléter le mot manquant
    reponse_utilisateur = input(f"\nMot en {len(mot_a_trouver)} lettres: ")

    # Vérification de la réponse
    if reponse_utilisateur.lower() == mot_a_trouver.lower():
        # Incrémente le score et affiche un message de victoire
        score += 1
        print(f" 🎉 Correct! Score: {score} points\n")
        indice_paragraphe += 1

    elif reponse_utilisateur.lower() == "quite":
        # Quitte le jeu si l'utilisateur le souhaite
        print(f"Merci d'avoir joué ! Score final {score} points.")
        break
      
    else:
        indice_paragraphe += 1
        # Traite une réponse incorrecte
        print(f"❌ Incorrect. Le mot était : {mot_a_trouver}")
        chances -= 1
        print(f"💔 Reste {chances} chances. Pour sortir, tapez 'quite'\n")
        
    # Vérification de la fin de la chanson
    if indice_paragraphe == len(paragraphes_chanson):
        print("🎉 Félicitations, tu as fait toutes les questions !")
        print(f"Score total {score}/14 points.")
        break

    # Vérification du nombre de chances restantes
    if chances == 0:
        print(f"💔 Score: {score} points. Désolé, tu as perdu !")
        break

# Demande à l'utilisateur s'il veut voir la chanson en entier
afficher_chanson = input("Tape 'y' et entrer pour afficher la chanson : ")
if afficher_chanson.lower() == "y":
    # Affiche la chanson complète
    print("\n 🎶 PETIT GARCON 🎶")
    print(paroles_chanson)
else:
    print("Au revoir\n")
