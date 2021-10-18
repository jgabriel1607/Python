from colorama import Fore, Back, Style
from time import sleep


def ajuda(msg):
    print(Fore.LIGHTWHITE_EX + Back.BLUE + '=' * (35 + len(msg)))
    print(f'  Acessando o Manual do comando {msg}.  ')
    print('=' * (35 + len(msg)))
    print(Style.RESET_ALL)
    sleep(1)
    print(Fore.LIGHTWHITE_EX + Back.WHITE)
    help(msg)
    print(Style.RESET_ALL)
    sleep(1)


while True:
    print(Fore.LIGHTWHITE_EX + Back.GREEN + '=' * 27)
    print('  SISTEMA DE AJUDA PyHELP  ')
    print('=' * 27)
    print(Style.RESET_ALL)
    mensagem = str(input('Função ou Biblioteca > ')).lower()
    if mensagem == 'fim'.strip().lower():
        break
    ajuda(mensagem)
