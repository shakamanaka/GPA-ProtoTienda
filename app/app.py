from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    ## return "___" ## retornar plantilla HTML -> Las respuesta que queremos entregar
    canales = [ 'Youtube', 'Twitch', 'Kick', 'Instagram']
    data = {
        'titulo': 'Esgaritus',
        'bienvenida': '¡Saludos!',
        'follow' : 'Recuerda seguirme en: ',
        'canales' : canales,
        'cantidadCanales' : len(canales)
    }
    return render_template('index.html', data = data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data={
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad' : edad
    }
    return render_template('contacto.html', data = data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'OK'

def pag_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pag_no_encontrada)
    app.run(debug=True, port=5000)