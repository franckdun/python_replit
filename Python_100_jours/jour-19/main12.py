import sys

# Constantes 
MONTANT_MINIMUM = 500
MONTANT_MAXIMUM = 10000
TAUX_INTERET = 5
MENSUALITE_MINIMUM = 100
MOIS_MAXIMUM = 500

# Fonction pour calculer l'intérêt mensuel 
def calculer_interet_mensuel(capital_restant, taux):
    return (capital_restant / 100) * taux

# Fonction pour la saisie du montant emprunté avec gestion des erreurs 
def saisir_montant_emprunte():
    while True:
        try:
            montant_emprunte = float(input("\nEmpruntez entre 500€ et 10000€ "))
            if MONTANT_MINIMUM <= montant_emprunte <= MONTANT_MAXIMUM:
                return montant_emprunte
            else:
                print(f"Le montant doit être entre {MONTANT_MINIMUM}€ et {MONTANT_MAXIMUM}€. Essaie encore !")
              
        except ValueError:
            print("Euh... essaie avec un nombre cette fois, d'accord ? ")

# Fonction pour le choix du type de crédit 
def choisir_type_credit():
    while True:
        choix_credit = input("Mensualités fixes(1) ou Durée fixe(2) ? ")
        if choix_credit.lower() == 'x':
            print("Okay, okay... Tu veux quitter. Bye bye!")
            sys.exit()
        if choix_credit in ["1", "2"]:
            return choix_credit
        else:
            print("Hmm... C'est soit 1, soit 2. Essaie encore !")

# Fonction pour le crédit à échéance fixe 
def credit_a_echeance_fixe():
    mensualite = float(input("\nDonne-moi le montant que tu veux payer chaque mois : "))
    mois = None  # Pas besoin de spécifier la durée dans ce cas
    return mensualite, mois

# Fonction pour le crédit à échéance libre 
def credit_a_echeance_libre(capital):
    mois = int(input("\nChoisis combien de mois tu veux rembourser (maximum) : "))
    mensualite = max(MENSUALITE_MINIMUM, (capital / mois) * 2)  
    # Assurer que la mensualité est au moins de 100€
    return mensualite, mois

# Fonction pour afficher les détails mensuels 
def afficher_details_mensuels(mois, mensualite, interet, capital_restant):
    print(f"\nMois {mois}:")
    print(f"Payement {min(mensualite, capital_restant + interet):.2f}€ moins intérêts {interet:.2f}€")
    print(f"Solde     {capital_restant:.2f}€")

# Fonction pour générer le contenu Markdown 
def generer_contenu_markdown(mois, mensualite, interet, capital_restant, total_interets, capital_initial, pourcentage):
    contenu_markdown = "# Résultats du Crédit\n\n"
    contenu_markdown += f"**Solde initial :** {capital_initial:.2f}€\n\n"

    for mois in range(1, mois + 1) if mois else range(1, MOIS_MAXIMUM + 1):
        interet = calculer_interet_mensuel(capital_restant, TAUX_INTERET)
        total_interets += interet
        capital_restant += interet

        if mensualite:
            capital_restant -= mensualite

        afficher_details_mensuels(mois, mensualite, interet, capital_restant)

        # Ajouter les détails dans le contenu Markdown
        contenu_markdown += f"\n### Mois {mois}\n"
        contenu_markdown += f"- **Paiement :** {min(mensualite, capital_restant + interet):.2f}€ moins intérêts {interet:.2f}€\n"
        contenu_markdown += f"- **Solde :** {capital_restant:.2f}€\n"

        if capital_restant <= 100 or capital_restant <= mensualite:
            contenu_markdown += "\nCrédit remboursé ! --------- Bravo!\n"
            break

        if mois >= MOIS_MAXIMUM:
            contenu_markdown += "\nDésolé, paiement mensuel insuffisant, recommencez !\n"
            sys.exit()

    # Ajouter les résultats finaux dans le contenu Markdown
    pourcentage = (total_interets / capital_initial) * 100
    contenu_markdown += "\n# Résultats finaux\n"
    contenu_markdown += f"- **Durée du crédit :** {mois} mois\n"
    contenu_markdown += f"- **Coût du crédit :** {capital_initial:.2f} + {total_interets:.2f} d'intérêts\n"
    contenu_markdown += f"- **Pourcentage du capital initial :** {pourcentage:.2f}%\n"

    return contenu_markdown

# Fonction pour écrire le contenu Markdown dans un fichier
def ecrire_contenu_dans_fichier_markdown(contenu_markdown):
    with open("resultats_credit.md", "w") as fichier_md:
        fichier_md.write(contenu_markdown)
    print("Fichier Markdown généré avec succès : resultats_credit.md")

# Fonction principale
def main():
    print("Bienvenue chez Petit Crédit.")
    print(f"Intérêt mensuel sur mensualité fixé à {TAUX_INTERET}%.")
    print("Tapez 'x' pour quitter.")

    # Saisie du montant emprunté
    capital_initial = saisir_montant_emprunte()

    # Choix du type de crédit
    choix_credit = choisir_type_credit()

    # Exécution du calcul du crédit
    mensualite, mois = credit_a_echeance_fixe() if choix_credit == "1" else credit_a_echeance_libre(capital_initial)

    total_interets = 0
    capital_restant = capital_initial

    contenu_markdown = generer_contenu_markdown(mois, mensualite, 0, capital_restant, total_interets, capital_initial, 0)

    # Écriture du contenu dans un fichier Markdown
    ecrire_contenu_dans_fichier_markdown(contenu_markdown)

# Exécution du programme si le script est exécuté directement
if __name__ == "__main__":
    main()
