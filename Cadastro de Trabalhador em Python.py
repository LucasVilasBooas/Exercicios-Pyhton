from datetime import datetime
trabalhador = {}
trabalhador['nome']         = str(input('Nome →'))
trabalhador['nasc']         = int(input('ano de Nascimento →')) # como nao vai usar ele usa uma variavel simples
trabalhador['ctps']         = int(input('Carteira de Trabalho (0 nao tem) →'))
trabalhador['idade']        = 2023-trabalhador['nasc']
if trabalhador['ctps']!=0:
    trabalhador['salario']      = float(input('Salario →'))
    trabalhador['anoinicio']    = int(input('Ano do inicio do trabalho →'))
    trabalhador['aposentadoria']= (35-(2023-trabalhador['anoinicio']))+trabalhador['idade']
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
print()


#FORMA DO GUANABARA
dados=dict()
dados['nome']= str(input('Nome →'))
nasc = int(input('Ano de nascimento →'))
dados['idade']= datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho →'))
if dados['ctps'] != 0:
    dados['contratação']= int(input('Ano de contratação'))
    dados['salario']=float(input('Sario R$ →'))
    dados['aposentadoria']= dados['idade'] + ((dados['contratação'] + 35 ) - datetime.now().year )
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')