time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador →'))
    tot = int(input(f"quantas partidas o {jogador['nome']} jogou? →"))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f' quantos gols na partida{c+1} ')))
    jogador['gols'] = partidas[:] # feito uma copia dos gols para o dicionario do jogador
    jogador['total'] = sum(partidas) # soma dos gols (valores de partidas) para um novo espaço(total de gols) em jogador
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ?[S/N] →')).upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-'*40)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-'*40)
for k, v in enumerate (time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) →'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Nao existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}--')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('>>> VOLTE SEMPRE <<<')