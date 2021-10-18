n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número '))

r = n1 + n2
print('O resultado da soma é {}'.format(r))

r = n1 - n2
print('O resultado da subtração é {}'.format(r))

r = n1 * n2
print('O resultado da multiplicação é {}'.format(r))

r = n1 / n2 
print('O resultado da divisão é {}'.format(r))
# Se quiser colocar quantas casas decimais serão mostradas deve escrever da seguinte maneira:
# print('O resultado da divisão é {:.3f}'.format(r)), Assim terão 3 casas decimais.

r = n1 ** n2
print('O resultado da potência é {}'.format(r))

r = n1 // n2 
print('O resultado da divisão inteira é {}'.format(r))

r = n1 % n2
print('O resultado do resto da divisão é {}'.format(r))

# Operadores aritiméticos: +, -, *, /, **, //, %
# São respectivamente: adição, subtração, multiplicação, divisão, potência, divisão inteira, resto da divisão
# Ex:
# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.5
# 5 ** 2 = 25
# 5 // 2 = 2 Aqui temos uma divisão onde o resultado será sempre um número inteiro.
# 5 % 2 = 1 Aqui o é o resto da divisão da operação acima.
# Ordem de precedência. Ordem de importância para obter resultado em uma conta onde possui mais de 1 operador. 
# 1: ()
# 2: **
# 3: *, /, //, %
# 4: 	+, -
# Obs. Quando quisermos expressar igual dentro de uma operação demvemos usar o operador ==
# Ex: 
# 5 + 2 == 7
# Outro método para utilizar potência é:
# pow(4,3) Onde quero saber o resultado de 4 elevado a 3
# Calcular raiz quadrada. Raiz quadrada é elevar o número pela metade.
# Ex:
# 81**(1/2)==9.0 Ficará dessa maneira. 
# Se quiser saber a raiz cúbica de ser feito assim: 127**(1/3)==5.0


# É possível realizar operações com strings.
# Ex:
# 'Oi' + 'Olá' == OiOlá

p1 = input('Digite uma palavra: ')
p2 = input('Digite outra palavra: ')
print('Resultado da Concatenação é:', p1 + p2)

# Quebra de linha: \n
# Ex:
# print('Resultado da Concatenação é:\n', p1 + p2)

# É possível multiplicar também:
# p1*5 == p1p1p1p1p1p1

print('Palavra 1 repetida 5 vezes: ', p1 * 5)

# Continuar print na mesma linha end=' '
# Ex:
# print('Palavra 1 repetida 5 vezes: ', p1 *5, end=' ')

# Isso pode ajudar ao repetir símbolos também:

print('Símbolo de = repetido 20 vezes: ', '=' * 20)

# Outro exemplo de como podemos usar operadores:

nome = input('Digite seu nome: ')
print('Seja bem vindo {:20}!'.format(nome))
print('Seja bem vindo {:=>20}!'.format(nome))
print('Seja bem vindo {:=<20}!'.format(nome))
print('Seja bem vindo {:=^20}!'.format(nome))
