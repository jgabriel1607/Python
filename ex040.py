print('Vamos descobrir se você foi aprovado: ')
nota1 = float(input('Digite a nota de prova: '))
nota2 = float(input('Digite a nota de trabalho: '))
media = (nota1 + nota2) / 2

print('Sua média foi {}.'.format(media))
if media <= 5.0:
    print('Sinto muito. Você foi reprovado.')
elif 5.0 < media <= 6.9:
    print('Infelizmente você ficará de recuperação.')
else:
    print('Parabéns! Você foi aprovado.')
