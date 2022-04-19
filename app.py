from flask import Flask, render_template
from flaskext.mysql import MySQL

import ControladorODBC

app = Flask(__name__)
mysql = MySQL()
ControladorODBC.conectar
mysql.init_app(app)


@app.route("/")
def index():
    sql = "INSERT INTO `provincia` (`codigo`, `nombre`) VALUES (NULL, 'Valencia');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('view/index.html')


if __name__ == '__main__':
    app.run(debug=True)

