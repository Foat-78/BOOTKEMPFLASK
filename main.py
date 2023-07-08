# print("Hello, Foat") # вывод

from flask import Flask     # Flask - это класс



app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Foat'


if __name__=='__main__':
    app.run()