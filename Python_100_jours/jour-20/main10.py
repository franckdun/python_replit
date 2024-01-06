def main():
  # Générateur de liste
  print('*** GENERATEUR DE LISTE ***\n')

  # Fonction pour générer la liste en fonction des paramètres
  def generer_liste(depart, fin, pas):
      # Déterminer automatiquement si la liste sera croissante ou décroissante
      sens = "croissante" if depart < fin else "décroissante"
      liste = list(range(depart, fin, (1 if sens == "croissante" else -1) * pas))
      return liste, sens

  # Fonction pour demander à l'utilisateur un entier avec gestion d'erreur
  def demander_entier(message):
      while True:
          try:
              return int(input(message))
          except ValueError:
              print("Erreur : Veuillez entrer un nombre entier.")

  # Demander à l'utilisateur les informations nécessaires
  nom_liste = input('Quel nom voulez-vous donner à votre liste ? ')
  depart = demander_entier('Entrez une valeur de départ : ')
  fin = demander_entier('Entrez une valeur d\'arrivée : ')
  pas = demander_entier("Entrez la valeur absolue d'incrémentation : ")

  # Générer la liste
  liste, sens = generer_liste(depart, fin, pas)

  # Afficher les résultats dans la console
  print('\nRésultats :')
  print(f'Nom de la liste : {nom_liste}')
  print(f'Départ : {depart}')
  print(f'Arrivée : {fin}')
  print(f'Incrémentation : {pas}')
  print(f'Sens de la liste : {sens}')

  print('\nListe générée :')
  for element in liste:
      print(f'- {element}')

  # Demander à l'utilisateur s'il souhaite enregistrer les résultats dans un fichier markdown
  enregistrer_fichier = input('Voulez-vous enregistrer les résultats dans un fichier markdown ? (Y/N) : ').lower() == 'y'

  # Si l'utilisateur souhaite enregistrer dans un fichier markdown, le faire
  if enregistrer_fichier:
      nom_fichier = nom_liste

      # Enregistrer les résultats dans un fichier markdown
      with open(nom_fichier + '.md', 'w') as fichier_md:
          
          fichier_md.write(f'# Nom de la liste : {nom_liste}\n\n')
          fichier_md.write(f'Liste générée ({sens})\n')
          fichier_md.write(f'\nDépart : {depart}\n')
          fichier_md.write(f'\nArrivée : {fin}\n')
          fichier_md.write(f'\nIncrémentation : {pas}\n\n')
          fichier_md.write('\nListe générée :\n\n')
          for element in liste:
              fichier_md.write(f'- {element}\n')
      print(f'Les résultats ont été enregistrés dans {nom_fichier}.md visible dans Files')

# Exécution du programme si le script est exécuté directement
if __name__ == "__main__":
  main()
