# config/settings.py

import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Configuração da URL do banco de dados SQLite (ou de outro banco)
DATABASE_URL = os.getenv("DATABASE_URL", 'sqlite:///restaurante.db')

# API Key para integração com o serviço de pagamento (exemplo fictício)
API_KEY = os.getenv("API_KEY", "default_key")

# Configurações para relatórios e impressão
REPORT_DIRECTORY = os.path.join(os.getcwd(), "reports")

# Função de utilidade para garantir que o diretório de relatórios existe
os.makedirs(REPORT_DIRECTORY, exist_ok=True)
