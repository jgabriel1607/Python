from modulos.moduloex115 import cabecalho

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao criar o arquivo.')
    else:
        cabecalho('Opção 1 - Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<52}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()






