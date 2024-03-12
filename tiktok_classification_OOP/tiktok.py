import json
from typing import List, Union

import elements_tiktok
from animal import Animal
from elements_tiktok import Musique, Filtre


class TikTok:
    # TODO Implantez mon constructeur
    def __init__(self, titre:str) -> None:
        self.titre = titre
        self.musique = elements_tiktok.Musique
        self.filtre = elements_tiktok.Filtre
        self.__animaux : List[Animal] = []

    def ajouter_animal(self, animal: Animal) -> 'TikTok':
    # TODO Ajoutez l'animal à la liste et retournez le TikTok mis à jour
        self.__animaux.append(animal)
        return self

    def __lt__(self, autre_tiktok: 'TikTok') -> bool:
        # TODO Surchargez l'opérateur < entre deux objets de type TikToks
        #  Retourne True si le présent TikTok a moins de vues que autre_tiktok
        #  Retourne False sinon
        if self.vues < autre_tiktok.vues:
            return True
        if self.vues > autre_tiktok.vues:
            return False

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  TITRE (NOMBRE_DE_VUES vues)
        return f"{self.titre} ({self.vues} vues)"

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    @property
    def vues(self) -> int:
        # TODO Retournez le nombre de vues de votre TikTok selon la formule suivante:
        #  vues = SCORE_MUSIQUE + SCORE_FILTRE + NOMBRE_ANIMAUX* SOMME(SCORE_ANIMAUX)
        score_musique = self.musique.score_viral()
        score_filtre = self.filtre.score_viral()
        nb_animaux = 0
        somme = 0
        for animal in self.__animaux:
            nb_animaux += 1
            somme += animal.score_viral()
        vues = score_musique + score_filtre+ nb_animaux* somme
        return vues


    def to_json(self):
        # Ne pas modifier
        return json.dumps({
            'titre': self.titre,
            'vues': self.vues,
            'musique': self.musique.titre,
            'filtre': self.filtre.nom,
            'animaux': [
                {
                    'nom': animal.nom,
                    'espèce': type(animal).__name__,
                    'accessoires': [
                        {
                            'nom': accessoire.nom,
                            'type': str(accessoire.type_accessoire)
                        } for accessoire in animal.liste_accessoires
                    ]
                } for animal in self.__animaux
            ]
        }, ensure_ascii=False)


class CompteTikTok:

    # TODO Implantez mon constructeur
    def __init__(self, identifiant: str) -> None:
        self.identifiant = identifiant
        self._CompteTikTok__tiktoks : List[TikTok] = []

    def __len__(self) -> int:
        # TODO Surchargez l'opérateur len pour que len(COMPTE_TIKTOK) retourne le nombre de tiktok du compte
        return len(self._CompteTikTok__tiktoks)

    def __iadd__(self, tiktok: TikTok) -> 'CompteTikTok':
        # TODO Surchargez l'opérateur += pour permettre d'ajouter un TikTok à la liste du compte
        #  Doit retourner le compte mis à jour
        self._CompteTikTok__tiktoks.append(tiktok)
        return self

    @property
    def vues(self) -> int:
        # TODO Retourne le nombre de vues cumulatives du compte c'est à dire la somme des vues des différents TikToks
        somme_vues = 0
        for tiktok in self._CompteTikTok__tiktoks:
           if len(self._CompteTikTok__tiktoks) != None:
                somme_vues += tiktok.vues
        return somme_vues

    def tiktoks_plus_populaires(self) -> List[TikTok]:
        # TODO Retourne une liste triée des TikToks du compte en ordre décroissant de vues
        liste_a_trier = [i for i in self._CompteTikTok__tiktoks]
        listetrier = []
        while len(liste_a_trier) != 1:
            for tiktok in liste_a_trier:
                for other in liste_a_trier:
                    if tiktok > other:
                        max = tiktok
                    if other > tiktok:
                        max = other
                listetrier.append(max)
                liste_a_trier.remove(max)
        listetrier.append(liste_a_trier[0])
        return listetrier

