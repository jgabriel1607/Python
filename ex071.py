print('Bem vindo ao caixa eletrônico.')
n = int(input('Quanto deseja sacar? '))
total = n
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced} Reais.')
            if ced == 50:
                ced = 20
            if ced == 20:
                ced = 10
            if ced == 10:
                ced = 1
            totced = 0
    if total == 0:
        break
