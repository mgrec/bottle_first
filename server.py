from bottle import route, run, template, error, view, static_file


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


run(host='localhost', port=8989)
