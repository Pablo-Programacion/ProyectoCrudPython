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
    sql = "SELECT * FROM provincia"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    provincia = cursor.fetchall()
    conn.commit()
    return render_template('view/indexProvincia.html', provincia=provincia)


@app.route('/insertarprovincia')
def insertarprovincia():
    return render_template('view/crearProvincia.html')


@app.route('/eliminarProvincia/<int:codigo>')
def eliminar(codigo):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM provincia where codigo = %s", (codigo))
    conn.commit()
    return redirect('/')


@app.route('/editarProvincia/<int:codigo>')
def editar(codigo):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM provincia where codigo = %s", (codigo))
    provincia = cursor.fetchall()
    conn.commit()
    return render_template('view/editarProvincia.html', provincia=provincia)


@app.route('/actualizarProvincia', methods=['POST'])
def actualizarProvincia():
    _codigo = request.form['txtCodigo']
    _provincia = request.form['txtProvincia']
    sql = "UPDATE provincia SET nombre=%s where codigo=%s"
    datos = (_provincia,_codigo)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/')


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
    return render_template('view/indexProvincia.html')


if __name__ == '__main__':
    app.run(debug=True)
