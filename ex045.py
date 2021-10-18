from random import choice, randint
print('Vamos jogar Jokenpô!')
'''pc = choice(['TESOURA', 'PAPEL', 'PEDRA'])
jokenpo = str(input('Faça sua escolha: Tesoura, Papel ou Pedra: ')).upper().strip()

if pc == 'TESOURA' and jokenpo == 'TESOURA' or pc == 'PAPEL' and jokenpo == 'PAPEL' or pc == 'PEDRA' and jokenpo == 'PEDRA':
    print('Opa! Parece que empatou. Eu também também coloquei {}.'.format(pc))
elif pc == 'TESOURA' and jokenpo == 'PAPEL':
    print('Eu ganhei! {} ganha de {}.'.format(pc, jokenpo))
elif pc == 'PAPEL' and jokenpo == 'PEDRA':
    print('Eu ganhei! {} ganha de {}.'.format(pc, jokenpo))
elif pc == 'PEDRA' and jokenpo == 'TESOURA':
    print('Eu ganhei! {} ganha de {}.'.format(pc, jokenpo))
elif pc == 'PAPEL' and jokenpo == 'TESOURA':
    print('Você ganhou! {} ganha de {}.'.format(jokenpo, pc))
elif pc == 'PEDRA' and jokenpo == 'PAPEL':
    print('Você ganhou! {} ganha de {}.'.format(jokenpo, pc))
elif pc == 'TESOURA' and jokenpo == 'PEDRA':
    print('Você ganhou! {} ganha de {}.'.format(jokenpo, pc))'''
itens = ('Tesoura', 'Papel', 'Pedra')
pc = randint(0, 2)
jogador = int(input('Escolha: \n0. Tesoura \n1. Papel \n2. Pedra \n'))
print('O computador escolheu: {}.'.format(itens[pc]))
print('O jogador escolheu: {}.'.format(itens[jogador]))
if itens[pc] == itens[jogador]:
    print('Opa! Parece que deu empate.')
elif pc == 0 and jogador == 1:
    print('Ganhei! {} ganha de {}.'.format(itens[pc], itens[jogador]))
elif pc == 1 and jogador == 2:
    print('Ganhei! {} ganha de {}.'.format(itens[pc], itens[jogador]))
elif pc == 2 and jogador == 0:
    print('Ganhei! {} ganha de {}.'.format(itens[pc], itens[jogador]))
elif jogador == 0 and pc == 1:
    print('Você ganhou! {} ganha de {}.'.format(itens[jogador], itens[pc]))
elif jogador == 1 and pc == 2:
    print('Você ganhou! {} ganha de {}.'.format(itens[jogador], itens[pc]))
elif jogador == 2 and pc == 0:
    print('Você ganhou! {} ganha de {}.'.format(itens[jogador], itens[pc]))
