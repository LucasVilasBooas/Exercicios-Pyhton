n = 7
vet : [int] = [ 0 for i in range(n)]
for i in range(0, n):
    vet[i] = int(input("digite um valor: "))
print()
print("numeros pares:")
for i in range(0, n):
    if vet[i] % 2 == 0:
            print(f"{vet[i]} ", end="")
print()
print("numeros impares")
for i in range(0, n):
    if vet[i] % 2 != 0:
            print(vet[i])