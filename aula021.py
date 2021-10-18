'''
Interactive Help
Podemos usar a função help() dentro do console.
Uma vez utilizado, podemos escrever alguma outra função para sabermos tudo a respeito dela.



Doc Strings
Ao criar uma função personalizada, podemos criar um manual informando sobre o funcionamento dela.
Ex:
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
Assim quando o usuário colocar help(contador)
Aparecerá na tela as informações registradas na Doc String



Parâmetros Opcionais
Quando criamos uma função com quantidade parâmetros específicos mas ao chamar a função, inserimos uma quantidade
menor de parâmetros isso daria um erro.
Podemo então criar os parâmetros opcionais da seguinte maneira.
Ex:
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5) -> Será válido
somar(8, 4) -> Será válido e 'c' vai receber 0.
somar() -> Será válido e 'a' recebe 0, 'b' recebe 0, e 'c' recebe 0.



Escopo de variáveis
Variáveis globais funcionam em tudo.
Variávies locais funcionam por expemplo dentro apenas de um função.



Retorno de Valores.
Utilizamos o return, para enviar o resultado de uma função a uma variável.
Ex:
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'O valor das somas foi de {r1}, {r2} e {r3}')

O return pode ser qualquer tipo de varívavel, inclusive Operador Lógico.
'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


'''n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2}, {f3}')


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
if par(n):
    print('É par.')
else:
    print('Não é par.')
