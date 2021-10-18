print('Vamos analisar alguns números: ')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
t = (n1, n2, n3, n4)
cont = conta9 = par = 0
conta3 = -1
print(f'Os valores digitados foram: {t}')
while True:
    if t[cont] == 9:
        conta9 += 1
    if cont == 0:
        if t[cont] == 3:
            conta3 = t.index(3)
    else:
        if t[cont] == 3:
            conta3 = t.index(3)
    cont += 1
    if cont >= 4:
        break
if conta9 == 0:
    print(f'O número 9 não foi digitado.')
else:
    print(f'O número 9 apareceu {conta9} vezes.')
if conta3 == -1:
    print(f'O número 3 não foi digitado.')
else:
    print(f'O número 3 apareceu pela primeira vez na posição {conta3}')
cont = 0
print(f'O(s) Número(s) Par(es) Digitado(s) Foi(Foram): ', end='')
while True:
    if t[cont] % 2 == 0:
        print(f'{t[cont]}', end=' ')
        par += 1
    if cont >= 3:
        break
    cont += 1
if par == 0:
    print('Não foi digitado número par.')

