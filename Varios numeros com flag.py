soma = cont = 0
while True:
    n= int(input("Digite um valor [999] para parar o programa"))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"Foram digitados {cont} numeros e a soma deles é {soma}")