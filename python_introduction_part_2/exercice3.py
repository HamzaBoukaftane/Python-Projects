import math
def decomposer(secondes):
# annee-sec = 31 536 000
# semaine-sec = 604 800
# jours-sec = 86400
# heure-sec = 3600
# min-sec = 60
    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = math.floor(secondes / 31536000)

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes

    reste_secondes = secondes % 31536000
    semaines = math.floor(reste_secondes / 604800)

    # TODO: Assigner à la variable "jours" le nombre de jours restants

    reste_secondes = reste_secondes % 604800
    jours = math.floor(reste_secondes / 86400)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes

    reste_secondes = reste_secondes % 86400
    heures = math.floor(reste_secondes / 3600)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes

    reste_secondes =reste_secondes % 3600
    minutes = math.floor(reste_secondes / 60)

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes

    reste_secondes = reste_secondes % 60
    secondes =math.floor(reste_secondes)

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes

    print(annees," ans ,",semaines," semaines, ",jours," jours, ",heures," heures, " ,minutes," minutes et " ,secondes,"secondes. ")
    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
