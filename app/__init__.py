'''
    07 setembro 2021 | 13:13

    Iniciando Desenvolvimento Web com
    Python e o Framework Flask

    Alterando o arquivo inicial do projeto
'''

from flask import Flask

app = Flask(__name__)

from app.controllers import default

'''
Comentando a seção de Hello World!
para ignorá-la nesta seção
Este bloco de código está sendo
implementado em um default.py no
diretório app/controllers/default.py

@app.route("/")
def index():
    return "Bem-vindo ao Flask"
'''



'''
Copyright (c) 2018 Copyright Holder All Rights Reserved.
'''
