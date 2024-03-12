# Initialisation des variables

capital = 8000 # capital initial en dollars
nb_jours = 72 # durée du placement en jours
taux_annuel = 0.065# taux d'intérêt annuel pourcentage / 100

# Calcul du taux intérêt périodique

taux_périodique = taux_annuel / 365

# Calcul des intérêts 

intérêt= capital * nb_jours * taux_périodique


# Calcul de la valeur acquise

valeur_acquise= intérêt + capital


# Affichage des interets et de la valeur acquise
print('Les intérêts gagnés après 72 jours sont:',round(intérêt,2),'$')

print('La valeur acquise après 72 jours est:', round(valeur_acquise,2), '$')

