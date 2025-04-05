import os
from main import app

def recupera(id):
    for imagem in os.listdir(app.config['UPLOAD']):
        if imagem == f'album`{id}':
            return imagem
        
    return '404.jpg'

