expressao = str(input('Digite uma expressão: '))
parenteses = []
for simbolo in expressao:
    if simbolo == '(':
        parenteses.append('(')
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está errada.')
