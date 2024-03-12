import math

def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.

    # convertir les km\h en m\s
    vitesseI_m = vitesseInitiale * 1000 / 3600
    vitesseF_m = vitesseFinale * 1000 / 3600
    # calculer acceleration
    acceleration = (vitesseF_m - vitesseI_m) / duree

    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = positionInitiale+ (vitesseI_m * duree + 0.5 * acceleration * duree**2 )

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
