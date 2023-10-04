n = int(input("Digite um numero: "))
base = int(input("""Escolha as opções abaixo
                 1 - binarios
                 2 - octadecimal
                 3 - hexadecimal \n"""))
if base == 1:
    print(f"{n} convertido em binario é {bin(n)[2:]}")
elif base == 2:
    print(f"{n} convertido octadecial é {oct(n)}[2:]")
elif base == 3:
    print(f"{n} convertido em hexadecial é {hex(n)}[2:]")
else:
    print("Opção invalida!")