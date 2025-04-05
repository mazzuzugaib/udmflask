import os

SECRET_KEY = 'satorarepotenetoperarotas'

# Configurando o banco de dados
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'tenet',
        servidor = 'localhost',
        database = 'play_musica'
    )

UPLOAD = os.path.dirname(os.path.abspath(__file__)) + '/uploads'