from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    
# for templates we use templates folder
# for css,images,videos etc. we use static folder