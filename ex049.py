print('Vamos realizar a tabuada de um número: ')
n = int(input('Digite o número desejado: '))
for c in range(1, 11):
    r = c * n
    print('{:2} x {:2} = {}'.format(c, n, r))
