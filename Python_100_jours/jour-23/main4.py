def ReplitLoginSystem():
    # Définition des informations de connexion valides
    # Bibliothèque des paramètres de connexion
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
        username = input("Quel est ton nom d'utilisateur ? (Tape 'q' pour quitter) : ").lower()
        if username == 'q':
            print("Au revoir !")
            break
        if username in valid_credentials:
            try:
                password = input("Quel est ton mot de passe ? : ")
                if password == valid_credentials[username]["password"]:
                    print("Bienvenue sur Replit !")
                    # Vérification des paramètres de validation supplémentaires
                    age_required = valid_credentials[username].get("age")
                    if age_required:
                        try:
                            age = int(input("Merci d'entrer ton âge : "))
                            if age >= age_required:
                                print("Accès accordé !")
                                break
                            else:
                                print("Désolé, tu n'as pas l'âge requis pour accéder à ce système.")
                                continue
                        except ValueError:
                            print("L'âge doit être un nombre entier.")
                            continue
                    else:
                        break
                else:
                    print("Oops ! Mot de passe incorrect. Réessaie !")
            except KeyboardInterrupt:
                print("\nOpération annulée.")
                break
        else:
            print("Nom d'utilisateur inconnu. Souhaitez-vous créer un compte ? (oui/non)")
            choix = input().lower()
            if choix == "oui":
                email = input("Entrez votre adresse e-mail : ")
                # Ajout de l'utilisateur avec un mot de passe par défaut et l'email fourni
                # mot de passe
                password = input("Choisissez un mot de passe : ")
              
                valid_credentials[username] = {"password": password, "email": email}
                print("Compte créé avec succès ! Veuillez vous connecter avec votre nouveau compte.")
            else:
                print("Réessayez avec un nom d'utilisateur valide ou tapez 'q' pour quitter.")


ReplitLoginSystem()
