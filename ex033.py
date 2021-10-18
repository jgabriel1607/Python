print('Vamos descobrir qual é o maior número: ')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Dos números digitados o menor é {}'.format(menor))
print('Dos números digitados o maior é {}'.format(maior))

'''if n1 > n2:
    if n1 > n3:
        print('Dos números digitados o número {} é o maior.'.format(n1))
    else:
        print('Dos números digitados o número {} é o maior.'.format(n3))
else:
    if n2 > n3:
        print('Dos números digitados o número {} é o maior.'.format(n2))
    else:
        print('Dos números digitados o número {} é o maior.'.format(n3))

if n1 < n2:
    if n1 < n3:
        print('Dos números digitados o número {} é o menor.'.format(n1))
    else:
        print('Dos números digitados o número {} é o menor.'.format(n3))
else:
    if n2 < n3:
        print('Dos números digitados o número {} é o menor.'.format(n2))
    else:
        print('Dos números digitados o número {} é o menor.'.format(n3))'''
