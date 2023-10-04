r1 = float(input("Digite o primeiro segmento "))
r2 = float(input("Digite o segundo segmento "))
r3 = float(input("Digite o terceiro segmento "))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1+ r2 :
    print("Os segmentos podem formar um triangulo")
    if r1 == r2 == r3 :
        print("os segmentos formam um triangulo equilatero")
    elif r1 != r2 != r3 != r1:
        print("os segmentos formam um triangulo escaleno ")
    else :
        print("Os segmentos formam um triangulo isoceles")
else :
    print("os segmentos nao formam um trialgulo")

