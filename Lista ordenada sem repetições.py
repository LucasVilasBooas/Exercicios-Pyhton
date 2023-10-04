lista = []
for c in range(0,5):
    n = int(input("Digite um valor "))
    if c==0 or n>lista[-1]:       #lista-1 é o meu ultimo numero ou poderia ter usado o len
        lista.append(n)
        print("Adicionado no final da lista ...")
    else:
        pos = 0
        while pos < len(lista): # poderia ter usado o lista-1
            if n <= lista[pos]:
                lista.insert(pos, n) #inserir na posição o numero ex→(3, 2)
                print(f"Adicionado na posição {pos} da lista ...")
                break
            pos += 1
print('*-'*20)
print(f'Os valores digitados em ordem foram {lista}')
