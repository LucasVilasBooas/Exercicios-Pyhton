valor = float(input("Digite o valor da compra: "))
formapagamento = int(input("""Digite como deseja pagar
1 - A vista em dinheiro ou cheque com 10% de desconto 
2 - A vista no Cartão com 5% de desconto
3 - No cartao em 2x 
4 - No cartao acima de 3x com juros de 20% \n"""))
if formapagamento == 1:
    print(f"o valor a ser pago é de R${valor * 0.9:.2f} reais")
elif formapagamento == 2:
    print(f"O valor a ser pago é de R${valor * 0.95:.2f} reais")
elif formapagamento == 3:
    print(f"O valor a ser pago é de R${valor} reais sendo 2x{ valor / 2 :.2f}")
elif formapagamento == 4:
    parcelas = int(input("Digite em quantas parcelas quer dividir. "))
    print(f"O valor a ser pago é de R${valor * 1.20 } reais sendo em {parcelas}x{ (valor * 1.20) / parcelas :.2f}")
else:
    print("Opção invalida!")