print('Vamos comparar temperaturas Celsius, Fahrenheit e Kelvin')
cl = float(input('Digite uma temperatura em Celsius: '))
fh = (cl * 9 / 5) + 32
kl = cl + 273.15
print('A temperatura de {:.2f}ºC equivale a: \n{:.2f}ºF \n{:.2f}ºK'.format(cl, fh, kl))
