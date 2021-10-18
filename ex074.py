from random import randint
a = randint(0, 9)
b = randint(0, 9)
c = randint(0, 9)
d = randint(0, 9)
e = randint(0, 9)
t = (a, b, c, d, e)
cont = menor = maior = 0
print('Os números sorteados foram: ', end='')
while True:
    print(t[cont], end=' ')
    if cont == 0:
        maior = t[cont]
        menor = t[cont]
    else:
        if t[cont] > maior:
            maior = t[cont]
        if t[cont] < menor:
            menor = t[cont]
    cont += 1
    if cont >= 5:
        break
print('')
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')

