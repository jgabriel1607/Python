def leiaint(i):
    while True:
        try:
            i = int(i)
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            break
        except (ValueError, TypeError):
            print('Você não digitou um número inteiro.')
            i = input('Digite um número inteiro: ')
        else:
            break
    return i


def leiafloat(f):
    while True:
        try:
            f = float(f)
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            break
        except ValueError:
            print('O usuário preferiu não digitar esse número.')
            f = 0
            f = float(f)
            break
        except:
            print('Você não digitou um número real.')
            f = input('Digite um número real: ')
        else:
            break
    return f


i = leiaint(input('Digite um número inteiro: '))
f = leiafloat(input('Digite um número real: '))
print(f'O valor inteiro digitado foi {i} e o real foi {f}.')
