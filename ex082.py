numeros = []
numero = 0
pares = []
impares = []
cont = 0
while True:
    opcao = ' '
    numero = int(input('Digite um número: ')) #Poderia usar numeros.append(int(input('Digite valor: ')))
    numeros.append(numero)
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
while True:
    if numeros[cont] % 2 == 0:
        pares.append(numeros[cont])
    if numeros[cont] % 2 == 1:
        impares.append(numeros[cont])
    cont += 1
    if cont >= len(numeros):
        break
print(f'Os números digitados foram: {numeros}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
