tulipa = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez','onze','doze', 'treze', 'quatorze', 'quinze', 'desseis', 'dessete', 'dezoito', 'dezenove', 'vinte' )
continuar = "S"
while True:
    n = int(input("Digite um numero entre 0 e 20 "))
    if 0 < n >20:
        n = int(input("Valor nao suportado. Digite um numero entre 0 e 20 -> "))
    print(tulipa[n])
    continuar = str(input("[S] Para continuar pressione \n"
                          "Pressione outro botão para sair.  ")).upper().strip()[0]
    if continuar != "S":
        break
