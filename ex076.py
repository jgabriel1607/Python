print('Vamos ver a lista de valores: ')
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila',
         120.32, 'Canetas', 22.3, 'Livro', 34.90)
item = 0
preco = 1
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
while True:
    print(f'{lista[item]:.<30}', end=' ')
    print(f'R${lista[preco]:>7.2f}')
    item += 2
    preco += 2
    if item > 16:
        break
print('=' * 40)
