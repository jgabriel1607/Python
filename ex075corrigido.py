numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Os números digitados foram: {numeros}')
if 9 in numeros:
    print(f'O número 9 apareceu {numeros.count(9)} vez(es).')
else:
    print(f'O número 9 não foi digitado.')
if 3 in numeros:
    print(f'O número 3 apareceu a primeira vez na posição {numeros.index(3) + 1}')
else:
    print(f'O número 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
