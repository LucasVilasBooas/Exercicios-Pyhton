valorcasa = float(input("Qual o valor da casa? "))
salariocomprador = float(input("Qual o salario do comprador? "))
tempo = int(input("EM quantos anos a casa vai ser paga? "))
if valorcasa/(tempo*12) > 0.30*salariocomprador:
    print(f"Seu pedido foi negado")
else:
    print(f"Seu emprestimo foi aprovado.")
    print(f"O valor da parcela é de R${valorcasa/(tempo*12):.2f} e sera pago em {tempo*12} parcelas")