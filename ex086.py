matriz = [[[], [], []], [[], [], []], [[], [], []]]
linha = coluna = 0
for v in range(0, 9):
    matriz[linha][coluna].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
    coluna += 1
    if coluna > 2:
        linha += 1
        coluna = 0
linha = coluna = 0
print('=' * 12)
for n in range(0, 3):
    for v in range(0, 3):
        print(f'{matriz[linha][coluna]}', end=' ')
        coluna += 1
        if coluna > 2:
            coluna = 0
            linha += 1
    print()
print('=' * 12)
