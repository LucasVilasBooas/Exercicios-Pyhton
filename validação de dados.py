sexo = str(input("Digite seu sexo ")).strip()[0] # o [] serve para pegar somente a primeira letra
while sexo != "M" and sexo != "m" and sexo != "f" and   sexo != "F": # while sexo not in 'MmFf'   substitui todos os AND's
    print("Entrada incorreta. Tente novamente.")
    sexo = str(input("Digite seu sexo ")).strip()[0]
print("Registro completo")
print("FIM")