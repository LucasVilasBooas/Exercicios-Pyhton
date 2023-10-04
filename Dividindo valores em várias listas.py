lista = []
listapar = []
listaimpar =[]
while True:
    lista.append(int(input('Digite um valor →')))
    mais = str(input("Deseja continuar? [S] Continuar →")).upper().strip()
    if mais != 'S':
        break                       #→→→→→JEITO DO GUANABARA←←←←←←
for c in range(len(lista)):         #for i, v in enumerate(lista) //
    if lista[c] % 2 == 0:           #   if v % 2 == 0:
        listapar.append(lista[c])   # restante igual listapar.append(v)
    else:
        listaimpar.append(lista[c])
lista.sort()
print(f'Sua lista em ordem crescennte é {lista}')
print(f'lista par {listapar}')
print(f'lista impar {listaimpar}')