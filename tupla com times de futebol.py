times = ('Botafogo', 'Palmeiras', 'Gremio', 'Flamengo', 'Fluminense', 'Bragantino', 'Atletico-PR',
         'Fortaleza', 'Atletico-MG', 'Cuiaba', 'Sao Paulo', 'Cruzeiro', 'Corintians', 'Internacional',
         'Goias', 'Bahia', 'Santos', 'Vasco da Gama', 'Coritiba', 'America-MG')
print(times)
print('*-'*30)
print(f'Os 5 primeiros times sao {times[0:5]}')
print('*-'*30)
print(f'Os 4 ultimos times sao {times[-4:]}') # mostra do -4 ate o ultimo
print('*-'*30)
print(f'Os  times em ordem alfabetica sao { sorted(times)}')
print('*-'*30)
print(f'O time da Chapecoence esta na {times.index("Santos")+1}ª posição')