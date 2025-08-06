from bottle import Bottle, static_file

routes_static = Bottle()

@routes_static.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='static')

@routes_static.route('/data/<filename>')
def serve_data_images(filename):
    return static_file(filename, root='data')