valor = 0
num = [[], []]         
for c in range(1, 8): 
    valor = int(input('Digite o {} valor: '.format(c)))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('-='*30)
print(f' Os valores digitados pares são: {num[0]}')
print(f' Os valores digitados ímpares são: {num[1]}')