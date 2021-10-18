from datetime import date


def voto(a=18):
    if a < 16:
        return 'Voto Negado.'
    if 16 <= a < 18 or a > 65:
        return 'Voto Opcional.'
    if 18 <= a <= 65:
        return 'Voto Obrigatório.'


atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc
res = voto(idade)
print(f'Com {idade} anos: {res}')
