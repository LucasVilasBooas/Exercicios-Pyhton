from time import  sleep
def contador(i, f, p):
    print(f'Contatem de {i} ate {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=" ")
            c += p
            sleep(0.3)
        print("FIM")
    else:
        c = i
        while c >= f:
            print(f'{c}', end=" ")
            c -= p
            sleep(0.3)
        print("FIM")

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
ini = int(input('Digite o numero de inicio →'))
fim = int(input('Digite o ultimo numero →'))
pas= int(input('Digite o passo →'))
print()
contador(ini, fim, pas)