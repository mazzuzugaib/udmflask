import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class FormularioMusica(FlaskForm):
    titulo = StringField('Nome da música:', [validators.DataRequired(), validators.length(min=1, max=50)])
    artista = StringField('Artista:', [validators.DataRequired(), validators.length(min=1, max=50)])
    genero = StringField('Genero:', [validators.DataRequired(), validators.length(min=1, max=50)])
    cadastrar = SubmitField('Cadastrar')


def recupera(id):
    for nome_imagem in os.listdir(app.config['UPLOAD']):
        #transformando imagem para string
        nome = str(nome_imagem)
        #separando o nome da extensão. Dessa forma, o nome da imagem fica apenas o nome do arquivo
        #ex: album1.jpg -> album1
        #assim é possivel adicionar imagens com outras extensões
        nome = nome.split('.')

        if f'album{id}_' in nome[0]:
            return nome_imagem
        
    return '404.jpg'

def deleta(id):
    deletada = recupera(id)
    if deletada != '404.jpg':
        os.remove(os.path.join(app.config['UPLOAD'], deletada))

