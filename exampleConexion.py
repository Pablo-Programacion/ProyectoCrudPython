import pyodbc

import ControladorODBC as con

server = 'localhost'
bd = 'paqueteria'
user = 'root'
contrasena = ''

try:
    con.conectar('localhost','paqueteria','root','')
except:
    print('no')
