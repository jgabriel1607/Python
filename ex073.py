print('Vamos ver alguns times do Campeonato Brasileiro 2021')
times = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Flamengo', 'Ceará SC',
         'Atlético-GO', 'Bahia', 'Corinthians', 'Fluminense', 'Santos', 'Juventude', 'Internacional',
         'Cuiabá', 'Sport Recife', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')
pos = 0
print('=' * 30)
print('Os cinco primeiros colocados são: ')
while True:
    print(times[pos])
    pos += 1
    if pos >= 5:
        break
pos = 16
print('=' * 30)
print('Os últimos quatro colocados são: ')
while True:
    print(times[pos])
    pos += 1
    if pos >= 20:
        break
print('=' * 30)
print('Organizando os times em ordem alfabética: ')
print(sorted(times))
print('=' * 30)
print(f'O time da Chapecoense está na posição: {times.index("Chapecoense") + 1}.')

f'''
Outra forma de resolver esse exercício de forma mais fácil.

print('=' * 30)
print(f'Lista de Times do Campeonato Brasileiro: {times}')
print('=' * 30)
print(f'Os 5 primeiros são {times[0:5]}')
print('=' * 30)
print(f'Os 4 útimos são {times[-4:]}')
print('=' * 30)
print(f'Em ordem alfabética ficam: {sorted(times)}')
print('=' * 30)
print(f'O time da Chapecoense está na posição: {times.index("Chapecoense") + 1}.')
'''
