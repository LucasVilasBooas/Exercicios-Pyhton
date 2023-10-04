cid = str(input('Em qual cidade voce nasceu? ')) .strip() # faz com que tire os espaços na hora das bucas
print(cid[:5].upper() == 'SANTO') # o upper faz com oque o usuario pode colocar maiusculo

#buscar se tem uma palavra na frase ou nome inteiro.

nome = str(input("qual seu nome completo? \n"))
print(f'seu nome tem silva? {"silva" in nome.lower()}')# ele vai buscar em toda a frase/nome digitado se tem a palavra buscada
