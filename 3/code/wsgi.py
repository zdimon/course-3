from werkzeug.debug import DebuggedApplication



def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    r = 34+'444'
    return 'Hello, world!'

app = DebuggedApplication(app, evalex=True)

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8084, app)
        print('Serving on port 8084...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
