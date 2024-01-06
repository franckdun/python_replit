# Générateur de liste
print('GENERATEUR DE LISTE\n')

# Déclare la variable "nom de liste"
nom_liste = input('Quel nom voulez-vous donner à votre liste ?')
# Déclare la variable "nombre de départ"
A = int(input('Entrez une valeur de départ : '))
# Déclare la variable "nombre de fin"
B = int(input('Entrez une valeur d\'arrivée : '))
# Déclare la variable "nombre de pas"
C = int(input('Entrez un incrément : '))

# Vérifier si l'utilisateur souhaite une liste décroissante
decroissant = input(
    'Voulez-vous une liste décroissante ? (Y/N) : ').lower() == 'y'

# Générer la liste en fonction des paramètres fournis
if decroissant:
    liste = list(range(B, A, -C))
else:
    liste = list(range(A, B, C))

# Afficher la liste dans la console
print('Liste générée :', liste)

# Demander à l'utilisateur s'il souhaite enregistrer les résultats dans un fichier markdown
enregistrer_fichier = input(
    'Voulez-vous enregistrer les résultats dans un fichier markdown ? (Y/N) : '
).lower() == 'y'

# Si l'utilisateur souhaite enregistrer dans un fichier markdown, le faire
if enregistrer_fichier:
    nom_fichier = nom_liste

    # Enregistrer les résultats dans un fichier markdown
    with open(nom_fichier + '.md', 'w') as fichier:
        fichier.write('# Liste générée\n\n')
        fichier.write('Voici la liste générée :\n\n')
        for element in liste:
            fichier.write(f'- {element}\n')
    print(f'Les résultats ont été enregistrés dans {nom_fichier}.md')
