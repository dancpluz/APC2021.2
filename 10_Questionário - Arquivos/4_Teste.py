import os

arquivo = input()[22:]

if os.path.isfile(arquivo):
    print('O arquivo existe')
else:
    print('Arquivo inexistente')
