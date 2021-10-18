print('Vamos realizar o fatorial: ')
n = int(input('Digite um número inteiro: '))
c = n
f = 1
print('{}! = '.format(n), end=' ')
while c > 0:
    print(c, end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f)
print('FIM!')

