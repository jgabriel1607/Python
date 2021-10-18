numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Número adicionado com sucesso.')
    else:
        print('Número duplicado. Não adicionado.')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
numeros.sort()
print(numeros)
