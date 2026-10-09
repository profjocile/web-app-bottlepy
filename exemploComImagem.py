from bottle import route, run, static_file


@route('/')
def index():
    file = 'image.png'
    page = f'''
                <link rel="stylesheet" type="text/css" href="/static/style.css">
                <body>
                    <h1>Usando arquivos estáticos</h1>
                    <img style="height:300px; width:auto;" src="/static/{file}">
                    <p>Esta é uma figura embutida</p>
                </body>
            '''
    return page

@route('/static/<filename:path>')
def send_static(filename):
    print(filename)
    return static_file(filename, root='./static/')

run(host='localhost', port=8080)