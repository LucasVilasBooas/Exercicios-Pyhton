''' melhor usar importar tudo como na linha 2  '''
import uteisaulamodulosepacotes #esta no outro programa feito para as funções
from uteisaulamodulosepacotes import dobro, fatorial, triplo  # chamando o programa assim eu nao preciso usar o .uteisaula antes da função
num = int(input("digite um valor "))
fat = uteisaulamodulosepacotes.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteisaulamodulosepacotes.dobro(num)}')
print(f'O triplo de {num} é {uteisaulamodulosepacotes.triplo(num)}')
print()

# chamando o programa assim eu nao preciso usar o .uteisaula antes da função
from uteisaulamodulosepacotes import dobro, fatorial, triplo
num = int(input("digite um valor "))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')