def fatorial(num=1, show=False):
    """
    Realiza o fatorial de um número digitado pelo usuário.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostra ou não o processo da conta.
    :return: O valor do Fatorial de um número n.
    """
    n = 1
    for f in range(num, 0, -1):
        if show:
            print(f'{f}', 'x ' if f > 1 else '', end='')
            n *= f
            if f <= 1:
                print(f'=', end=' ')
        else:
            n *= f
    return n


numero = int(input('Digite um número: '))
op = ' '
while op not in 'SN':
    op = str(input('Deseja mostrar processo: ')).strip().upper()
    if op == 'S':
        x = True
        break
    if op == 'N':
        x = False
        break
print(f'Fatorial de {numero} é: ')
fat = fatorial(numero, x)
print(fat)
