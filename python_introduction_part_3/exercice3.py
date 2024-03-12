def compute_pi(p):
    result = 0
    n = 0
    old_result = 0
    precision = 10 ** -p
    # TODO calculer la valeur de pi d'après la formule donnée dans l'énoncé
    spread=1
    while spread>precision:
        somme_terme=(4*((-1)**n)*(1/(2*n+1)))
        result+=somme_terme
        spread=abs(somme_terme)
        n+=1
    return result, n

if __name__ == '__main__':
    # Calcul de π (pi)
    pi = 3.141592653589793
    p = 5
    computed_pi , nb_iter = compute_pi(p)
    print("La valeur réel de pi est : {}".format(pi))
    print("La valeur approché de pi à 10e-{} est : {}".format(p, computed_pi))
    print("Résultat obtenu après {} itérations".format(nb_iter))