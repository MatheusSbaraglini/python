from bottle import get, route, run, request, template, TEMPLATE_PATH
from bottle import static_file, error
import os

'''
@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return '<center><h1>Hello ' + nome + '</h1></center>'
'''


# @get('/<filename:re:.*\.css>')
@route('/static/css/<filepath:path>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@route('/login')
def login():
    TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(
                         os.path.dirname(__file__), 'view')))
    return template('login')


def check_login(username, password):
    return True if(username == 'Matheus' and password == '123') else False


@route('/login', method='POST')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if check_login(username, password):
        return '<center><h1> Login realizado com sucesso! </h1></center>'
    else:
        return '<center><h1> Falha ao realizar o login </h1></center>'

@error(404)
def error404(error):
    TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(
                         os.path.dirname(__file__), 'view')))
    return template('pagina404')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=False, reloader=True)
