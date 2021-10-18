'''
Dicionários.
Podemos criar listas de itens e seus índices podem ser letras ou palavras, ao invés só de números.
Podemos utilizar da seguinte forma:
dados = dict() ou dados = {}
Ex:
dados = {'nome':'Pedro', 'idade':'25'} --> onde 'nome' é o índice do valor 'Pedro'.
print(dados['nome']) --> Pedro
print(dados['idade']) --> 25
Para adicionar itens ao dicionário usamos:
dados['sexo'] = 'M' --> dados = {'nome':'Pedro', 'idade':'25', 'sexo':'M'}
Para deletar um item do dicionário usamos:
deldados['idade'] --> dados = {'nome':'Pedro', 'sexo':'M'}
Também podemos criar um dicionário da seguinte forma:
filme{'titulo':'Star Wars'
      'ano':'1977'
      'diretor':'George Lucas'
}
Com dicionários temos algumas categorias para nos atentarmos:
valores, chaves e itens ou values, keys e items
valores no exemplo acima são: Star Wars, 1977, George Lucas
chaves no exemplo acima são: titulo, ano, diretor
e items são tanto os valores quanto as chaves
Ex:
print(filme.values())
print(filme.keys())
print(filme.items())

Podemos utilizar essas informações também dentro do for.
Ex:
for k, v in filme.items(): --> onde k será keys e v será values
    print(f'O {k} é {v}.') --> O título é Star Wars
                           --> O ano é 1977
                           --> O diretor é George Lucas
Podemos utilizar tuplas, listas e dicionários juntos.
Nesse exemplo podemos ter uma lista de filmes.
Ex:
locadora = [{'titulo':'Star Wars', 'ano':'1977', 'diretor':'George Lucas'},
            {'titulo':'Avengers', 'ano':'2012', 'diretor':'Joss Whedon'},
            {'titulo':'Matrix', 'ano':'1999', 'diretor':'Wachowski'}
           ]
print(locadora[0]['ano']) --> 1977
print(locadora[2]['titulo']) --> Matrix
Anteriormente em tuplas e listas precisávamos utilizar enumerate. Mas com dicionários precisamos utilizar pessoas.items()

'''

pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 25}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for i in pessoas.items():
    print(i)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
print(pessoas)
pessoas['nome'] = 'Carlos'
print(pessoas)
pessoas['peso'] = 98.8
print(pessoas)

'''brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = {}
brasil = []
for x in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
