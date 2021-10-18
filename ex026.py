print('Vamos analisar uma frase e contar quantas letras "A" ela possui: ')
frase = str(input('Digite uma frase: ')).strip().lower()
print('A frase digitada possui {} letras a'.format(frase.count('a')))
print('A frase digitada tem seu primeiro a na posição {}.'.format(frase.find('a') + 1))
print('A frase digitada tem seu último a na posição {}.'.format(frase.rfind('a') + 1))

