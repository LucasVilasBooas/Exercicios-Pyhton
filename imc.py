peso = float(input("Digite seu peso em Kg. "))
altura = float(input("Digite sua altura em metros. "))
imc = peso / (altura**2)
print(f"Seu IMC é de {imc:.2f}")
if imc < 18.5:
    print("Voce esta abaixo do peso")
elif 18.5 <= imc == 25:
    print("Voce esta na faixa de peso ideal")
elif 25 <= imc == 30:
    print("Voce esta com sobre peso")
elif 30 <= imc == 40:
    print("Voce esta com obesidade")
elif  imc > 40:
    print("Voce esta com obesidade morbida")