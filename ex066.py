print('Vamos somar alguns números: ')
soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números.')
print(f'A soma de todos os valores digitados é {soma}.')

