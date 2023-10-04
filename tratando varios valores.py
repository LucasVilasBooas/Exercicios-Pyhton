soma = n = cont = 0
n = int(input("Digite um valor : [999] PARA PARAR "))
while n < 999:
    soma += n
    n = int(input("Digite um valor : [999] PARA PARAR "))
    cont += 1 # A ORDEM NAO DEIXA ELE ADICIONAR O VALOR NA VARIAVEL
print()
print(f"Foram digitados {cont} numeros e a soma entre eles foi {soma}")
