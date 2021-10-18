print('Vamos verificar o nome de diversas maneiras: ')
nome = str(input('Digite seu nome completo: ')).strip()
# letras sem espaço(variável) = quantidade de caracteres - contagem de espaçoes em 'nome':
letrasnome = len(nome) - nome.count(' ')
# primeiro nome(variável) = divida nome.
prinome = nome.split()
print('Veja seu nome com letras maiúsculas: {}'.format(nome.upper()))
print('Veja seu nome com letras minúsculas: {}'.format(nome.lower()))
print('Seu nome possui {} letras.'.format(letrasnome)) # Poderia ter feito diretamente --> print('Seu nome...{} letras'.format(len(nome) - nome.count(' ')))
# Ao final mostre o primeiro nome da string dividida.
print('O seu primeiro nome é: {} e possui {} letras.'.format(prinome[0], len(prinome[0]))) # Ou podemos colocar print('Seu... {} letras.'.format(nome.find(' ')))


