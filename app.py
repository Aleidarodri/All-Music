# python3 -m venv venv
# source virtual/bin/active
# flask --app


from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def main():
    return "hola Ite"


@app.route("/bye")
def adios():
    return "bye bye"


@app.route("/about")
def about():

    f = open('allmusic.json')
    data = json.load(f)
    f.close()
    return data


if __name__ == '__main__':
    app.run()
