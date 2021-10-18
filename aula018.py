'''
Listas dentro de listas.
Temos o exemplo:
    dados = list()
    dados.append('Pedro')
    dados.append(25)
    print(dados) --> [Pedro, 25]
Se quisermos adicionar esses valores a outra lista, fica da seguinte maneira:
    pessoas = list()
    pessoas.append(dados[:]) --> Adicionará todos os dados da lista anterior.
Porém os dados da lista anterior entrarão como um único item.
Ex:
print(pessoas[0]) --> [Pedro, 25]
Ex:
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) --> Pedro
print(pessoas[1][1]) --> 19
print(pessoas[2][0]) --> João
print(pessoas[1]) --> [Maria, 19]
'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

Esse método cria apenas uma ligação da primeira lista.
Ou seja se mudarmos um valor na primeira lista, automaticamente muda na segunda lista.
'''

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

pessoas = [['João', 19], ['Ana', 22], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[2][1])

for p in pessoas:
    print(p)
for p in pessoas:
    print(p[0])
for p in pessoas:
    print(p[1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')

cambada = list()
dados = list()
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    cambada.append(dados[:])
    dados.clear()
print(cambada)
print(dados)

for p in cambada:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')










