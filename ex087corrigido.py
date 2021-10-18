matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = col3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            col3 += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
print('=' * 22)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 22)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {maior}')

