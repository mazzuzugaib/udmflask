from sqlalchemy import create_engine


# Substitua pelos seus dados de conexão
usuario = "root"
senha = "tenet"
host = "localhost"
banco = "play_musica"

# Criar conexão
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}")

# Testar conexão
if engine:
    print('cabrunco')

