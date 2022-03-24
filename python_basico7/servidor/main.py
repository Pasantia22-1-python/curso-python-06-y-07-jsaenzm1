from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Jakeline del Rocío Sáenz Mogollón, curso python basic7 terminado.'


if __name__ == '__main__':
    app.run()
