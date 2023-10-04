op = 0
resultado = 0
n1 = int(input("Digite um valor "))
n2 = int(input("Digite mais um valor "))
while op != 5:
    print("""   [1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA""")
    op = int(input("Oque deseja fazer? "))
    if op == 1:
        resultado = n1 + n2
        print(f"a soma entre ele é {resultado}")
        print()
    elif op == 2:
        resultado = n1 * n2
        print(f"a multiplicação entre eles é {resultado}")
        print()
    elif op == 3:
        if n1 > n2:
            print(f"O maior numero é {n1}")
            print()
        else:
            print(f"O maior numero é {n2}")
            print()
    elif op == 4:
        n1 = int(input("Digite um valor "))
        n2 = int(input("Digite mais um valor "))
    elif op ==5:
        print("Finalizando.....")
    else:
        print("OPERAÇÂO NAO CADASTRADA, Tente novamente")
    print("/*-"*20)
