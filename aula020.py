"""
Funções
São rotinas que executam algo.
Podemos criar funções personalizadas de acordo com nossa necessidade.
Ex:
def mostraLinha():
    print('-----------------------')
Onde def -> É Definir Função
Juntamente com a função temos o parâmetro.
Ex:
def mensagem(msg):
    print('-----------------------')
    print(msg)
    print('-----------------------')
Depois de definida a função com o parâmetro, podemos chamar a função e escrever algo específico como parâmetro.
Ex:
mensagem('Sistema de Alunos') -->
    -----------------------
    Sistema de Alunos
    -----------------------
Após escrever a definição da função, devemos deixar 2 linhas em branco para começar a escrever o código.
Na linguagem Python temos uma funcionalidade chamada de empacotador.
Ao criarmos uma função e definirmos seus parâmetros, mas quando chamamos a função, chamamos com parâmetros -->
para mais ou para menos do que tinhamos definido anteriormente vai apresentar erro.
Porém podemos criar parâmetros variáveis da seguinte forma:
Ex: funcao(*num)
Isso siginifica que não importa a quantidade de parametros que colocarmos, a função vai conseguir armazenar todos eles.

"""


def soma(a, b):
    print('=' * 20)
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('=' * 20)


'''def contador(* num):
    for v in num:
        print(f'{v} ', end='')
    print('Fim!')'''


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=2, a=6)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)







