maior = 0
menor = 9999            # se eu coloco uma ordem crescente ele nao sobrescreve este peso
for c in range (0 ,5):  # melhor usar o jeito do guanabara
    n = float(input("DIgite o peso da pessoa "))
    if n > maior :
        maior = n
    elif n < menor:
        menor = n
print(f"O menor peso é {menor} e o maior peso é {maior}")


# JEITO DO GUANABARA

maior = 0
menor = 0
for c in range (0 ,5):
    n = float(input("DIgite o peso da pessoa "))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior :
            maior = n
        elif n < menor:
            menor = n
print(f"O menor peso é {menor} e o maior peso é {maior}")