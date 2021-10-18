print('Vamos às compras!')
total = produto = menor = cont = 0
prodbarato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o valor do produto: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        produto += 1
    if cont == 1 or preco < menor:
        menor = preco
        prodbarato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a registrar produtos? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da sua compra foi de R$ {total:.2f}')
print(f'Nessa compra tivemos {produto} produtos acima de R$ 1000.00 ')
print(f'O Produto mais barato foi {prodbarato}.')

