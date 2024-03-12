# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Creer le      : 26 février 2022
# Creer par     : Hamza Boukaftane
# Version num   : 2
# Modifier le   : 8 mars 2022


import matplotlib.pyplot as plt
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules
from Molecule import ajusteDirApresCollision, inverseDirMolecule



def creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD):
    #TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)
    reservoir= {"h": hauteur,
                "l": largeur,
                "posPar": posParoi,
                "mG": creerListMolecules(hauteur,0,posParoi,nbMoleculesG),
                "mD": creerListMolecules(hauteur, posParoi , largeur ,nbMoleculesD),
                "lCG": [ 0 for i in range(int(nbMoleculesG * (nbMoleculesG - 1) / 2)) ],
                "lCD": [ 0 for i in range(int(nbMoleculesD * (nbMoleculesD - 1) / 2)) ] }

    return reservoir

def colision(reservoir):
    #TODO 3.2.2 Vérifier si il y a des collisions entre des molécules dans un réservoir
    # Pour chaque molécule vérifier si elles est en collision avec une autre molécule du réservoir
    # Réservoir de gauche
    lCGCompteur=0
    for i,mG in list(enumerate(reservoir["mG"]))[:-1]:
        for j,otherMG in list(enumerate(reservoir["mG"]))[i + 1:]:
            if  moleculesSeTouche(mG,otherMG):
                ajusteDirApresCollision(mG,otherMG)
                reservoir["lCG"][lCGCompteur] = 1
                reservoir["mG"][i] = mG
                reservoir["mG"][j]= otherMG
            lCGCompteur += 1

    # Réservoir de droite
    lCDCompteur = 0
    for a, mD in list(enumerate(reservoir["mD"]))[:-1]:
        for b, otherMD in list(enumerate(reservoir["mD"]))[a + 1:]:
            if moleculesSeTouche(mD, otherMD):
                ajusteDirApresCollision(mD, otherMD)
                reservoir["lCD"][lCDCompteur] = 1
                reservoir["mD"][a] = mD
                reservoir["mD"][b] = otherMD
            lCDCompteur += 1

    # Retourne les nouveaux paramètres des molécules après collision
    return reservoir


def inverseDirMolecules(reservoir):
    #TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
    # Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)
    for i,mG in list(enumerate(reservoir["mG"])):
        inverseDirMolecule(mG, 0, reservoir["posPar"], reservoir["h"])
        reservoir["mG"][i] = mG

    for j,mD in list(enumerate(reservoir["mD"])):
        inverseDirMolecule(mD, reservoir["posPar"], reservoir["l"] , reservoir["h"])
        reservoir["mD"][j] = mD

    return reservoir

def getTemperature(reservoir, cote):
    #TODO 3.2.4 Calcule la température de chaque côté du réservoir.
    # Utiliser la formule dans le Readme
    def vitesseMolecule(mol):
        v = (mol["dx"] ** 2 + mol["dy"] ** 2) ** (1/2)
        return v

    def energieG(reservoir):
        energieG = 0
        for molG in range(len(reservoir["mG"])):
            energieG += 0.5*(vitesseMolecule(reservoir["mG"][molG]) ** 2)
        return energieG

    def energieD(reservoir):
        energieD = 0
        for molD in range(len(reservoir["mD"])):
            energieD += 0.5*(vitesseMolecule(reservoir["mD"][molD]) ** 2)
        return energieD

    dictTemp={"Droite": energieD(reservoir)/ len(reservoir["mD"]),
              "Droit": energieD(reservoir) / len(reservoir["mD"]),
              "Gauche": energieG(reservoir)/len(reservoir["mG"])
             }

    return dictTemp[cote]

#####################################################
# Donner
#####################################################
def affichage(reservoir, ax):
    txt = "Température côté Gauche: {:.2f}C \t\t\t\t\t Température côté Droit: {:.2f}C".expandtabs()

    ax.plot([reservoir['posPar'], reservoir['posPar']], [0, reservoir['h']], 'k-', linewidth=10)
    ax.axis([-20, reservoir['l'] + 20, -20, reservoir['h'] + 20])
    ax.title.set_text(txt.format(getTemperature(reservoir, "Gauche"), getTemperature(reservoir, "Droit")))

    for k in [['mG', 'ro'], ['mD', 'go']]:
        for i in range(len(reservoir[k[0]])):
            inte = min(max((abs(reservoir[k[0]][i]['dx']) + abs(reservoir[k[0]][i]['dy'])) / 60, 0.2), 1)
            ax.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha=inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])

    plt.pause(0.01)
    clear_output() 
    

def deplacerMolecules(reservoir, ax):
    # TODO 3.2.6
    # deplacer_molecule deplace les molecules du reservoir
    # Cette function recoit comme parametre un objet de type reservoire est execute les etapes suivantes:
    # 1) Inverser la direction des molecules du reservoir
    inverseDirMolecules(reservoir)
    # 2) Afficher les molecules
    affichage(reservoir, ax)
    # 3) Determination des colision des molecules
    colision(reservoir)

    return reservoir

if __name__ == '__main__':
    hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD = 2000, 2000, 1300, 30, 30
    reservoir = creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD)
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot()
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir, ax)
        ax.clear()