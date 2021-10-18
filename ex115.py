from modulos import moduloex115
from modulos import arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoexiste(arq):
    arquivo.criararquivo(arq)

while True:
    x = moduloex115.menu(['Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if x == 1:
        arquivo.lerarquivo(arq)
    elif x == 2:
        moduloex115.cabecalho('Opção 2 - Cadastrar Nova Pessoa')
        nome = str(input('Nome: '))
        idade = moduloex115.leiaint(input('Idade: '))
        arquivo.cadastrar(arq, nome, idade)
    elif x == 3:
        moduloex115.cabecalho('Opção 3 - Sair do Sistema')
        print('Saindo do Sistema...')
        break
    else:
        print('\033[0;31mErro: Digite uma opção válida.\033[m')
    sleep(1)

