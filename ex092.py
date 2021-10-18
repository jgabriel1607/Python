from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento : '))
idade = date.today().year - ano
dados['Idade'] = idade
ctps = int(input('Carteira de Trabalho (Digite 0 se não possuir): '))
dados['CTPS'] = ctps
if ctps == 0:
    print('=' * 30)
    print(dados)
    for c, v in dados.items():
        print(f'{c} é', end=' ')
        print(f'{v}')
else:
    contratacao = int(input('Ano de Contratação: '))
    dados['Contratação'] = contratacao
    dados['Salário'] = float(input('Salário: R$ '))
    idadeapos = contratacao + 35
    aposentadoria = idadeapos - ano
    dados['Aposentadoria'] = aposentadoria
    print('=' * 30)
    print(dados)
    for c, v in dados.items():
        print(f'{c} é', end=' ')
        print(f'{v}')























