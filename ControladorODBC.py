from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
import app as p


def conectar():
    p.app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    p.app.config['MYSQL_DATABASE_USER'] = 'root'
    p.app.config['MYSQL_DATABASE_PASSWORD'] = ''
    p.app.config['MYSQL_DATABASE_DB'] = 'paqueteria'
