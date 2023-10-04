x = int(input("Digite um numero "))
r = int(input("Digite a razao "))
print(f"{x}", end=" ->")
c = 1
while c < 10:
    x = x + r
    print(x, end=" ->")
    c+= 1
print('->FIM<-')