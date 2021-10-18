print('Vamos analisar as informações: ')
sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    print('Digite uma opção válida.')
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
print('Você digitou uma opção válida. Obrigado!')
