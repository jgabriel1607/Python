'''
Tratamento de erros.
Exceções. Não são necessáriamente erros no código.
NameError = Erro de nome, variável não iniciada.
ValueError = Erro de valor, não foi digitado algo do mesmo tipo solicitado.
ZeroDivisionError = Erro de divisão por zero.
TypeErroor = Erro de tipo.
IndexError = Erro de índice.
ModuleNotFoundError = Erro de modulo não encontrado.

Para tratamento de exceções vamos utilizar os comandos:
try: Operação.
except: Caso falhe.
else: Caso funcione.
finally: Caso falhe ou funcione.
Podemos utilizar o except Exception para mostra uma mesagem sobre o erro ocorrido.
Um mesmo 'try' pode ter vários 'exception'
'''

'''try:
    a = int(input('Numerador: '))
    b = int(input('Denomidaor: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre. Muito Obrigado.')'''


try:
    a = int(input('Numerador: '))
    b = int(input('Denomidaor: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre. Muito Obrigado.')