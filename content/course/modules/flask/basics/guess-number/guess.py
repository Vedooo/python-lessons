from flask import Flask
import random as rd

random_numb = rd.randint(0,9)
print(random_numb)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>'\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_numb:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif guess < random_numb:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"    
    
if __name__ == "__main__":
    app.run(debug=True)