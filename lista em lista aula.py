lista = []
temp = []
while True:
    temp.append(str(input("Digite o nome: →")))
    temp.append(float(input("Digite o peso: →")))
    lista.append(temp[:])
    temp.clear()
    adc = str(input("Deseja cadastrar outras pessoa? [S] para Sim ")).upper().strip()
    if adc != "S":
        break
print(f'A quantidade de pessoas cadastradas foi {len(lista)}')
print("pessoas acima do peso sao ", end="")
for p in lista:
    if p[1] > 70:
        print(f'{p[0]} ', end=" ")
print()
print("Pessoas abaixo do peso sao ", end="")
for p in lista:
    if p[1] <=70:
        print(f'{p[0]} ', end="")
print()
print('>>>>FIM PROGRAMA<<<<')