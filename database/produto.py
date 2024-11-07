from sqlalchemy import Column, Integer, String, Float, DECIMAL
from database.init_db import Base

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # Exemplo: Marmita Completa, Marmita+Refri, etc.
    preco = Column(DECIMAL(10, 2), nullable=False)  # Usando DECIMAL para precisão financeira
    descricao = Column(String)  # Opcional, para detalhes adicionais

    def __repr__(self):
        return f"<Produto(id={self.id}, nome={self.nome}, tipo={self.tipo}, preco={self.preco})>"
