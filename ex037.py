print('Vamos converter números decimais: ')
numero = int(input('Digite um número inteiro: '))
print('Agora escolha o método de conversão: ')
print('Digite 1 para Binário. \nDigite 2 para Octal. \nDigite 3 para Hexadecimal.')
conversao = int(input('Qual você escolhe? '))

if conversao == 1:
    print('Você escolheu Binário. ')
    print('O resultado da conversão de {} para binário é {}.'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('Você escolheu Octal.')
    print('O resultado da conversão de {} para octal é {}.'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('Você escolheu Hexadecimal.')
    print('O resultado da conversão de {} para hexadecimal é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Esolha outra opção.')
