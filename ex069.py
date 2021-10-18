print('Vamos coletar informações: ')
m = 0
f = 0
maior = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo, [M/F]: ')).strip().upper()[0]
    print('-' * 20)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-' * 20)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        f += 1
    if continuar == 'N':
        break
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'Tivemos {m} homens.')
print(f'E {f} mulheres menores de 20 anos. ')