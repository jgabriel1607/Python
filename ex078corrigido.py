numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print(f'Você digitou os números: {numeros}')
print(f'O maior número digitado foi {maior}', 'nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {menor}', 'nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
