numeros = []
numero = cont = 0
while True:
    opcao = ' '
    numero = int(input('Digite um número: ')) #Poderia usar numeros.append(int(input('Digite número: ')))
    numeros.append(numero)
    cont += 1
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {cont} números.') #Poderia usar apenas len(numeros)
print(f'Os números digitados em ordem decrescente ficam: {numeros}')
if 5 in numeros:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')