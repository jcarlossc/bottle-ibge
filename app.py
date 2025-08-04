from bottle import Bottle, run
from routes.route_graphic import route_graficos
from routes.route_static import routes_static

app = Bottle()
app.mount('/', route_graficos)
app.mount('/static', routes_static)

if __name__ == "__main__":
    run(app, host='localhost', port=8080, debug=True, reloader=True)

