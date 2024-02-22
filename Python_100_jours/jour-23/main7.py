def obtenir_utilisateur():
    """
    Demande le nom d'utilisateur à l'utilisateur.
    """
    return input("Quel est ton nom d'utilisateur ? (Tape 'q' pour quitter) : ").lower()


def connexion_utilisateur(username, valid_credentials):
    """
    Connecte un utilisateur avec son nom d'utilisateur et son mot de passe.
    """
    try:
        password = input("Quel est ton mot de passe ? : ")
        if password == valid_credentials[username]["password"]:
            print("Bienvenue sur Replit !")
            print("Accès accordé !")
    except KeyboardInterrupt:
        print("\nOpération annulée.")


def ajouter_utilisateur(valid_credentials):
    """
    Ajoute un nouvel utilisateur avec un mot de passe, un email et demande son âge.
    """
    username = input("Choisissez un nom d'utilisateur : ").lower()
    if username in valid_credentials:
        print("Ce nom d'utilisateur existe déjà.")
        return
    else:
        email = input("Entrez votre adresse e-mail : ")
        password = input("Choisissez un mot de passe : ")
        try:
            age = int(input("Merci d'entrer ton âge : "))
        except ValueError:
            print("L'âge doit être un nombre entier.")
            return
        valid_credentials[username] = {"password": password, "email": email, "age": age}
        print("Compte créé avec succès ! Veuillez vous connecter avec votre nouveau compte.")


def ReplitLoginSystem():
    """
    Système de connexion principal.
    """
    valid_credentials = {
        "david": {
            "password": "bald",  # Mot de passe de David
            "age": 18,  # Âge de David
            "email": "david@example.com",  # Email de David
            "adresse": "123 rue de la République"  # Adresse de David
        },
        # Ajouter plus d'utilisateurs au besoin
    }

    while True:
        username = obtenir_utilisateur()
        if username == 'q':
            print("Au revoir !")
            break
        elif username in valid_credentials:
            connexion_utilisateur(username, valid_credentials)
        else:
            print("Nom d'utilisateur inconnu. Souhaitez-vous créer un compte ? (oui/non)")
            choix = input().lower()
            if choix == "oui":
                ajouter_utilisateur(valid_credentials)
            else:
                print("Réessayez avec un nom d'utilisateur valide ou tapez 'q' pour quitter.")


ReplitLoginSystem()
