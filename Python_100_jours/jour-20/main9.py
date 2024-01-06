def main():
  # Générateur de liste
  print('GENERATEUR DE LISTE\n')

  # Fonction pour générer la liste en fonction des paramètres
  def generer_liste(depart, fin, pas):
      # Déterminer automatiquement si la liste sera croissante ou décroissante
      sens = 1 if depart < fin else -1
      return list(range(depart, fin, sens * pas))

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
  liste = generer_liste(depart, fin, pas)

  # Afficher la liste dans la console
  print('Liste générée :', liste)

  # Demander à l'utilisateur s'il souhaite enregistrer les résultats dans un fichier markdown
  enregistrer_fichier = input('Voulez-vous enregistrer les résultats dans un fichier markdown ? (Y/N) : ').lower() == 'y'

  # Si l'utilisateur souhaite enregistrer dans un fichier markdown, le faire
  if enregistrer_fichier:
      nom_fichier = nom_liste

      # Enregistrer les résultats dans un fichier markdown
      with open(nom_fichier + '.md', 'w') as fichier_md:
          fichier_md.write('# Liste générée\n\n')
          fichier_md.write('Voici la liste générée :\n\n')
          for element in liste:
              fichier_md.write(f'- {element}\n')
      print(f'Les résultats ont été enregistrés dans {nom_fichier}.md visible dans Files')

# Exécution du programme si le script est exécuté directement
if __name__ == "__main__":
  main()
