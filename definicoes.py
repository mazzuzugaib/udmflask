import os
from main import app

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

