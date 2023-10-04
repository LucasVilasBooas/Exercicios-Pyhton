nome = str(input('digite seu nume completo: ')) .strip() # retira os espaços da frase na contagem
print (f'seu nome em maiusculas é',nome.upper())
print(f'seu nome me minusculas é {nome.lower()}')
print('*¨' * 30)
print(f"seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print (f'seu primeiro nome tem {nome.find(" ")} letras')
print('*¨' * 30)
separa = nome.split()
print(f"seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")
