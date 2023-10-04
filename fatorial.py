"""from math import factorial   >>>>>>>>>>>>>>>>>>>>>>>>>>> FORMA RESUMIDA USANDO O IMPORT
n = int(input("Digite um numero para saber o fatorial "))
f = factorial(n)
print(f"O fatorial de {n} é {f}")
print("*"*30)"""

n = int(input("Digite um numero para saber o fatorial "))
c = n-1
while c > 0:    #for c in range (n, 0, -1):  E RETIRA O CONTADOR PORQUE O FOR JA FAZ A CONTAGEM
    n = n * c
    c = c - 1
print(f"O fatorial é {n}")

"""""
print('x'  if c > 1 else ' = ')
faz com que troque a o caracter
especifico na contagem especifica"""

""" UTILIZANDO O FOR """

