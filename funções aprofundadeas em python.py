def leiaInt(msg):
    while True:
        try:
          n = int(input(msg))
        except :
            print('\033[31mERRO! Por favor digite um numero inteiro valido!\033[m')
            continue
        else:
            return f"o numero é {n}"



def leiaFloat(msg):
    while True:
        try:
          n = float(input(msg))
        except :
            print('\033[32mPor favor digite um numero real valido!\033[m')
            continue
        else:
            return f"o numero é {n}"

num1 = leiaInt("Digite um valor")
num2 = leiaFloat("Digite um valor real")
print(f'O numero inteiro foi {num1} ')
print(f"O numero real foi {num2}")