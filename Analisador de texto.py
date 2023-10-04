nome = str(input("Digite o nome completo: "))
print(f"o seu nome todo em maiusculo é {nome.upper()}")
print(f"O seu nome todo em minusculo é {nome.lower()}")
print(f"o seu nome tem ao todo {len(nome) - nome.count(' ')}")
print(f"o seu primeiro nome tem {nome.find(' ')} letras")
print()
separa = nome.split() # o nome completo vai ser escrito por blocos
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras") # len é usado para contar quantos caracteres
