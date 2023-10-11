
# Déclaration des constantes
secondes_par_minute = 60
minutes_par_heure = 60
heures_par_jour = 24
jours_par_an = 365
jours_par_an_bissextile = 366

# Calcul du nombre de secondes dans une année normale
secondes_par_an = secondes_par_minute * minutes_par_heure * heures_par_jour * jours_par_an

# Calcul du nombre de secondes dans une année bissextile
secondes_par_an_bissextile = secondes_par_minute * minutes_par_heure * heures_par_jour * jours_par_an_bissextile

# Affichage des résultats
print("Nombre de secondes dans une année normale :", secondes_par_an)
print("Nombre de secondes dans une année bissextile :", secondes_par_an_bissextile)
