matriz = [[[], [], []], [[], [], []], [[], [], []]]
linha = coluna = somapar = somacol3 = maior = 0
for v in range(0, 9):
    numero = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    matriz[linha][coluna].append(numero)
    if numero % 2 == 0:
        somapar += numero
    if coluna == 2:
        somacol3 += numero
    if linha == 1:
        if coluna == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
    coluna += 1
    if coluna > 2:
        linha += 1
        coluna = 0
linha = coluna = 0
print('=' * 12)
for n in range(0, 3):
    for v in range(0, 3):
        print(matriz[linha][coluna], end=' ')
        coluna += 1
        if coluna > 2:
            coluna = 0
            linha += 1
    print()
print('=' * 12)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somacol3}')
print(f'O maior valor da segunda linha é {maior}.')
