# python3 -m venv venv
# source virtual/bin/active
# flask --app app run -h ip


from flask import Flask, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'allmusic'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)


@app.route("/")
def main():
    return "hola Ite"


@app.route("/bye")
def adios():
    return "bye bye"


@app.route("/api/sql/test")
def listar():
    cursor = mysql.connection.cursor()
    sqlQuery = "SELECT * from canciones"
    cursor.execute(sqlQuery)
    canciones = cursor.fetchall()
    response = jsonify(canciones=canciones,
                       mensaje="Canciones listadas :)")
    cursor.close()
    return response


@app.route("/about")
def about():

    f = open('allmusic.json')
    data = json.load(f)
    f.close()
    return data


if __name__ == '__main__':
    app.run()
