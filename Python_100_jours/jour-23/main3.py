def ReplitLoginSystem():
    # Définition des informations de connexion valides
    valid_credentials = {
        "david": {
            "password": "bald",
            "age": 30,
            "email": "david@example.com",
            "adresse": "123 rue de la République"
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
            print("Oops ! Nom d'utilisateur inconnu. Réessaie !")


ReplitLoginSystem()
