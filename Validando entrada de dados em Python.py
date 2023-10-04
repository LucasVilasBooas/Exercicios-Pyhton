def leiaInt():
    n = str(input("Digite um numero "))
    while True:
        if n.isnumeric():
            return f'O numero digitado foi {n}'
        else:
            print('Isso nao é um numero, DIGITE APENAS NUMEROS')
            n = str(input("Digite um numero "))


print(leiaInt())