from flask import Flask, render_template, request, jsonify
from database.init_db import SessionLocal, engine
from database.models import Pedido, Base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import logging

app = Flask(__name__)

# Configuração do logger para registrar informações e erros
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criação das tabelas no banco de dados, se não existirem
Base.metadata.create_all(bind=engine)

# Inicializa a sessão do banco de dados
def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pedidos', methods=['POST'])
def criar_pedido():
    data = request.json
    logger.info("Dados recebidos para novo pedido: %s", data)

    # Validação básica dos dados recebidos
    required_fields = ["cliente_nome", "cliente_telefone", "cliente_endereco", "cliente_cpf", "cliente_data_nascimento", "forma_entrega", "forma_pagamento", "tipo_pedido"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"O campo '{field}' é obrigatório."}), 400

    # Criação do novo pedido
    try:
        novo_pedido = Pedido(
            cliente_nome=data['cliente_nome'],
            cliente_telefone=data['cliente_telefone'],
            cliente_endereco=data['cliente_endereco'],
            cliente_cpf=data['cliente_cpf'],
            cliente_data_nascimento=datetime.strptime(data['cliente_data_nascimento'], '%Y-%m-%d').date(),
            forma_entrega=data['forma_entrega'],
            forma_pagamento=data['forma_pagamento'],
            tipo_pedido=data['tipo_pedido']
        )

        # Uso do gerador `get_db_session` para abrir e fechar a sessão automaticamente
        session = next(get_db_session())
        session.add(novo_pedido)
        session.commit()
        logger.info("Pedido criado com sucesso: %s", novo_pedido)
        return jsonify({"message": "Pedido criado com sucesso!"}), 201

    except SQLAlchemyError as e:
        logger.error("Erro ao criar o pedido: %s", str(e))
        return jsonify({"error": "Erro ao criar o pedido no banco de dados."}), 500

    finally:
        session.close()  # Fechar a sessão após a transação

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    try:
        # Uso do gerador `get_db_session` para abrir e fechar a sessão automaticamente
        session = next(get_db_session())
        pedidos = session.query(Pedido).all()
        
        # Converte cada pedido para um dicionário
        pedidos_dict = [
            {
                "cliente_nome": pedido.cliente_nome,
                "cliente_telefone": pedido.cliente_telefone,
                "cliente_endereco": pedido.cliente_endereco,
                "cliente_cpf": pedido.cliente_cpf,
                "cliente_data_nascimento": pedido.cliente_data_nascimento.strftime('%Y-%m-%d'),
                "forma_entrega": pedido.forma_entrega,
                "forma_pagamento": pedido.forma_pagamento,
                "tipo_pedido": pedido.tipo_pedido,
                "id": pedido.id  # Inclua o ID do pedido, se aplicável
            }
            for pedido in pedidos
        ]
        logger.info("Listagem de pedidos enviada com sucesso.")
        return jsonify(pedidos_dict)

    except SQLAlchemyError as e:
        logger.error("Erro ao listar pedidos: %s", str(e))
        return jsonify({"error": "Erro ao listar pedidos do banco de dados."}), 500

    finally:
        session.close()

if __name__ == "__main__":
    app.run(debug=True)
