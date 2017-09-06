from bottle import route, run, template, error, view, static_file, request


# display if error 404
@error(404)
def error404(error):
    return 'Nothing here, sorry'


# load css
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./assets/css/')


# route for home
@route('/')
@view('templates/home')
def home(name='default'):
    return dict(name=name)


# route for home + arg name
@route('/name/<name>')
@view('templates/home')
def name(name='default'):
    return dict(name=name)


# route for form
# fake login form
@route('/form')
@view('templates/form')
def form(login="false"):
    return dict(login=login)


# route POST for form
# fake login
@route('/form', method='POST')
@view('templates/form')
def action_form(login="true"):
    username = request.forms.get('btl_username')
    password = request.forms.get('btl_pass')
    if username == 'test' and password == 'test':
        return dict(login=login)
    else:
        login = 'error'
        return dict(login=login)


run(host='localhost', port=8989)
