from flask import Flask, render_template
from flask_wtf import  FlaskForm
from wtforms import StringField,EmailField,PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired,Email,Length
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class LoginForm(FlaskForm):
    email=EmailField("Email",validators=[DataRequired(),Email(),Length(min=5)])
    password=PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Login")
app = Flask(__name__)
app.secret_key = "saksham"

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/login',methods=["GET","POST"])
def login():
    login_form=LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data=="admin@gmail.com" and login_form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template('denied.html')

    return render_template("login.html",form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
