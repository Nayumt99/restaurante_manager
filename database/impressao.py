# database/impressao.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Pedido  # Certifique-se de que Pedido está corretamente definido
from config.settings import REPORT_DIRECTORY  # Importa o diretório de relatórios
import os

def imprimir_pedido(pedido: Pedido):
    # Verifica se o diretório de relatórios existe
    os.makedirs(REPORT_DIRECTORY, exist_ok=True)
    
    # Define o caminho do PDF dentro do diretório de relatórios
    pdf_path = os.path.join(REPORT_DIRECTORY, f"pedido_{pedido.id}.pdf")
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Adiciona informações do pedido no PDF
    c.drawString(100, 750, f"Pedido ID: {pedido.id}")
    c.drawString(100, 730, f"Cliente: {pedido.cliente.nome}")
    c.drawString(100, 710, f"Data: {pedido.data}")
    c.drawString(100, 690, f"Forma de Entrega: {pedido.forma_entrega}")
    c.drawString(100, 670, f"Forma de Pagamento: {pedido.forma_pagamento}")
    c.drawString(100, 650, f"Tipo de Pedido: {pedido.tipo_pedido}")

    # Salva o PDF
    c.save()
    return pdf_path
