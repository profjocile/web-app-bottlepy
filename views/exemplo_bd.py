"""Exemplo de
<https://jocile.com/turmas/programador-de-sistema/uc2---programador-de-sistemas/pratica-crud-python-sqlite>
"""
import sqlite3
 
# 1. Abre a conexão com o arquivo do banco de dados (ou cria se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')
 
# 2. Cria o objeto cursor para enviar comandos SQL
cursor = conn.cursor()
 
print("Conexão estabelecida com sucesso!")

# 3. Executa a criação da tabela clientes se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
    );
''')
 
# Confirma a alteração estrutural no banco
conn.commit()
print("Tabela 'clientes' pronta para uso!")

def inserir_valores():
    """ 4 Inserindo valores na tabela clientes"""
    # Lista de tuplas com os dados de exemplo
    novos_clientes = [
        ("Brandom", "Brandon@example.com", "11 99999-0001"),
        ("Diogo", "Diogo@example.com", "11 99999-0002"),
        ("Olavo", "Olavo@example.com", "11 99999-0003")
    ]
    
    # Inserção em lote usando placeholders (?)
    cursor.executemany(
        "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?);",
        novos_clientes
    )
    
    # Salva permanentemente a inserção no arquivo do banco
    conn.commit()
    print(f"{cursor.rowcount} registros inseridos com sucesso!")

def visualizar():
    """ Executa a consulta """
    cursor.execute("SELECT id, nome, email, telefone FROM clientes;")
 
    # Recupera todas as linhas encontradas
    resultados = cursor.fetchall()
    
    print("\n--- Lista de Clientes ---")
    for id_, nome, email, telefone in resultados:
        print(f"ID: {id_} | Nome: {nome} | E-mail: {email} | Telefone: {telefone}")

def atualizar_email(id, email):
    """Edita o email de um cliente pelo id"""
    # 1. Atualizar e-mail de um cliente específico pelo ID
    cursor.execute(
        "UPDATE clientes SET email = ? WHERE id = ?;",
        (email, id)
    )
    # Confirma as alterações no banco de dados
    conn.commit()
    print("\nAlterações de atualização e exclusão aplicadas!")

def deletar(id):   
    # 2. Deletar um cliente específico pelo ID
    cursor.execute(
        "DELETE FROM clientes WHERE id = ?;",
        (id,)
    )
    
    # Confirma as alterações no banco de dados
    conn.commit()
    print("\nAlterações de atualização e exclusão aplicadas!")

visualizar()
atualizar_email(1, "ana.nova@example.com")
visualizar()
deletar(2)
visualizar()

cursor.close()
conn.close()
print("Conexão fechada com segurança.")
