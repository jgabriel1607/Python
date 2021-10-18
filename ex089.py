boletim = [[[], []]]
pessoa = media = 0
while True:
    nome = str(input('Nome: '))
    boletim[pessoa][0].append(nome)
    nota1 = float(input('Nota 1: '))
    boletim[pessoa][1].append(nota1)
    nota2 = float(input('Nota 2: '))
    boletim[pessoa][1].append(nota2)
    media = (nota1 + nota2) / 2
    boletim[pessoa][1].append(media)
    pessoa += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
    boletim.append([[], []])
pessoa = 0
print('=' * 25)
print(f'{"No.":<} NOME {"MÉDIA":>15}')
print('-' * 25)
for v in boletim:
    print(f'{pessoa:<}   {boletim[pessoa][0][0]:15}  {boletim[pessoa][1][2]:<.1f}')
    pessoa += 1
print('-' * 25)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    print(f'As notas de {boletim[aluno][0][0]} são {boletim[aluno][1][0:2]}')
