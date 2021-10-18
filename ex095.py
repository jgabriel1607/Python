jogador = {}
time = []
while True:
    total = 0
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Partidas'] = partidas
    jogador['Gols'] = []
    for p in range(0, partidas):
        jogador['Gols'].append(int(input(f'Quantos gols na partida {p + 1}? ')))
        total += jogador['Gols'][p]
        jogador['Total'] = total
    time.append(jogador.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print('=' * 50)
print(f'{"Cod"} / {"Nome"} / {"Gols"} / {"Total"}')
print('-' * 50)
for x in range(0, len(time)):
    print(f'{x} / {(time[x]["Nome"])} / {time[x]["Gols"]} / {(time[x]["Total"])}')
print('-' * 50)
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 Interrompe] '))
    if dados == 999:
        break
    if dados <= len(time) - 1:
        print('-' * 50)
        print(f'-- LEVANTAMENTO DO JOGADOR {time[dados]["Nome"]} --')
        for j in range(0, time[dados]['Partidas']):
            print(f'Na partida {j + 1} fez {time[dados]["Gols"][j]}')
        print('-' * 50)
