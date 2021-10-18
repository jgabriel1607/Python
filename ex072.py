print('Vamos ver números por extenso.')
print('Digite um número entre 0 e 20')
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
opcao = 's'
while True:
    while True:
        n = int(input('Digite um número: '))
        if n >= 0 and n <= 20:
            break
    print('Escrito por extenso fica: ')
    print(numeros[n])
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().lower()
        if opcao in 'SsNn':
            break
    if opcao in 'n':
        break