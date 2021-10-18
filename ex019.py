import random
print('Qual aluno será sorteado: ')
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
l = [al1, al2, al3, al4]
print('O aluno escolhido foi {}'.format(random.choice(l)))
