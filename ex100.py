from random import randint
numero = 0
numeros = []
soma = 0


def sorteia():
    global numero
    global numeros
    for n in range(0, 5):
        numero = randint(0, 10)
        numeros.append(numero)
    print(f'Sorteando 5 valores da lista: ')
    for n in range(0, 5):
        print(f'{numeros[n]}', end=' ')
    print()


def somapar():
    global soma
    for n in range(0, 5):
        if numeros[n] % 2 == 0:
            soma += numeros[n]
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somapar()
