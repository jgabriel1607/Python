numeros = []
numero = 0
maior = menor = 0
for n in range(0, 5):
    numero = int(input('Digite um número: '))
    if n == 0:
        numeros.append(numero)
        maior = menor = numero
        print('Número adicionado na última posição.')
    if numero < menor:
        menor = numero
        numeros.insert(0, numero)
        print('Número adicionado na posição 0')
    if numero > maior:
        maior = numero
        numeros.append(numero)
        print('Número adicionado na última posição.')
    if n == 2:
        if numeros[1] > numero > numeros[0]:
            numeros.insert(1, numero)
            print('Número adicionado na posição 1')
    if n == 3:
        if numeros[1] > numero > numeros[0]:
            numeros.insert(1, numero)
            print('Número adicionado na posição 1')
        if numeros[2] > numero > numeros[1]:
            numeros.insert(2, numero)
            print('Número adicionado na posição 2')
    if n == 4:
        if numeros[1] > numero > numeros[0]:
            numeros.insert(1, numero)
            print('Número adicionado na posição 1')
        if numeros[2] > numero > numeros[1]:
            numeros.insert(2, numero)
            print('Número adicionado na posição 2')
        if numeros[3] > numero > numeros[2]:
            numeros.insert(3, numero)
            print('Número adicionado na posição 3')
print(numeros)