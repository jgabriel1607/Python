print('Vamos realizar contagem de números: ')
print('Digite um número de 0 à 998. Ao digitar 999 o programa encerrará.')
n = 0
cont = 0
soma = 0
while n != 999:
    if n >= 0 and n <= 998:
        n = int(input('Digite um número inteiro: '))
    else:
        print('Digite um número válido:')
        n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
print('Você escolheu sair.')
cont -= 1
soma -= 999
print('Você digitou {} números diferentes.'.format(cont))
print('A soma de todos os números digitados é {}.'.format(soma))
