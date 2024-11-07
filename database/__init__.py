# database/__init__.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.settings import DATABASE_URL

# Criação da base declarativa
Base = declarative_base()

# Configuração do banco de dados usando DATABASE_URL do settings.py
engine = create_engine(DATABASE_URL)

# Configuração da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para inicializar o banco de dados
def initialize_database():
    from .models import Produto, Cliente, Pedido  # Importar aqui para evitar importação circular
    Base.metadata.create_all(bind=engine)
