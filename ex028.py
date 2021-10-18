import random
import time

print('Vamos ver se você descobre qual número estou pensando.')
ln = random.randint(0, 5)
nd = int(input('Digite um número de 1 à 5 que você acha que estou pensando: '))
print('Deixa eu pensar...')
time.sleep(2)
if nd == ln:
    print('Você Acertou! O número que estava pensando era {}'.format(ln))
else:
    print('Você Errou! O número que estava pensando era {}'.format(ln))



