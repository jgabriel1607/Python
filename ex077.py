print('Vamos ver apenas as Vogais das palavras: ')
palavra = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')
qualPalavra = 0
qualLetra = 0
while True:
    print(f'\nA palavra {palavra[qualPalavra]} tem as vogais: ', end='')
    while True:
        if palavra[qualPalavra][qualLetra] in 'AaEeIiOoUu':
            print(f'{palavra[qualPalavra][qualLetra]}', end=' ')
        qualLetra += 1
        if qualLetra >= len(palavra[qualPalavra]):
            break
    qualLetra = 0
    qualPalavra += 1
    if qualPalavra >= len(palavra):
        break
