print('Vamos descobrir se retas podem formar um triângulo: ')
x = float(input('Digite o valor da primeira reta: '))
y = float(input('Digite o valor da segunda reta: '))
z = float(input('Digite o valor da terceira reta: '))

if x + y > z and x + z > y and y + z > x:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
