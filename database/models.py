from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.init_db import Base

class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))  # Chave estrangeira para relacionamento
    cliente_nome = Column(String, index=True)
    cliente_telefone = Column(String, index=True)
    cliente_endereco = Column(String, index=True)
    cliente_cpf = Column(String, index=True)
    cliente_data_nascimento = Column(Date)
    forma_entrega = Column(String)
    forma_pagamento = Column(String)
    tipo_pedido = Column(String)
    
    # Relacionamento com Cliente
    cliente = relationship("Cliente", back_populates="pedidos")

    def __repr__(self):
        return f"<Pedido(id={self.id}, cliente_nome={self.cliente_nome}, tipo_pedido={self.tipo_pedido})>"

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    telefone = Column(String, index=True)
    endereco = Column(String)
    cpf = Column(String, unique=True)
    data_nascimento = Column(Date)
    
    # Relacionamento com Pedido
    pedidos = relationship("Pedido", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf})>"
