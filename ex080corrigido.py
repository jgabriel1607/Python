numeros = []
numero = 0
for n in range(0, 5):
    numero = int(input('Digite um valor: '))
    if n == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Número adicionado na última posição.')
    else:
        cont = 0
        while cont < len(numeros):
            if numero <= numeros[cont]:
                numeros.insert(cont, numero)
                print(f'Número adicionado na posição {cont}')
                break
            cont += 1
print(numeros)
