try:                                 #fazer tentativas para saber os possiveis erros
    a = int(input("numerador"))
    b = int(input("Denominador"))
    r =a / b
except (ValueError, TypeError):     #pode declarar uma msg personalisada para erros especificos
    print("Tivemos um problema com os tipos de dados que voce digitou.")
except ZeroDivisionError:
    print("Nao é possivel dividir um numero por zero.")
except KeyboardInterrupt:
    print("o usuario nao informou os dados")
except Exception as erro: #pode colocar para aparecer qual foi a causa do erro
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f"O resultado é {r:.1}")   #caso nao de erro ele vai aparecer oque voce escolher
finally:
    print("Volte sempre! Muito obrigado!")  #mensagem para finalizar o programa independente do caminho que foi tomado!