# -*- coding: utf-8 -*-

def indiceMinimum(vec): 
    #To do: Trouve l’indice et la valeur minimum dans un vecteur
    minimum = vec[0]
    # Boucle traversant le vecteur et définissant la valeur minimum
    for position, value in enumerate(vec):
        # Si le premier élément du vecteur est -1
        if minimum == -1:
            minimum = vec[position + 1]
            # Si tout les éléments du vecteur sont -1
            if position == len(vec) - 2 and vec[position + 1] == -1:
                minimum = -1
                break
        # Si un élément est plus petit que le minimum précédent
        if minimum > value and value != -1:
            minimum = value
    # Affectation de l'indice de la valeur minimum
    if minimum == -1:
        indice = -1
    else:
        indice = vec.index(minimum)

    return indice, minimum

def noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis):
    #To do: Cherche le nœud non visité ayant le poids minimum autour d’un nœud spécifique
    #To do: utiliser la fonction indiceMinimum(vec)
    #1) extraire la ligne du noeud de la matrice
    rowN = matrice[noeud]
    # 2) affecter -1 pour chaque noeud des noeuds_vis de la ligne
    for indice in range(len(rowN)):
        for noeudV in noeuds_vis:
            if indice == noeudV:
                matrice[noeud][indice] = -1
    # 3) Trouve l’indice et la valeur minimum de la ligne
    return indiceMinimum(rowN)


def noeudMinimalNonVisites(matrice,noeuds_vis):
    #To do: Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins
    #To do: utiliser la fonction noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    # Liste de Noeud contenant les combinaisons possibles de noeud départ et arrivé et leur poid associé
    listNoeud = []
    for noeud in noeuds_vis:
        indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
        listNoeud.append((noeud, indice, minimum))
    # À partir de la liste de Noeud, recherche du poid minimum possible
    for couple in listNoeud:
        for otherC in listNoeud:
            if couple[2] >= otherC[2] and otherC != -1:
                debut = otherC[0]
                fin = otherC [1]
            if couple[2] < otherC[2] and couple != -1:
                debut = couple[0]
                fin = couple[1]
    return debut, fin

def noeudsVoisins(matrice, noeud):
    #To do: Cherche les nœuds voisins et leur poids par rapport à un nœud initial.
    listNoeudV = []
    listPoid = []
    for index, poids in enumerate(matrice[noeud]):
        if poids != -1:
            listNoeudV.append(index)
            listPoid.append(poids)

    return listNoeudV,listPoid

def dijkstra(matrice, depart, arrive):
    # To do: Calcule le plus court chemin entre un nœud de départ et un nœud d’arrivée.
    # Initialisation de la liste distanMin, de la liste des prédécésseurs et des noeuds visités
    distanceMin = []
    predecesseur = []
    # Comme on commence avec départ, on le considère déjà visité
    noeudVisites = [depart]
    # Ajout d'éléments initiaux dans les listes pour chaque noeud
    for node in range(len(matrice)):
        predecesseur.append(-1)
        if node == depart:
            distanceMin.append(0)
        else:
            distanceMin.append(-1)
    # Début de la boucle de parcours du graphe
    noeudCourant = depart
    while len(noeudVisites) != len(matrice) and noeudCourant != arrive:
        noeudVoisin, poids = noeudsVoisins(matrice,noeudCourant)
        for index,node in enumerate(noeudVoisin):
            distance = distanceMin[noeudCourant] + poids[index]
            if distance < distanceMin[node] or distanceMin[node] == -1:
                distanceMin [node] = distance
                predecesseur [node] = noeudCourant
        debut, fin = noeudMinimalNonVisites(matrice, noeudVisites)
        noeudCourant = fin
        noeudVisites.append(noeudCourant)
    # Fin du traitement de la boucle et modif effectué sur les 3 variables initiales suite au parcours
    distance = distanceMin[arrive]
    return distance, predecesseur

if __name__ == '__main__':
    vec     = [-1, 4, 6, -1, -1, 3, 5]
    indice, minimum = indiceMinimum(vec)
    txt = "la valeur minimale du vecteur est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1, 2, 3]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 1
    noeudsVoisins(matrice, noeud)
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 3
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    depart  = 0
    arrive  = 2
    indice, prédécesseurs = dijkstra(matrice, depart, arrive)
    txt = "la distance la plus cours entre un noeud de départ {} et un noeud d’arrivée {} est {} avec les prédécesseurs {}"
    print(txt.format(depart, arrive, indice, prédécesseurs))
        