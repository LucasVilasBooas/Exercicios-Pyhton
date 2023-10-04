dados = {}
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'  #dicionario nao aceita o .append
print(dados)
del dados['idade']
print(dados)

filme = {'titulo':'Star Wars',
         'ano': 1997,
         'diretor':'George Lucas'
}
print()
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

print()                   # NO LUGAR DO ENUMARATE é usado o .ITEMS
for k,v in filme.items(): # é usado o .items porque esta pegando 2 valores
    print(f'O {k} é {v}') # k e v sendo atribuidos a chaves e valores

print()
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'Sao Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print()
estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf']= str(input('Unidade Federativa'))
    estado['sigla']= str(input('Sigla do Estado'))
    brasil.append(estado.copy()) # utiliza para fazer a copia correta do dicionario
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')