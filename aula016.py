'''
Tuplas são variáveis compostas imutáveis.
Para fazer tuplas temos que utilizar parênteses
'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[0])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra Caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra Caramba!')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5)) # -> Conta quantas vezes o número 5 vai aparecer.
print(c.index(2)) # -> Vai mostrar qual a primeira posição em que o número aparece.
print(c.index(2, 4)) # -> Mostra a primeira ocorência de número 2 após a posição 4

# Podemos ter dados de tipos diferentes numa mesma tupla:
pessoa = ('João', 25, 'M', 60.50)
# Podemos deletar os valores de uma Tupla com o seguinte comando:
# del(pessoa)
# Não podemos exluir elementos específicos dentro da Tupla
print(pessoa)


