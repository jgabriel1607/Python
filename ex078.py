numeros = []
maior = menor = 0
posmaior = []
posmenor = []
for c, n in enumerate(range(0, 5)):
    numeros.append(int(input(f'Digite um número para posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
        posmaior.append(c)
        posmenor.append(c)
    else:
        if numeros[c] == maior:
            posmaior.append(c)
        if numeros[c] == menor:
            posmenor.append(c)
        else:
            if numeros[c] > maior:
                maior = numeros[c]
                posmaior = []
                posmaior.append(c)
            if numeros[c] < menor:
                menor = numeros[c]
                posmenor = []
                posmenor.append(c)
print(numeros)
print(f'O maior número foi {maior} na(s) posição(ões) ', end='')
for m in posmaior:
    print(f'{m}... ', end='')
print(f'\nO menor número foi {menor} na(s) posição(ões) ', end='')
for m in posmenor:
    print(f'{m}... ', end='')
