import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy.orm import sessionmaker
from database.init_db import initialize_database, engine
from database.models import Pedido
from database.crud import criar_pedido
from database.impressao import imprimir_pedido
import re
from datetime import datetime

# Configuração e inicialização da interface
root = tk.Tk()
root.title("Gerenciamento de Restaurante")

# Inicialização do banco de dados
initialize_database()

# Criação da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Função para validar dados de entrada
def validar_dados_pedido(cliente_nome, cliente_telefone, cliente_cpf, cliente_data_nascimento):
    if not cliente_nome or not cliente_telefone or not cliente_cpf or not cliente_data_nascimento:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        return False
    
    # Validação do CPF (exemplo simples, pode ser aprimorado)
    if not re.match(r'^\d{11}$', cliente_cpf):
        messagebox.showerror("Erro", "CPF inválido. Deve conter 11 dígitos.")
        return False

    # Validação da data de nascimento
    try:
        datetime.strptime(cliente_data_nascimento, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Erro", "Data de nascimento inválida. Use o formato YYYY-MM-DD.")
        return False

    return True

# Função para imprimir pedido
def imprimir_pedido_ui():
    pedido_id = entry_pedido_id.get()
    try:
        pedido_id = int(pedido_id)
        pedido = session.query(Pedido).get(pedido_id)
        if pedido:
            pdf_path = imprimir_pedido(pedido)
            messagebox.showinfo("Sucesso", f"Pedido impresso: {pdf_path}")
        else:
            messagebox.showwarning("Atenção", "Pedido não encontrado.")
    except ValueError:
        messagebox.showerror("Erro", "ID do pedido deve ser um número.")

# Função para criar um pedido
def criar_pedido_ui():
    cliente_nome = entry_cliente_nome.get()
    cliente_telefone = entry_cliente_telefone.get()
    cliente_endereco = entry_cliente_endereco.get()
    cliente_cpf = entry_cliente_cpf.get()
    cliente_data_nascimento = entry_cliente_data_nascimento.get()
    forma_entrega = combo_forma_entrega.get()
    forma_pagamento = combo_forma_pagamento.get()
    tipo_pedido = combo_tipo_pedido.get()

    # Validação dos dados
    if not validar_dados_pedido(cliente_nome, cliente_telefone, cliente_cpf, cliente_data_nascimento):
        return

    novo_pedido = criar_pedido(
        session,
        cliente_nome,
        cliente_telefone,
        cliente_endereco,
        cliente_cpf,
        cliente_data_nascimento,
        forma_entrega,
        forma_pagamento,
        tipo_pedido
    )
    messagebox.showinfo("Sucesso", f"Pedido criado com sucesso! ID do Pedido: {novo_pedido.id}")

# Componentes da interface para criação de pedido
tk.Label(root, text="Criar Pedido").pack()
tk.Label(root, text="Nome do Cliente").pack()
entry_cliente_nome = tk.Entry(root)
entry_cliente_nome.pack()

tk.Label(root, text="Telefone do Cliente").pack()
entry_cliente_telefone = tk.Entry(root)
entry_cliente_telefone.pack()

tk.Label(root, text="Endereço do Cliente").pack()
entry_cliente_endereco = tk.Entry(root)
entry_cliente_endereco.pack()

tk.Label(root, text="CPF do Cliente").pack()
entry_cliente_cpf = tk.Entry(root)
entry_cliente_cpf.pack()

tk.Label(root, text="Data de Nascimento (YYYY-MM-DD)").pack()
entry_cliente_data_nascimento = tk.Entry(root)
entry_cliente_data_nascimento.pack()

tk.Label(root, text="Forma de Entrega").pack()
combo_forma_entrega = ttk.Combobox(root, values=["Em Domicílio", "Retirada no Local"])
combo_forma_entrega.pack()

tk.Label(root, text="Forma de Pagamento").pack()
combo_forma_pagamento = ttk.Combobox(root, values=["Cartão de Crédito", "Cartão de Débito", "Pix", "Dinheiro"])
combo_forma_pagamento.pack()

tk.Label(root, text="Tipo de Pedido").pack()
combo_tipo_pedido = ttk.Combobox(root, values=["Marmita Completa", "Marmita com Refrigerante", "Marmita com Suco", "Refrigerante", "Suco", "Água com Gás", "Água sem Gás"])
combo_tipo_pedido.pack()

tk.Button(root, text="Criar Pedido", command=criar_pedido_ui).pack()

# Componentes para impressão
tk.Label(root, text="Imprimir Pedido").pack()
tk.Label(root, text="ID do Pedido").pack()
entry_pedido_id = tk.Entry(root)
entry_pedido_id.pack()
tk.Button(root, text="Imprimir Pedido", command=imprimir_pedido_ui).pack()

# Fechamento da sessão ao encerrar o programa
def fechar_sessao():
    session.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", fechar_sessao)
root.mainloop()
