# database/crud.py

from sqlalchemy.orm import Session
from database.models import Pedido  # Certifique-se de que o modelo Pedido está correto
from datetime import datetime

def criar_pedido(db: Session, cliente_nome: str, cliente_telefone: str, cliente_endereco: str, cliente_cpf: str, cliente_data_nascimento: str, forma_entrega: str, forma_pagamento: str, tipo_pedido: str):
    # Verifica se os dados essenciais foram fornecidos
    if not cliente_nome or not cliente_telefone or not cliente_endereco:
        raise ValueError("Nome, telefone e endereço do cliente são obrigatórios.")

    # Valida o formato da data de nascimento (exemplo: "YYYY-MM-DD")
    try:
        data_nascimento = datetime.strptime(cliente_data_nascimento, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Data de nascimento deve estar no formato YYYY-MM-DD.")
    
    # Cria uma nova instância de Pedido
    novo_pedido = Pedido(
        cliente_nome=cliente_nome,
        cliente_telefone=cliente_telefone,
        cliente_endereco=cliente_endereco,
        cliente_cpf=cliente_cpf,
        cliente_data_nascimento=data_nascimento,
        forma_entrega=forma_entrega,
        forma_pagamento=forma_pagamento,
        tipo_pedido=tipo_pedido
    )
    
    # Adiciona o novo pedido à sessão do banco de dados
    db.add(novo_pedido)
    db.commit()  # Salva as alterações no banco de dados
    db.refresh(novo_pedido)  # Atualiza a instância do pedido com os dados do banco (incluindo o ID gerado)

    return novo_pedido
