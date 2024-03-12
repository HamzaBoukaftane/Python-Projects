# Initilisation des variables 

capital_initiale=300000 # capital initial en dollars
taux_annuel=0.08 # taux d'intérêt annuel

# Calcul du capital au bout de 20 années

nombre_année=0 #la durée du placement en année
for nombre_année in range(20):
    capital_initiale= capital_initiale + capital_initiale * taux_annuel

# Affichage du capital au bout de 20 années

print("Valeur du capital au bout de 20 années:", round(capital_initiale,2),'$')

