from random import randint
from time import sleep
megasena = []
cont = 0
print('=' * 35)
print(f'{"JOGO NA MEGA SENA":^35}')
print('=' * 35)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
while True:
    megasena.append([])
    while True:
        numeros = randint(1, 60)
        if numeros not in megasena[cont]:
            megasena[cont].append(numeros)
        if len(megasena[cont]) >= 6:
            break
    cont += 1
    if cont >= jogos:
        break
print('=' * 35)
print(f'Sorteando {jogos} Jogos')
print('=' * 35)
cont = 0
for v in megasena:
    sleep(1)
    print(f'Jogo {cont + 1}: {v}')
    cont += 1
print('=' * 35)
print(f'{"BOA SORTE":^35}')
