algo = input('Digite algo: ')
print('O tipo primitivo é: {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É texto? {}'.format(algo.isalpha()))
print('É número? {}'.format(algo.isnumeric()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em totalmente em maiúsculo? {}'.format(algo.isupper()))
print('EStá em totalmente em minúsculo? {}'.format(algo.islower()))
# Capitalizado é apenas quando a primeira letra está em maiúsculo.
print('Está capitalizado? {}'.format(algo.istitle()))
# algo é um objeto e is*() É um atributo 
