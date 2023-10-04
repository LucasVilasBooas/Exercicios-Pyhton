linha1=[]
linha2=[]
linha3=[]
for c in range (0,3):
    linha1.append(int(input("Digite um valor →")))
for c in range (0,3):
    linha2.append(int(input("Digite um valor →")))
for c in range (0,3):
    linha3.append(int(input("Digite um valor →")))
print(linha1)
print(linha2)
print(linha3)


#→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→GUANABARA
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l},{c}] →"))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=" ")
    print()
