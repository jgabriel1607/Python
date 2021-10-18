print('Vamos realizar uma comparação entre números: ')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior. Os números são iguais')
