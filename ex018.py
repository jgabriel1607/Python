import math

print('Descubra o seno, o cosseno e a tangente de um ângulo: ')
ang = float(input('Digite o ângulo desejado: '))
sn = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))

print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sn, cos, t))
