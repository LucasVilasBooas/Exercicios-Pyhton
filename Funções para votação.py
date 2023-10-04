from datetime import date

        # O DATE TTIME NAO ESTA FUNCIONANDO NESTE PROGRAMA
def voto(ano):
    atual = 2023
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos nao se pode votar'
    elif 16<= idade < 18 or idade > 65:
        return f'com {idade} anos o voto é opcional'
    else:
        return f'com {idade} anos o voto é obrigatorio'

nasc = int(input("Em que ano voce nasceu ?"))
print(voto(nasc))