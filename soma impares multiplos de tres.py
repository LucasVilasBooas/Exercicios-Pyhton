n = 0
cont =0
for c in range (1, 501, 2):
    if c % 3 == 0:
        n = n + c
        cont = cont + 1
print(f"a soma de {cont} valores é {n} ")
