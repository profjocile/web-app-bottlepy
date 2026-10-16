"""Este exemplo testa os código de: 
<https://jocile.com/notas/python/bottle/templates-no-bottle>"""
from bottle import route, run, template


@route('/')
def teste():

    lista_clientes = [{
        "nome" : "joão",
        "email" : "joao@gmail.com",
        "ativo": True
    },{
    "nome" : "Fernando",
            "email" : "fernando@gmail.com",
            "ativo": True
        }]

    return template('Template_clientes', lista_clientes=lista_clientes)

run(host='localhost', port=8080)