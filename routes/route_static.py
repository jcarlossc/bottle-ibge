from bottle import Bottle, static_file

route_static = Bottle()

@route_static.route('/data/<filename>')
def serve_data_images(filename):
    return static_file(filename, root='data')