print('Vamos verificar se o carro ultrapassou a velocidade: ')
v = float(input('Digite a velocidade do carro: '))
lv = v - 80
if v <= 80.0:
    print('Seu Carro não ultrapassou o limite de velocidade de 80 km/h.')
else:
    print('Seu Carro ultrapassou o limite de velocidade  de 80 km/h e terá que pagar R$ {:.2f}'.format(lv * 7))
