from bottle import Bottle, run
from routes.routes_graficos import routes_graficos
from routes.routes_static import routes_static

app = Bottle()

app.mount('/static', routes_static)
app.mount('/', routes_graficos)
app.mount('/data', routes_static)

if __name__ == "__main__":
    run(app, host='localhost', port=8080, debug=True, reloader=True)

