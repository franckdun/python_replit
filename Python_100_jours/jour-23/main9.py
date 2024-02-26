import getpass

# Constantes
NB_ESSAIS = 3  # Nombre d'essais pour saisir le mot de passe
AGE_MIN = 18  # Âge minimum requis pour accéder au système

# Exceptions personnalisées
class UtilisateurInvalide(Exception):
    """Exception levée quand le nom d'utilisateur n'existe pas."""
    pass

class AgeIncorrect(Exception):
    """Exception levée quand l'âge n'est pas un entier ou est inférieur à l'âge minimum."""
    pass

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
    essais_restants = NB_ESSAIS
    while essais_restants > 0:
        try:
            password = getpass.getpass("Quel est ton mot de passe ? : ")
            if password == valid_credentials[username]["password"]:
                print("Bienvenue sur Replit !")
                if valid_credentials[username]["age"] >= AGE_MIN:
                    print("Accès accordé !")
                else:
                    print(f"Désolé, tu n'as pas l'âge requis pour accéder à ce système. Tu as {valid_credentials[username]['age']} ans et il faut avoir au moins {AGE_MIN} ans.")
                return
            else:
                essais_restants -= 1
                if essais_restants > 0:
                    print(f"Mot de passe incorrect. Il te reste {essais_restants} essais.")
                else:
                    print("Tu as épuisé tous tes essais.")
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
        email = input("Entrez ton adresse e-mail associée à ton compte : ")
        if email == valid_credentials[username]["email"]:
            print("Un e-mail a été envoyé à ton adresse avec les instructions pour réinitialiser ton mot de passe.")
        else:
            print("Adresse e-mail incorrecte.")
    except KeyboardInterrupt:
        print("\nOpération annulée.")


def ajouter_utilisateur(valid_credentials):
    """
    Ajoute un nouvel utilisateur avec un mot de passe, un e-mail et un âge.
    """
    username = input("Choisis un nom d'utilisateur : ").lower()
    if username in valid_credentials:
        print("Ce nom d'utilisateur existe déjà.")
        return
    else:
        email = input("Entrez ton adresse e-mail : ")
        password = getpass.getpass("Choisis un mot de passe : ")
        try:
            age = int(input("Merci d'entrer ton âge : "))
            if age < AGE_MIN:
                raise AgeIncorrect(f"Tu as {age} ans et il faut avoir au moins {AGE_MIN} ans pour accéder à ce système.")
        except ValueError:
            raise AgeIncorrect("L'âge doit être un nombre entier.")
        valid_credentials[username] = {"password": password, "email": email, "age": age}
        print("Compte créé avec succès ! Veuillez te connecter avec ton nouveau compte.")


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
        try:
            username = demander_utilisateur()
            if username == 'q':
                print("Au revoir !")
                exit()
            elif username in valid_credentials:
                connexion_utilisateur(username, valid_credentials)
            else:
                raise UtilisateurInvalide(f"Le nom d'utilisateur {username} n'existe pas.")
        except UtilisateurInvalide as e:
            print(e)
            print("Souhaites-tu créer un compte ? (y/n)")
            choix = input().lower()
            if choix == "y":
                ajouter_utilisateur(valid_credentials)
            else:
                print("Réessaie avec un nom d'utilisateur valide ou tape 'q' pour quitter.")
        except AgeIncorrect as e:
            print(e)
            print("Réessaie avec un âge valide ou tape 'q' pour quitter.")
			
systeme_connexion()