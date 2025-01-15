import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'banco_sqlite.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150),
    email VARCHAR(150)
)
""")

data = ("Wagner", "wsawebmaster@yahoo.com.br")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
conexao.commit()

conexao.close()