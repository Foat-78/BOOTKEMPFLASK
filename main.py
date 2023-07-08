# print("Hello, Foat") # вывод

from flask import Flask     # Flask - это класс



app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Hello, Foat</h1><br><a href='/index'>перейти на 2-ую страницу</a>"

# @app.route('/index')
# def index():
#     return "It's my first project"

@app.route('/index/<x>/<y>')
def index(x, y):
    return f'Результат: {int(x) + int(y)}' 

if __name__=='__main__':
    app.run()

    