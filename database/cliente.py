# database/cliente.py

from sqlalchemy import Column, Integer, String, Date
from database import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)  # Define um limite de 100 caracteres
    aniversario = Column(Date)  # Ajustado para tipo Date
    whatsapp = Column(String(15))  # Define um limite de caracteres, ex.: "(XX) XXXXX-XXXX"
    endereco = Column(String(200))  # Define um limite de 200 caracteres para o endereço

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome={self.nome}, whatsapp={self.whatsapp})>"
