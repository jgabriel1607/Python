print('Bem vindo ao Caixa Eletrônico.')
d = 0
n50 = n20 = n10 = n1 = 0
n = int(input('Digite o valor a ser sacado: '))
if n % 50 == 0:
    d = n // 50
    n = n % 50
    n50 = d
else:
    d = n // 50
    n = n % 50
    n50 = d
    if n % 20 != 20:
        d = n // 20
        n = n % 20
        n20 = d
    if n % 10 != 10:
        d = n // 10
        n = n % 10
        n10 = d
    if n % 1 == 0:
        d = n // 1
        n1 = d
print(f'Notas de 50: {n50}')
print(f'Notas de 20: {n20}')
print(f'Notas de 10: {n10}')
print(f'Notas de 1: {n1}')


