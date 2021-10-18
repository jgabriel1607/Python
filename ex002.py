print('Cálculo de 2 números inteiros')
n1 = int(input('Digite um valor: '))
# print(type(n1)) Console apresentará o tipo da variável
n2 = int(input('Digite outro valor: '))
# Posso atribuir o resultado a uma variável
r = n1 + n2
# O resultado ficaria:
# print('A soma dos valores é igual a: {}.'.format(r))
# print('A soma dos valores é igual a: {}.'.format(n1 + n2))
# print('A soma entre', n1, 'e', n2, 'é igual a:', n1+n2)
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, r))

print('Cálculo de 2 números reais')
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
print('A soma dos valores é igual a: {}.'.format(n1 + n2))
