pessoa = []
galera = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = pessoa[1]
    if len(galera) > 0:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    galera.append(pessoa[:])
    pessoa.clear()
    if opcao == 'N':
        break
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
