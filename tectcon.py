from sqlalchemy import create_engine

from sqlalchemy import create_engine, text

# Substitua pelos seus dados de conexão
usuario = "root"
senha = "tenet"
host = "localhost"
banco = "play_musica"

# Criar conexão
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}")

# Testar conexão com uma query simples
try:
    with engine.connect() as conexao:
        resultado = conexao.execute(text("SELECT 1"))
        print("Conexão bem-sucedida!", resultado.scalar())  # Deve imprimir 1
except Exception as e:
    print("Erro ao conectar:", e)

