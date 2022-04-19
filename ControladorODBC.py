from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'paqueteria'
mysql.init_app(app)


@app.route("/")
def index():
    return render_template('view/index.html')


@app.route("/provincia")
def indexprovincia():
    sql = "SELECT * FROM provincia"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    provincia = cursor.fetchall()
    conn.commit()
    return render_template('view/Provincia/indexProvincia.html', provincia=provincia)


@app.route('/insertarprovincia')
def insertarprovincia():
    return render_template('view/Provincia/crearProvincia.html')


@app.route('/eliminarProvincia/<int:codigo>')
def eliminar(codigo):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM provincia where codigo = %s", (codigo))
    conn.commit()
    return redirect('/provincia')


@app.route('/editarProvincia/<int:codigo>')
def editar(codigo):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM provincia where codigo = %s", (codigo))
    provincia = cursor.fetchall()
    conn.commit()
    return render_template('view/Provincia/editarProvincia.html', provincia=provincia)


@app.route('/actualizarProvincia', methods=['POST'])
def actualizarProvincia():
    _codigo = request.form['txtCodigo']
    _provincia = request.form['txtProvincia']
    sql = "UPDATE provincia SET nombre=%s where codigo=%s"
    datos = (_provincia, _codigo)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/provincia')


@app.route('/store', methods=['POST'])
def storage():
    _codigo = request.form['txtCodigo']
    _nombre = request.form['txtProvincia']
    datos = (_codigo, _nombre)
    sql = "INSERT INTO `provincia` (`codigo`, `nombre`) VALUES (%s, %s);"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/provincia')


''' PAQUETES '''


@app.route("/paquete")
def indexpaquete():
    sql = "SELECT * FROM paquete"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    paquete = cursor.fetchall()
    conn.commit()
    return render_template('view/Paquete/indexPaquete.html', paquete=paquete)


@app.route('/insertarpaquete')
def insertarpaquete():
    return render_template('view/Paquete/crearPaquete.html')


@app.route('/storepaquete', methods=['POST'])
def storage2():
    _codigo = request.form['txtCodigo']
    _descripcion = request.form['txtDescripcion']
    _destinatario = request.form['txtDestinatario']
    _direccion = request.form['txtDireccion']
    _codigo_provincia = request.form['txtProvinciaCodigo']
    _dni_camionero = request.form['txtDniCamionero']
    datos = (_codigo, _descripcion, _destinatario,
             _direccion, _codigo_provincia, _dni_camionero)
    print(datos)
    sql = "INSERT INTO `paquete` (`codigo`, `descripcion`, `destinatario`, `direccion`, `codigo_provincia`, `dni_camionero`) VALUES (%s, %s, %s, %s, %s, %s);"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/paquete')


@app.route('/actualizarPaquete', methods=['POST'])
def actualizarPaquete():
    _codigo = request.form['txtCodigo']
    _provincia = request.form['txtProvincia']
    sql = "UPDATE provincia SET nombre=%s where codigo=%s"
    datos = (_provincia, _codigo)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/provincia')


if __name__ == '__main__':
    app.run(debug=True)
