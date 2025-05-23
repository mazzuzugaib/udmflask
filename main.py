from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py')
#configurando a chave secreta para o uso de sessões

#instanciando o banco de dados
db = SQLAlchemy(app)

from views import *
if __name__ == '__main__':
    app.run(debug=True)
