def area(c, l):
    area = c * l
    print(f'A area de um terreno {l}x{c} é de {area}m².')


print('Digite a largura e comprimento da aera')
l = float(input('LARGURA (m) →'))
c = float(input('COMPRIMENTO (m) →'))
area(l, c)
