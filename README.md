# 🍽 Restaurante Manager

Este projeto é uma aplicação web simples para gerenciar pedidos de um restaurante. Ele utiliza Python com Flask para o backend, HTML e CSS para a interface, e SQLAlchemy para interação com o banco de dados.

## 📝 Funcionalidades

- Interface de formulário para criar novos pedidos.
- Armazenamento e listagem de pedidos no banco de dados.
- Validação básica de dados no backend para garantir a integridade dos pedidos.
- Camada visual com uma imagem de fundo estilizada e caixas de formulário centralizadas.

## 💻Tecnologias Utilizadas

- **Python 3**: Linguagem principal do backend.
- **Flask**: Framework web para lidar com as rotas e exibir a interface HTML.
- **SQLAlchemy**: ORM para comunicação com o banco de dados.
- **HTML/CSS**: Interface visual da aplicação.
- **Logging**: Para registrar erros e eventos importantes.

## 🛠 Estrutura do Projeto

```
restaurante_manager/
├── app.py                  # Arquivo principal com rotas e lógica de pedidos
├── database/
│   ├── __init__.py         # Inicialização do banco de dados
│   ├── init_db.py          # Configuração e criação de sessões do banco
│   └── models.py           # Definição dos modelos do banco de dados
├── templates/
│   └── index.html          # Interface principal do formulário de pedidos
├── static/
│   └── images/
│       └── background.png  # Imagem de fundo da interface
└── README.md               # Documentação do projeto
````

## 🗒 Pré-requisitos

1. Python 3.8+ instalado.

2. Bibliotecas: Instale as dependências usando o seguinte comando:

````
pip install -r requirements.txt
````

Certifique-se de que o arquivo requirements.txt lista as bibliotecas Flask, SQLAlchemy, e qualquer outra necessária.

3. Banco de Dados: O banco de dados será criado e inicializado automaticamente com SQLAlchemy na primeira execução.

## Funcionalidades Futuras

1. Autenticação de usuários
2. Suporte para atualizar e deletar pedidos
3. Integração com um banco de dados relacional completo, como PostgreSQL ou MySQL
# restaurante_manager
