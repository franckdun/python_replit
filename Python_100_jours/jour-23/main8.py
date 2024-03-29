import getpass

def demander_utilisateur():
    """
    Demande à l'utilisateur de saisir un nom d'utilisateur.
    """
    return input("Quel est ton nom d'utilisateur ? (Tape 'q' pour quitter) : ").lower()


def connexion_utilisateur(username, valid_credentials):
    """
    Vérifie si le nom d'utilisateur et le mot de passe saisis sont valides.
    Si le mot de passe est incorrect, demande à l'utilisateur de saisir son adresse e-mail pour récupérer le mot de passe.
    """
    essais_restants = 3
    while essais_restants > 0:
        try:
            password = getpass.getpass("Quel est ton mot de passe ? : ")
            if password == valid_credentials[username]["password"]:
                print("Bienvenue sur Replit !")
                if valid_credentials[username]["age"] >= 18:
                    print("Accès accordé !")
                else:
                    print("Désolé, tu n'as pas l'âge requis pour accéder à ce système.")
                return
            else:
                essais_restants -= 1
                if essais_restants > 0:
                    print(f"Mot de passe incorrect. Il vous reste {essais_restants} essais.")
                else:
                    print("Vous avez épuisé tous vos essais.")
                    recuperer_mot_de_passe(username, valid_credentials)
                    return
        except KeyboardInterrupt:
            print("\nOpération annulée.")
            return


def recuperer_mot_de_passe(username, valid_credentials):
    """
    Demande à l'utilisateur de saisir son adresse e-mail pour récupérer le mot de passe.
    """
    try:
        email = input("Entrez votre adresse e-mail associée à votre compte : ")
        if email == valid_credentials[username]["email"]:
            print("Un e-mail a été envoyé à votre adresse avec les instructions pour réinitialiser votre mot de passe.")
        else:
            print("Adresse e-mail incorrecte.")
    except KeyboardInterrupt:
        print("\nOpération annulée.")


def ajouter_utilisateur(valid_credentials):
    """
    Ajoute un nouvel utilisateur avec un mot de passe, un e-mail et un âge.
    """
    username = input("Choisissez un nom d'utilisateur : ").lower()
    if username in valid_credentials:
        print("Ce nom d'utilisateur existe déjà.")
        return
    else:
        email = input("Entrez votre adresse e-mail : ")
        password = getpass.getpass("Choisissez un mot de passe : ")
        try:
            age = int(input("Merci d'entrer ton âge : "))
            if age < 18:
                print("Désolé, tu n'as pas l'âge requis pour accéder à ce système.")
                return
        except ValueError:
            print("L'âge doit être un nombre entier.")
            return
        valid_credentials[username] = {"password": password, "email": email, "age": age}
        print("Compte créé avec succès ! Veuillez vous connecter avec votre nouveau compte.")


def systeme_connexion():
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
        username = demander_utilisateur()
        if username == 'q':
            print("Au revoir !")
            break
        elif username in valid_credentials:
            connexion_utilisateur(username, valid_credentials)
        else:
            print("Nom d'utilisateur inconnu. Souhaitez-vous créer un compte ? (y/n)")
            choix = input().lower()
            if choix == "y":
                ajouter_utilisateur(valid_credentials)
            else:
                print("Réessayez avec un nom d'utilisateur valide ou tapez 'q' pour quitter.")


systeme_connexion()
