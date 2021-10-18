p = ('Curso', 'Video', 'Python')
cont = 0
contl = 0
while True:
    while True:
        if p[cont][contl] in 'AaEeIiOoUu':
            print(p[cont][contl])
        contl += 1
        if contl >= len(p[cont]):
            break
    contl = 0
    cont += 1
    if cont >= len(p):
        break
