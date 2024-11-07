# database/init_db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL  # Importa o DATABASE_URL de settings.py

# Cria o engine do banco de dados
engine = create_engine(DATABASE_URL)

# Cria a base declarativa
Base = declarative_base()

# Inicializa a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_database():
    """
    Inicializa o banco de dados criando todas as tabelas definidas nos modelos.
    Certifique-se de importar os modelos para evitar importações circulares.
    """
    import database.models  # Importa os modelos para registrar as tabelas
    Base.metadata.create_all(bind=engine)
