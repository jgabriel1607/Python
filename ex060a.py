n = int(input('Digite um número: '))
cont = 1
f = 1
print('{}! = '.format(n), end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)
