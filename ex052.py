print('Vamos verificar se um número é primo: ')
n = int(input('Digite um número: '))
if n % 1 == 0 and n % n == 0:
    print('O número {} é um número primo.'.format(n))
else:
    print('O número {} não é um número primo.'.format(n))
