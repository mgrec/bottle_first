from bottle import route, run, template, error

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/')
def home():
    return "Hello World!"

run(host='localhost', port=8080)
