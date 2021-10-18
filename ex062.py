print('Vamos realizar outra Progressão Aritimética: ')
i = int(input('Digite o primeiro valor da P.A.: '))
r = int(input('Digite o valor da razão: '))
f = int(input('Digite quantos termos deseja: '))
c = 1
while c <= f:
    print(i, end=' ')
    print(' → ' if c < f else 'PAUSA', end=' ')
    i += r
    c += 1
print('FIM')
