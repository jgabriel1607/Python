boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print('=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
cont = 0
for v in boletim:
    print(f'{cont:<4}{boletim[cont][0]:<10}{boletim[0][2]:>8.1f}')
    cont += 1
print('=' * 30)
while True:
    a = int(input('De qual aluno deseja mostrar as notas? (999 interrompe): '))
    if a == 999:
        break
    if a <= len(boletim) - 1:
        print('-' * 30)
        print(f'As notas de {boletim[a][0]} são {boletim[a][1]}')
        print('=' * 30)
print('Você encerrou o programa.')
