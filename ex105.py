def notas(*num, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma
    """
    dados = {}
    maior = menor = soma = cont = 0
    for x in num:
        if cont == 0:
            maior = menor = x
        else:
            if x > maior:
                maior = x
            if x < menor:
                menor = x
        soma += x
        cont += 1
    media = soma / cont
    if media >= 7:
        situacao = 'Boa'
    if 5 < media <= 6.9:
        situacao = 'Razoável'
    if media <= 5:
        situacao = 'Ruim'
    if sit:
        dados = {'Total': cont, 'Maior': maior, 'Menor': menor, 'Média': media, 'Situação': situacao}
    if not sit:
        dados = {'Total': cont, 'Maior': maior, 'Menor': menor, 'Média': media}
    return dados


boletim = notas(5.5, 2.5, 1.5, sit=True)
print(boletim)
