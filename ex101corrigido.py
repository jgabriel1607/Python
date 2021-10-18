def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Voto Negado.'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opicional.'
    if 18 <= idade <= 65:
        return f'Com {idade} anos: Voto Obrigatório.'


nasc = int(input('Digite sua data de nascimento: '))
print(voto(nasc))
