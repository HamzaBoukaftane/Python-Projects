
def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat et retourner celle-ci avec le mot-clé return.

    if (n % (3 * 5)) == 0:
        resultat=("FizzBuzz")

    elif ( n % 3) == 0 :
        resultat =("Fizz")

    elif ( n % 5 ) == 0 :
        resultat =("Buzz")

    else:
        resultat = ( str(n) + " est ni un multiple de 3 ni un multiple de 5!" )

    print(resultat)
    return resultat
if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))

    fizzBuzz(n)


