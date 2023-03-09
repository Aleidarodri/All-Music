# python3 -m venv venv
# source virtual/bin/active
# flask --app


from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "hola Ite"


@app.route("/bye")
def adios():
    return "bye bye"


if __name__ == '__main__':
    app.run()
