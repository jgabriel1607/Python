print('Vamos ver se um número digitado é par ou ímpar: ')
n = int(input('Digite um número: '))
p = n % 2
if p == 0:
    print('O número {} é Par'.format(n))
else:
    print('O número {} é Ímpar'.format(n))

