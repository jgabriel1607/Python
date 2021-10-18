'''
Laços de repetição WHILE.
Usado para repetições onde não sabemos o limite de repetições.
'''

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('FIM')

n = 1
par = impar = 0 #variaveis com mesmo valor podem ser representadas dessa forma.
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímmpares.'.format(par, impar))

