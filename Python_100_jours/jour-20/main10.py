import sys

# Constantes
MONTANT_MINIMUM = 500
MONTANT_MAXIMUM = 10000
TAUX_INTERET = 5
MENSUALITE_MINIMUM = 100
MOIS_MAXIMUM = 500

# Fonction pour calculer l'intérêt mensuel 📈
def calculer_interet_mensuel(capital_restant, taux):
    return (capital_restant / 100) * taux

# Fonction pour la saisie du montant emprunté avec gestion des erreurs 🤓
def saisir_montant_emprunte():
    while True:
        try:
            montant_emprunte = float(input("\nEntrez un montant de 500€ à 10000€ maximum ? "))
            if MONTANT_MINIMUM <= montant_emprunte <= MONTANT_MAXIMUM:
                return montant_emprunte
            else:
                print(f"Le montant emprunté doit être entre {MONTANT_MINIMUM}€ et {MONTANT_MAXIMUM}€. Réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Fonction pour le choix du type de crédit 🤔
def choisir_type_credit():
    while True:
        choix_credit = input("Mensualités fixes(1) ou Durée fixe(2) ? ")
        if choix_credit.lower() == 'x':
            print("Sortie du programme. 😢 Bye bye!")
            sys.exit()
        if choix_credit in ["1", "2"]:
            return choix_credit
        else:
            print("Choix invalide. Veuillez choisir 1 ou 2. 🤷‍♂️")

# Fonction pour le crédit à échéance fixe 💸
def credit_a_echeance_fixe():
    mensualite = float(input("\n(1) Entrez le paiement mensuel souhaité : "))
    mois = None  # Pas besoin de spécifier la durée dans ce cas
    return mensualite, mois

# Fonction pour le crédit à échéance libre 📅
def credit_a_echeance_libre(capital):
    mois = int(input("\n(2) Entrez la durée maximum en mois : "))
    mensualite = max(MENSUALITE_MINIMUM, (capital / mois) * 2)  # Assurer que la mensualité est au moins de 100€
    return mensualite, mois

# Fonction pour afficher les détails mensuels 📊
def afficher_details_mensuels(mois, mensualite, interet, capital_restant):
    print(f"\nMois {mois}:")
    print(f"Payement {min(mensualite, capital_restant + interet):.2f}€ moins intérêts {interet:.2f}€")
    print(f"Solde     {capital_restant:.2f}€")

# Fonction pour exécuter le calcul du crédit 🚀
def executer_calcul_credit(capital_initial, choix_credit):
    taux = TAUX_INTERET
    total_interets = 0
    capital_restant = capital_initial

    print(f"\nSolde initial : {capital_initial:.2f}€")

    if choix_credit == "1":
        mensualite, mois = credit_a_echeance_fixe()
    else:
        mensualite, mois = credit_a_echeance_libre(capital_initial)

    for mois in range(1, mois + 1) if mois else range(1, MOIS_MAXIMUM + 1):
        interet = calculer_interet_mensuel(capital_restant, taux)
        total_interets += interet
        capital_restant += interet

        if mensualite:
            capital_restant -= mensualite

        if capital_restant <= 100 or capital_restant <= mensualite:
            afficher_details_mensuels(mois, mensualite, interet, capital_restant)
            print("\n--- 🎉 Bravo! Crédit remboursé ! ---")
            break

        if mois >= MOIS_MAXIMUM:
            print("Désolé, paiement mensuel insuffisant, recommencez ! 😅")
            sys.exit()

        afficher_details_mensuels(mois, mensualite, interet, capital_restant)

    # Affichage du résultat final 🏁
    pourcentage = (total_interets / capital_initial) * 100
    print(f"\nDurée du crédit : {mois} mois ")
    print(f"Coût du crédit : {capital_initial:.2f} + {total_interets:.2f} d'intérêts")
    print(f"Soit {pourcentage:.2f}% du capital initial. 💸")

# Fonction principale 🚀
def main():
    print("\nBienvenue chez Petit Crédit. 🌟")
    print(f"Intérêt mensuel sur mensualité fixé à {TAUX_INTERET}%. 📈")
    print("Tapez 'x' pour quitter. 😊")

    # Saisie du montant emprunté
    capital_initial = saisir_montant_emprunte()

    # Choix du type de crédit
    choix_credit = choisir_type_credit()

    # Exécution du calcul du crédit
    executer_calcul_credit(capital_initial, choix_credit)

# Exécution du programme si le script est exécuté directement 🎬
if __name__ == "__main__":
    main()
