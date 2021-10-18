def maior(*num):
    global ma
    ma = 0
    for n in range(0, len(num)):
        if n == 0:
            ma = num[n]
        else:
            if num[n] > ma:
                ma = num[n]
    print('=' * 50)
    print('Analisando os valores passados...')
    for n in range(0, len(num)):
        print(f'{num[n]}', end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {ma}.')
    print('=' * 50)
    ma = 0


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
