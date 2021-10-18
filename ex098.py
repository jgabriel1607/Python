from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}.')
        for x in range(i, f+1, p):
            print(f'{x}', end=' ')
            sleep(0.3)
        print('Fim!')
        sleep(0.4)
        print('=' * 40)
    if i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}.')
        for x in range(i, f-1, -p):
            print(f'{x}', end=' ')
            sleep(0.3)
        print('Fim!')
        sleep(0.4)
        print('=' * 40)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem.')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
