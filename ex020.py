import random

print('Descubra a ordem de apresentação: ')
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
l = [a1, a2, a3, a4]
random.shuffle(l)
print('Os alunos se apresentarão na seguinte ordem: \n{}'.format(l))
