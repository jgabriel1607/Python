from datetime import date
print('Vamos verificar se um ano é bissexto: ')
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
# A regra para identificar se ano é bissexto é:
# Tem que ser divisível por 4. Não divisível por 100 e disível por 400.
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
