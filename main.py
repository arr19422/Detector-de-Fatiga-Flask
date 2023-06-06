from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'lazzy_db'

conexion = MySQL(app)


@app.before_request
def before_request():
    print("Antes de la petición...")


@app.after_request
def after_request(response):
    print("Después de la petición")
    return response


@app.route('/')
def index():
    data = { }
    return render_template('index.html', data=data)


@app.route('/user/login>')
def contacto(username, password):
    data = { }
    return render_template('contacto.html', data=data)


def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "Ok"


@app.route('/travels')
def listar_cursos():
    data = {}
    try:
        travels = conexion.connection.travels()
        sql = "SELECT * FROM travels ORDER BY nombre ASC where user_id = 1"
        travels.execute(sql)
        cursos = travels.fetchall()
        # print(cursos)
        data['travesl'] = cursos
        data['mensaje'] = 'Exito'
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)


def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
