jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome Jogador '))
tot = int(input(f"quantas partidas o {jogador['nome']} jogou "))
for c in range (0, tot):
    partidas.append(int(input(f' quantos gols na partida{c} ')))
jogador['gols'] = partidas[:] # feito uma copia dos gols para o dicionario do jogador
jogador['total'] = sum(partidas) # soma dos gols (valores de partidas) para um novo espaço(total de gols) em jogador
print('=-'*30)
print(jogador)
print('=-'*30)
for l, v in jogador.items():
    print(f'o campo {l} tem o valor {v}')
print('=-'*30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate (jogador['gols']):
    print(f'=>Na partida {i+1}, fez {v} gols.')
print(f' Foi um total de {jogador["total"]} gols.')