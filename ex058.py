from random import randint
print('Vamos ver se você descobre em qual número estou pensando: ')
print('Digite um número de 0 à 10.')
pc = randint(0, 10)
contador = 0
acertou = False
while not acertou:
    jogador = int(input('Digite um número: '))
    contador += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
            print('Menos... Tente novamente.')
        if jogador < pc:
            print('Mais...Tente novamente')
print('Parabéns! Você acertou na {}ª tentativa.'.format(contador))
