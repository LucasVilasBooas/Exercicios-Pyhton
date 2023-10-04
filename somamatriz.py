l= int(input("Digite a quantidade de LINHAS da matriz: "))
c= int(input("Digite a quantidade de COLUNAS da matriz: "))

a : [[int]] =[[0 for x in range(c)]  for x in range(l)]
b : [[int]] =[[0 for x in range(c)]  for x in range(l)]
d : [[int]] =[[0 for x in range(c)]  for x in range(l)]

print('-*'*30)
print("digite os valores da marriz A ")
for i in range(0,l):
    for j in range(0,c):
        a[i][j]= input(f"elemento [{i},{j}]:")

print('-*'*30)
print("digite os valores da marriz B ")
for i in range(0,l):
    for j in range(0,c):
        b[i][j]= input(f"elemento [{i},{j}]:")

for i in range(l):
    for j in range(c):
        d[i][j] = a[i][j] + b[i][j]


print('-*'*30)
for i in range(l):
    for j in range(c):
        print(f"{d[i][j]}", end="")
    print()
