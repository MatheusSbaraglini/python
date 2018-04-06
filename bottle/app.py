from bottle import route, run, request


'''
@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return '<center><h1>Hello ' + nome + '</h1></center>'
'''


@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            username: <input name="username" type="text" />
            password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


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

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
