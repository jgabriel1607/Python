jogador = {}
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = []
for p in range(0, partidas):
    jogador['Gols'].append(int(input(f'Quantos gols na partida {p + 1}? ')))
jogador['Total'] = sum(jogador['Gols'])
print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'Na partida {c + 1}, fez {jogador["Gols"][c]} gol(s).')
print(f'Foi um total de {sum(jogador["Gols"])} gol(s).')























