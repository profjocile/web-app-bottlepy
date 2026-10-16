import sqlite3

from bottle import get, redirect, request, route, run, template

DB_NAME = 'meu_banco_de_dados.db'
 
@route('/')
@get('/')
def index():
    msg_erro = request.query.get('erro', '')
    '''Futuramente implentar Banco de Dados
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()'''

    # Testando o Front End com uma lista de exemplos
    clientes = [{
                "nome" : "joão",
                "email" : "joao@gmail.com",
                "id": 1
            },
            {
                "nome" : "Fernando",
                "email" : "fernando@gmail.com",
                "id": 2
            }
        ]
 
    # Chama o arquivo views/index.tpl enviando os parâmetros
    return template('index', lista_clientes=clientes, msg_erro=msg_erro)
 
@get('/editar/<id:int>')
def exibir_formulario_edicao(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()
 
    if not cliente:
        redirect('/?erro=Cliente+não+encontrado')
 
    # Chama o arquivo views/editar.tpl
    return template('editar', cliente=cliente)
 
# (Demais rotas de cadastrar, salvar_edicao e deletar mantêm a lógica do banco de dados)
 
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)