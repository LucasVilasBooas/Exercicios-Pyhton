def fatorial(n, show=False):
    """
    Calcular o FATORIAL de um numero
    :param n: Numero que vai ter o fatorial feito
    :param show: mostrar ou nao o calculo
    :return: mostrar o valor do fatorial do numero N
    """
    f=1
    for c in range (n, 0, -1):
        if show:
            print(c, end="")
            if c>1:
                print(' x ', end="")
            else:
                print(" = ")
        f *= c
    return f

print(fatorial(5, show=True)) # show TRUE é para mostrar a conta inicialmente ele vem como show FALSE