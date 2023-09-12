import requests
from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
# export FLASK_APP= <flask currently working file.>
# flask run


@app.route('/')
def hello_world():
    return "Bye!"

# @app.route('/username/<name>')
# def greet(name):
#     return f'Hello {name}'
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return '<h1 style="text-align: center">Hello there</h1>' \
            f'<p style="text-align: center"> {name}, you are {number} years old</p>' \
            '<img src="https://www.akc.org/wp-content/uploads/2017/11/Pembroke-Welsh-Corgi-standing-outdoors-in-the-fall.jpg" alt="corki dog" width="300" height="200">' \
            '<img src="https://media.giphy.com/media/m5N9gsl3eE1C8HbPVF/giphy.gif" width="300" height="300" style="float: right; object-position: 50px ">'

@app.route('/bye')
def bye():
    return 'bye'

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)