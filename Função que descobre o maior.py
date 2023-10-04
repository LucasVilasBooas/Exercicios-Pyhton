def maiorvalor(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores ')
    for valor in num:
        print(f'{valor}', end=" ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informador {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maiorvalor(2,3,4,5,6,7,8)
print()
maiorvalor(4,5,7,9)
print()
maiorvalor(44,5,88,3,111)