from flask import Flask
import random
app = Flask(__name__)

random_ans=random.randint(0,9)
@app.route('/')
def home_page():
    return ('<h1>Guess any Number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>')

@app.route('/<int:number>')
def answer(number):
    if number<random_ans:
        return ('<h1>Your Guess is too Low</h1>'
                '<p>Guess Any Other Larger than this</p>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>')
    elif number>random_ans:
        return ('<h1>Your Guess is too High</h1>'
                '<p>Guess Any Other Smaller than this</p>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>')
    else:
        return ('<h1>Your Guess is Correct</h1>'
                '<p>Congrats You are a Champion 🏆 </p>'
                '<img src=" https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>')


if __name__=="__main__":
    app.run(debug=True)
