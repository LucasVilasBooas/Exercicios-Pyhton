cad = {}
cad['nome'] = str(input("Digite o nome"))
cad['media']= float(input('Digite a media'))
if cad['media']>=7:
    cad['situação']='Aprovado'
elif 5<= cad['media'] < 7:
    cad['situação']= 'Recuperação'
else:
    cad['situação']= 'Reprovado'

for k, v in cad.items():
    print(f'- {k} é igual a {v}')