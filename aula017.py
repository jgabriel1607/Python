'''
Listas
Listas são semelhantes as tuplas, porém, elas são Mutáveis.

Além disso as Listas são representadas por '[]'
Ex:
Lanches = ['Hambunguer', 'Suco', 'Pizza', 'Pudim']

Podemos modificar um item da lista.
Ex:
Lanches[4] = 'Sorvete' --> Lanches = ['Hambunguer', 'Suco', 'Pizza', 'Sorvete']

Podemos também acrescentar itens ao final da lista.
Ex:
Lanches.append('Cookie') --> Lanches = ['Hambunguer', 'Suco', 'Pizza', 'Sorvete', 'Cookie']

Ou podemos inserir itens em outras posições da lista.
Ex:
Lanches.insert(0, 'Cachorro Quente') --> Lanches = ['Cachorro Quente', 'Hambunguer', 'Suco', 'Pizza', 'Sorvete', 'Cookie']

Podemos exluir itens de uma lista.
Ex:
del Lanchse[3] ou Lanches.pop(3) ou Lanches.remove('Pizza') -->
Lanches = ['Cachorro Quente', 'Hambunguer', 'Suco', 'Sorvete', 'Cookie']
Obs: As 2 Primeiras opções utilizamos o índice para remover, enquanto a última, buscamos o valor dentro da lista.
Se utilizarmos apenas Lanches.pop(), irá apagar o último item da lista.
Se tentarmos remover item que não está na lista será apresentado erro.
Para evitar isso podemos utilizar o 'if' -->
(Se 'Valor' está em Nome da Lista:)
if 'Pizza' in Lanches:
    Lanches.remove('Pizza')
Se a Lista possui 2 valores idênticos e fizermos a remoção do valor, ele exluirá apenas a 1ª ocorrência.

Podemos criar uma Lista a partir de um 'range'.
Ex:
valores = list(range(4, 11))
Criará uma lista com valores de 4 à 10 de forma crescente. -->
valores = [4, 5, 6, 7, 8, 9, 10]

Se criarmos uma Lista com valores de forma desordenada, podemos ordená-la da seguinte maneira.
Ex:
valores = [8, 2, 5, 4, 9, 3, 0] -->
valores.sort() -->
valores = [0, 2, 3, 4, 5, 8, 9]
Podemos também colocar na ordem inversa
valores.sort(reverse = True)

Podemos saber quantos itens tem na lista.
Ex:
len(valores) --> 7
'''

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2, 0)
print(num)
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não possui o número 4 na lista.')
print(num)
print(f'Essa lista possui {len(num)} elementos.')
print()

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...', end='')
print()

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Final da Lista')
print()

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()


numeros = list()
for cont in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))
for c, v in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Final da Lista')





