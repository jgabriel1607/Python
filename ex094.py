pessoa = {}
galera = []
totidade = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()
    pessoa['Sexo'] = sexo
    idade = int(input('Idade: '))
    pessoa['Idade'] = idade
    opcao = ' '
    galera.append(pessoa.copy())
    totidade += idade
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
media = totidade / len(galera)
print('=' * 30)
print(f'O total de pessoas cadastradas foi {len(galera)}.')
print(f'A média de idade do grupo foi de {media:.2f}.')
print('A lista com mulheres é: ', end='')
for x in range(0, len(galera)):
    if galera[x]['Sexo'] == 'F':
        print(f'{galera[x]["Nome"]} /', end=' ')
print()
print(f'As pessoas com idade acima da média são: ', end='')
for x in range(0, len(galera)):
    if galera[x]['Idade'] >= media:
        print(f'{galera[x]["Nome"]} /', end=' ')

















