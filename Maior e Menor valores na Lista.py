from operator import index

lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor para a posição {c}→ ")))
    if c == 0:
        maior = menor = lista[c]
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]

print(f"Voce digitou os valores {lista}")

#usa para mostrar a posição tambem mas so vai mostrar o primeiro
print(f"o maior valor foi {maior} e estava na posição {lista.index(maior)}")
print(f"o menor valor foi {menor} e estava na posição {lista.index(menor)}")

print()
print(f"o maior valor foi {maior} e estava na posição ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end="")
print()
print(f"o menor valor foi {menor} e estava na posição ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end="")