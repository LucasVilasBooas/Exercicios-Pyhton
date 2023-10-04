lista =[]
while True:
    '''x = int(input("Digite um valor →"))
    lista.append(x)      TROQUEI  POR '''
    lista.append(int(input('Digite um valor ')))
    cont = str(input("Deseja continuar? ")).upper().strip()
    if cont !='S':
        break

print(f'foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f"A sua lista em ordem decressente é {lista}")
if 5 in lista:
    print("o valor 5 foi digitado na lista")
else:
    print("O valor 5 nao foi digitado na lista")