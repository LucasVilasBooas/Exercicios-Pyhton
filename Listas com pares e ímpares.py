lista = [[], []]
x = 0
for c in range (0,7):
    x = int(input("Digite um numero →"))
    if x % 2 == 0 :
        lista[0].append(x)
    else:
        lista[1].append(x)
print()
lista[0].sort()
lista[1].sort()
print(f"os valores pares digitados sao {lista[0]}")
print(f"os valores impares digitados sao {lista[1]}")
