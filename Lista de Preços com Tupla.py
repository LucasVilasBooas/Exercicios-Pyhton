listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.30,
            'Livro', 34.90)
print('--'*19)
print(F'{"LISTAGEM DE PREÇOS":^40}') # ARTIFICIO USADO PARA DEIXAR ELE COM 40 CASAS E CENTRALIZADO
print('--'*19)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end="")
    else:
        print(f'R${listagem[pos]:>7.2f}') # :>5 É PARA USAR 5 CASAS DECIMAIS A ESQUERDA E O 2.f É PARA USAR 2 CASAS DECIMAIS NO FLOAT

print('--'*20)