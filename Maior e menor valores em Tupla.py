from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Sortiei os valores {n}')
print()

print('Sortiei os valores ', end=" ")
for c in n:                      # so usa o c  porque ja esta sendo no proprio N
    print(f'{c}', end=" ")       # por isso nao precisa colocar {n[c]} -> seria como subir para cima

print()
print("*-"*30)
print(f'O maior valor sorteado foi {max(n)}')
print()
print(f'O maior valor sorteado foi {min(n)}')
print()
print("***FIM PROGRAMA***")