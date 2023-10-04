n1 = int(input("Digite um valor "))
n2 = int(input("Digite um valor "))
n3 = int(input("Digite um valor "))
n4 = int(input("Digite um valor "))     #ele faz direto na tupla LEMBRANDO QUE TEM QUE POR TUDO EM  (  ) 
lista = (n1, n2, n3, n4)   # -> lista = (int(input('Digite um numero '), ('Digite um numero '), ('Digite um numero '), ('Digite um numero ')
print("*-"*20)
if 9 in lista:
    print(f'O numero 9 foi digitado {lista.count(9)} vezes')   #se eu nao colocar o 9 na digitação da erro
else:
    print('O valor 9 nao foi digitado ')
print("*-"*20)
if 3 in lista:
    print(f'O numero 3 esta na posição {lista.index(3)+1}')    #se eu nao colocar o 3 na digitaçã da erro ===== feito a correção com o if
else:
    print('O valor 3 nao foi digitado ')
print("*-"*20)
print("Os numeros Pares digitados são ", end=" ")
for c in lista:
    if c % 2 == 0:
        print(c, end=", ")
print()
print("*-"*20)
print("***FIM PROGRAMA***")



