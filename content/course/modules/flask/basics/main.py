import requests
from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)

@app.route('/hello')
def hello_world():
    return 'Hello world!'

# export FLASK_APP= <flask currently working file.>
# flask run

if __name__ == "__main__":
    app.run()