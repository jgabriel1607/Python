print('Vamos ver a tabuada de vários números:')
tab = 1
res = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print('=' * 20)
    while tab <= 10:
        res = n * tab
        print(f'{tab} x {n} = {res}')
        tab += 1
    tab = 1
    print('=' * 20)
print('Ao digitar um número negativo você escolheu sair.')
