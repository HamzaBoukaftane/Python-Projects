# Initialisation des variables

capital_1= 2600 # capital du premier placement en dollars
taux_annuel_1=0.045 #taux d'intérêt annuel premier placement
capital_2= 2600 - 60 # capital du deuxième placement en dollars
taux_annuel_2=0.1 #pourcentage par an
nombre_jour_1=100 # nombre de jours
nombre_jour_2=300 # nombre de jours

# Calcul du montant du capital avec le premier placement au 100ème jour de l'année 

montant_1= capital_1 * taux_annuel_1 / 365 * nombre_jour_1 + capital_1

# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année 

montant_2= capital_2 * taux_annuel_2 / 365 * nombre_jour_2 + capital_2

# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le premier

nombre_jour_3=0 #nombre de jours
while nombre_jour_3>=0 :
    nombre_jour_3 += 1
    valeur_acquise_placement_1= capital_1 * taux_annuel_1 / 365 * nombre_jour_3 + capital_1
    valeur_acquise_placement_2= capital_2 * taux_annuel_2 / 365 * nombre_jour_3 + capital_2
    if valeur_acquise_placement_2>=valeur_acquise_placement_1 :
        break

# Affichage des valeurs calculées
print("Le montant du capital du premier placement au 100ème jour est:", round(montant_1, 2), '$')

print("Le montant du capital du deuxième placement au 300ème jour est:", round(montant_2, 2), '$')
import math
print("Le deuxième placement est supérieur au premier placement à partir du", math.ceil(nombre_jour_3), 'ième jour.')

