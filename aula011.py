''' Cores em Python
Podemos utilizar o padrão ANSI para colocar cores no terminal
Para adicionar cores devemos utilizar o comando: \033[m
Entre \033[ e m devemos colocar o código correspondente ao estilo desejado.
Referente ao estilo desejado. Podemos colocar 3 códigos separados por ; cada.
Ex: \033[0;33;44m --> onde 0 é um estilo, 33 é cor do texto e 44 o background.
Estilo mais utilizados:
0: Nenhum estilo
1: Negrito
4: Sublinhado
7: Negativo
Sobre a cor do texto:
30: Branco
31: Vermelho
32: Verde
33: Amarelo
34: Azul
35: Roxo
36: Azul Claro
37: Cinza (Padrão)
Sobre a cor do background:
40: Branco
41: Vermelho
42: Verde
43: Amarelo
44: Azul
45: Roxo
46: Azul Claro
47: Cinza (Padrão)

'''

print('\033[0;30;41m Teste \033[m')




