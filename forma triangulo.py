l1 = int(input("Digite o tamanho do primeiro lado do triangulo: "))
l2 = int(input("Digite o tamanho do segundo lado do triangulo: "))
l3 = int(input("Digite o tamanho do terceiro lado do triangulo: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l3:
    print("Os tamanhos acima podem formar um triangulo! ")
else:
    print("Os tamanhos acima nao pode formar um triangulo! ")