import random
n1 = str(input("Digite o nome do primeiro aluno "))
n2 = str(input("Digite o nome do segundo aluno "))
n3 = str(input("Digite o nome do terceiro aluno "))
n4 = str(input("Digite o nome do quarto aluno "))
n5 = str(input("Digite o nome do quinto aluno "))
lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")
random.shuffle(lista)
print()
print(f"A ordem da apresentação sera: ")
print(lista)
