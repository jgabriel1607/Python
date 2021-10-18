from random import randint
numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores digitados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')
