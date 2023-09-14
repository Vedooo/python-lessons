from flask import Flask,render_template
import random
import datetime
import requests as rq

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().year
    name = "Vedat Kocoglu"
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=year, writer=name)


@app.route('/guess/<name>')
def guess(name):
    genderize_url = f'https://api.genderize.io?name={name}'
    gender_response = rq.get(url=genderize_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    agify_url = f'https://api.agify.io?name={name}'
    agify_response = rq.get(url=agify_url)
    agify_data = agify_response.json()
    age = agify_data["age"]
    return render_template('guess.html', name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    npoint_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    npoint_response = rq.get(url=npoint_url)
    npoint_datas = npoint_response.json()
    return render_template('blog.html', posts=npoint_datas)
    
if __name__ == "__main__":
    app.run(debug=True)
    
