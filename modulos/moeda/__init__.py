def moeda(n):
    r = f'R$ {n:.2f}'
    return r.replace('.', ',')


def metade(n, form=False):
    r = n / 2
    if form:
        f = moeda(r)
        return f
    else:
        return r


def dobro(n, form=False):
    r = n * 2
    if form:
        f = moeda(r)
        return f
    else:
        return r


def aumentar(n, p, form=False):
    r = n + ((p / 100) * n)
    if form:
        f = moeda(r)
        return f
    else:
        return r


def diminuir(n, p, form=False):
    r = n - ((p / 100) * n)
    if form:
        f = moeda(r)
        return f
    else:
        return r


def resumo(n, a=0, b=0):
    print('=' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('=' * 30)
    print('Preço analisado: ', end='')
    f = moeda(n)
    print(f'{f:>13}')
    print('Dobro do preço:  ', end='')
    f = moeda(dobro(n))
    print(f'{f:>13}')
    print('Metade do preço: ', end='')
    f = moeda(metade(n))
    print(f'{f:>13}')
    if a < 10:
        print(f'0{a}% de aumento:  ', end='')
    else:
        print(f'{a}% de aumento:  ', end='')
    f = moeda(aumentar(n, a))
    print(f'{f:>13}')
    if b < 10:
        print(f'0{b}% de redução:  ', end='')
    else:
        print(f'{b}% de redução:  ', end='')
    f = moeda(diminuir(n, b))
    print(f'{f:>13}')
    print('-' * 30)
