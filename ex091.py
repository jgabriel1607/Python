from random import randint
from operator import itemgetter
jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
partida = []
print(f'{"-- VALORES SORTEADOS --":^30}')
print('-' * 30)
for j, d in jogadas.items():
    print(f'{j} tirou {d}')
print('=' * 30)
print(f'{"-- RANKING --":^30}')
print('-' * 30)
partida = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for x in range(0, 4):
    print(f'{x + 1}º Lugar - {partida[x][0]} tirou {partida[x][1]}')











