n50 = n20 = n10 = n1 =  0
valor = int(input("Digite o valor que deseja saca: R$"))
n50 = valor // 50
valor = valor - (n50*50)
n20 = valor // 20
valor = valor - (n20*20)
n10 = valor // 10
valor = valor - (n10*10)
n1 = valor // 1
print("*-"*30)
if n50 > 0:
    print(f"Total de {n50} cedulas de R$50")
if n20 > 0:
    print(f"Total de {n20} cedulas de R$20")
if n10 > 0:
    print(f"Total de {n10} cedulas de R$10")
if n1 > 0:
    print(f"Total de {n1} cedulas de R$1")
print("*-"*30)
print("Obrigado por usar nosso Banco")

print()
print()
print()

print("BANCO DO GUANABARA")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
valor = int(input("que valor quer sacar? R$"))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cedulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("volte sempre")

