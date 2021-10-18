n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
#print('A soma é igual a {}'.format(soma))
print(f'A soma é igual a {soma}') #É a mesma coisa que a linha de cima.
'''
Nesse caso ao digitar o  número 999 ele não será contabilizado na soma.
'''
nome = 'João'
idade = 25
salario = 1470.3
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}.')
