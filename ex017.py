import math
print('Descubra a hipotenusa: ')
cat1 = float(input('Digite o valor do primeiro cateto: '))
cat2 = float(input('Digite o valor do segundo cateto: '))
h = math.hypot(cat1, cat2)
print('O triângulo que possui os catetos {:.2f}, {:.2f} tem uma hipotenusa de: {:.2f}'.format(cat1, cat2, h))


