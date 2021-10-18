print('Vamos verificar se a frase é um palindromo, ou seja, pode ser lida de trás pra frente sem perder sentido.')
frase = str(input('Digite uma frase: ')).strip().upper()
cf = len(frase) - frase.count(' ')
i = 0
for c in range(i, cf):

