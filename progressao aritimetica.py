x = int(input("Digite um numero "))
r = int(input("Digite a razao "))
print(f"{x}", end=" ->")
for c in range (1,10):
    x = x + r
    print(x, end=" ->")