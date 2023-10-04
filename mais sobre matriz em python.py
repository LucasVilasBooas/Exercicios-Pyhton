matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l},{c}] →"))
print('*-'*15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=" ")
        if matriz[l][c] % 2 ==0:
            spar += matriz[l][c]
    print()
for l in range(0,3):
    scol += matriz[l][2]
for c in range (0,3)
    if c==0:
        mai = matriz[1][c]
    elif matriz[1[c]] > mai:
        mais = matriz[1][c]
print('*-'*15)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da tercerira coluna é {scol}')
print(f'O maior valor da segunda linha é {mai}')