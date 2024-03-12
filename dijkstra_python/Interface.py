# -*- coding: utf-8 -*-

import random

def saisirMatrice():
    #To do: Saisit une matrice d’adjacence au clavier
    # Initialisation de la matrice
    matrice = []
    # Sélection du nombre de noeuds
    nbNoeuds = input('Donner le nombre de noeuds dans la matrice:')
    # Initialisation des noeuds dans la matrice
    for i in range(int(nbNoeuds)):
        matrice.append([-1 for x in range(int(nbNoeuds))])
    # Sélection du nombre de noeuds
    nbPoid = input('Donner le nombre de poids dans la matrice:')
    #création liste de nombre de poids
    listNbPoid = []
    nb = 0
    while nb < int(nbPoid):
        listNbPoid.append(nb)
        nb += 1
    # Sélection des valeurs de poid entre noeuds choisis
    for poid in listNbPoid:
        print (f"   Saisir le poids {poid}")
        firstNode = int(input("      Donner le noeud dextrémité 1:" ))
        secondNode = int(input("      Donner le noeud dextrémité 2:" ))
        weightValue = int(input("      Saisir le poids:" ))
        # On implémente les nouvelles valeurs à la matrice
        matrice [firstNode][secondNode] = weightValue
        matrice [secondNode][firstNode] = weightValue
    return matrice

def genereMatriceAleatoire(nb_noeuds):
    #To do: Génère une matrice d’adjacence de manière aléatoire
    matrice = []
    # Initialisation des noeuds dans la matrice
    for i in range(nb_noeuds):
        matrice.append([-1 for x in range(nb_noeuds)])
    # Sélection des valeurs de poid entre noeuds choisis
    for noeud in range(nb_noeuds//2):
        firstNode = noeud
        for otherN in range((nb_noeuds//2), nb_noeuds):
            secondNode = otherN
            weightValue = random.randint(1,99)
            # On implémente les nouvelles valeurs à la matrice
            matrice[firstNode][secondNode] = weightValue
            matrice[secondNode][firstNode] = weightValue
    if nb_noeuds%2 != 0:
        rNb = random.randint(1,99)
        matrice[nb_noeuds//2][len(matrice)-1] = rNb
        matrice[len(matrice) - 1][nb_noeuds // 2] = rNb
    return matrice

def afficheChemin(predecesseurs, depart, arrive):
    #To do: Affiche le chemin entre un nœud de départ et d’arrivé à partir du tableau de prédécesseurs
    listchemin = []
    while depart not in listchemin:
        listchemin.append(arrive)
        if arrive != depart:
            listchemin.append(predecesseurs[arrive])
            arrive = predecesseurs[predecesseurs[arrive]]
    listchemin.reverse()
    for index, element in enumerate(listchemin):
        listchemin[index] = str(element)
    affichage = f"Le chemin à parcourir est:\n\tDEBUT : {'  ==> '.join(listchemin)}: FIN \n"
    return affichage


if __name__ == '__main__':
    saisirMatrice()
    
    nb_noeuds = 5
    matAlea = genereMatriceAleatoire(nb_noeuds)
    txt = "la matrice aleatoire est: \n\t"
    for i in matAlea:
        for j in i:
            txt += "{}\t".format(j)
        txt += "\n\t"
    print(txt)
    
    predecesseurs = [-1, 0, 0, 2, 5, 2]
    depart = 0
    arrive = 4
    afficheChemin(predecesseurs, depart, arrive)
