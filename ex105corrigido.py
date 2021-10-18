def notas(*num, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma
    """
    dados = {}
    dados['Total'] = len(num)
    dados['Maior'] = max(num)
    dados['Menor'] = min(num)
    media = dados['Média'] = sum(num) / len(num)
    if media >= 7:
        situacao = 'Boa'
    if 5 < media <= 6.9:
        situacao = 'Razoável'
    if media <= 5:
        situacao = 'Ruim'
    if sit:
        dados['Situação'] = situacao
        print(dados)
    if not sit:
        print(dados)
    return dados


boletim = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
