from sqlalchemy import create_engine

# Substitua pelos seus dados de conexão
usuario = "root"
senha = "tenet"
host = "localhost"
banco = "play_musica"

# Criar conexão
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}")

# Testar conexão
try:
    with engine.connect() as conexao:
        print("✅ Conexão bem-sucedida!")
except Exception as e:
    print(f"❌ Erro na conexão: {e}")

