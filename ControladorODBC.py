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
    sql = "INSERT INTO `paquete` (`codigo`, `descripcion`, `destinatario`, `direccion`, `codigo_provincia`, `dni_camionero`) VALUES (%s, %s, %s, %s, %s, %s);"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/paquete')


@app.route('/actualizarPaquete', methods=['POST'])
def actualizarPaquete():
    _codigo = request.form['txtCodigo']
    _descripcion = request.form['txtDescripcion']
    _destinatario = request.form['txtDestinatario']
    _direccion = request.form['txtDireccion']
    _codigo_provincia = request.form['txtProvinciaCodigo']
    _dni_camionero = request.form['txtDniCamionero']

    sql = "UPDATE `paquete` SET `descripcion` = %s, `destinatario` = %s, `direccion` = %s, `codigo_provincia` = %s, `dni_camionero` = %s WHERE `paquete`.`codigo` = %s;"
    datos = (_descripcion, _destinatario, _direccion,
             _codigo_provincia, _dni_camionero, _codigo)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/paquete')


@app.route('/editarPaquete2/<int:codigo>')
def editar2(codigo):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM paquete where codigo = %s", (codigo))
    paquete = cursor.fetchall()
    conn.commit()
    return render_template('view/Paquete/editarPaquete.html', paquete=paquete)


@app.route('/eliminarPaquete/<int:codigo>')
def eliminar2(codigo):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM paquete where codigo = %s", (codigo))
    conn.commit()
    return redirect('/paquete')


''' CAMIONEROS '''


@app.route("/camionero")
def indexcamionero():
    sql = "SELECT * FROM camionero"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    camionero = cursor.fetchall()
    conn.commit()
    return render_template('view/Camionero/indexCamionero.html', camionero=camionero)


@app.route('/insertarcamionero')
def insertarcamionero():
    return render_template('view/Camionero/crearCamionero.html')


@app.route('/storecamionero', methods=['POST'])
def storage3():
    _dni = request.form['txtDNI']
    _poblacion = request.form['txtPoblacion']
    _nombre = request.form['txtNombre']
    _telefono = request.form['txtTeléfono']
    _direccion = request.form['txtDireccion']
    _salario = request.form['txtSalario']
    datos = (_dni, _poblacion, _nombre, _telefono, _direccion, _salario)
    sql = "INSERT INTO `camionero` (`dni`, `poblacion`, `nombre`, `telefono`, `direccion`, `salario`) VALUES (%s, %s, %s, %s, %s, %s);"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/camionero')


@app.route('/eliminarCamionero/<string:dni>')
def eliminar3(dni):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM camionero where dni = %s", (dni))
    conn.commit()
    return redirect('/camionero')


@app.route('/actualizarCamionero', methods=['POST'])
def actualizarCamionero():
    _dni = request.form['txtDNI']
    _poblacion = request.form['txtPoblacion']
    _nombre = request.form['txtNombre']
    _telefono = request.form['txtTeléfono']
    _direccion = request.form['txtDireccion']
    _salario = request.form['txtSalario']
    sql = "UPDATE `camionero` SET `poblacion` = %s, `nombre` = %s, `telefono` = %s, `direccion` = %s, `salario` = %s WHERE `camionero`.`dni` = %s;"
    datos = (_poblacion, _nombre, _telefono, _direccion, _salario, _dni)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/camionero')


@app.route('/editarCamionero2/<string:dni>')
def editar3(dni):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM camionero where dni = %s", (dni))
    camionero = cursor.fetchall()
    conn.commit()
    return render_template('view/Camionero/editarCamionero.html', camionero=camionero)


''' CONDUCE '''


@app.route("/conduce")
def indexconduce():
    sql = "SELECT * FROM conduce"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conduce = cursor.fetchall()
    conn.commit()
    return render_template('view/Conduce/indexConduce.html', conduce=conduce)


@app.route('/insertarconduce')
def insertarconduce():
    return render_template('view/Conduce/crearConduce.html')


@app.route('/storeconduce', methods=['POST'])
def storage4():
    _dniCAMIONERO = request.form['txtDNICAMIONERO']
    _matriculaCAMIONERO = request.form['txtMATRICULACAMION']
    datos = (_dniCAMIONERO, _matriculaCAMIONERO)
    sql = "INSERT INTO `conduce` (`dni_camionero`, `matricula_camion`) VALUES (%s, %s);"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/conduce')


@app.route('/eliminarConduce/<string:id>')
def eliminar4(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM conduce where ID = %s", (id))
    conn.commit()
    return redirect('/conduce')


@app.route('/actualizarConduce', methods=['POST'])
def actualizarConduce():
    _id = request.form['txtID']
    _dniCAMIONERO = request.form['txtDNICAMIONERO']
    _matriculaCAMIONERO = request.form['txtMATRICULACAMION']
    sql = "UPDATE `conduce` SET `dni_camionero` = %s, `matricula_camion` = %s where ID = %s;"
    datos = (_dniCAMIONERO, _matriculaCAMIONERO,_id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/conduce')


@app.route('/editarConduce2/<string:id>')
def editar4(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM conduce where id = %s", (id))
    conduce = cursor.fetchall()
    conn.commit()
    return render_template('view/Conduce/editarConduce.html', conduce=conduce)


if __name__ == '__main__':
    app.run(debug=True)
