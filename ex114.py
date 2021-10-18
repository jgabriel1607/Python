import requests
url = "http://www.pudim.com.br"
try:
    page = requests.get(url)
except:
    print('\033[0;31m O site Pudim não está acessível no momento. \033[m')
else:
    print('\033[0;32m Consegui acessar o site Pudim com sucesso! \033[m')