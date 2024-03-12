from abc import abstractmethod, ABC
from typing import List, Tuple

from accessoire import Accessoire, TypeAccessoire
from elements_tiktok import ElementViral


# TODO Je suis abstraite et j'hérite de ElementViral
class Animal(ElementViral,ABC):
    # TODO Implantez mon constructeur
    def __init__(self, nom : str, nb_pattes : int) -> None:
        self.nom = nom
        self.nb_pattes = nb_pattes
        self.liste_accessoires : List[Accessoire] = []

    def __add__(self, accessoire: Accessoire) -> int:
        # TODO Retournez le score viral de l'animal plus celui de l'accessoire
        return self.score_viral() + accessoire.score_viral()

    def __iadd__(self, accessoire: Accessoire) -> 'Animal':
        # TODO Ajoutez l'accessoire à la liste de l'animal. Retournez l'animal en question
        #  Attention! Un animal n'ayant aucune patte ne peut enfiler des chaussures
        if accessoire.type_accessoire == TypeAccessoire.CHAUSSURES and self.nb_pattes == 0:
            print("Vous ne pouvez pas mettre de chaussures à un animal sans pieds")
        else:
            self.liste_accessoires.append(accessoire)
        return self

    @abstractmethod
    def crier(self) -> str:
        # TODO Rendez-moi abstraite
        pass

    def score_viral(self) -> int:
        # TODO Retournez la somme du score viral des accessoires présents dans la liste d'accessoires de l'animal
        somme = 0
        for accessoire in self.liste_accessoires:
            somme += accessoire.score_viral()
        return int(somme)


def calcul_meilleur_animal(animaux: List[Animal]) -> Tuple[str, int]:
    # TODO Retournez le nom et le score viral de l'animal ayant le score le plus haut
    data = {}
    for animal in animaux:
        if animal.liste_accessoires == []:
            data.update({animal.nom : 0})
        else:
            data.update({animal.nom: animal.score_viral()})
    max_score = max(data.values())
    key = [k for k,v in data.items() if v==max_score ]
    return key[0], max_score

