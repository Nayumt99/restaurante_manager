# test_import.py
try:
    from config.settings import DATABASE_URL
    print("Importação bem-sucedida:", DATABASE_URL)
except ModuleNotFoundError as e:
    print("Erro:", e)
