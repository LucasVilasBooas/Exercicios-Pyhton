soma = 0
cont = 0
for c in range (1,7):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print(f"Voce informou {cont} numeros pares e a soma deles é {soma}")