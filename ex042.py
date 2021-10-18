print('Vamos verificar qual o tipo do triângulo: ')
x = float(input('Digite o valor da primeira reta: '))
y = float(input('Digite o valor da segunda reta: '))
z = float(input('Digite o valor da terceira reta: '))

if x + y > z and x + z > y and y + z > x:
    print('As retas podem formar um triângulo. ')
    if x == y == z:
        print('O triângulo formado é um Triângulo Equilátero.')
    elif x != y != z != x:
        print('O triângulo formado é um Triângulo Escaleno.')
    else:
        print('O triângulo formado é um Triângulo Isósceles.')
else:
    print('As retas não podem formar um triângulo.')
