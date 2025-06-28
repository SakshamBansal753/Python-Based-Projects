from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///movie.db"
db=SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column(String,nullable=False,unique=True)
    year:Mapped[int]=mapped_column(Integer)
    description:Mapped[str]=mapped_column(String,nullable=False)
    rating:Mapped[float]=mapped_column(Float,nullable=False)
    ranking:Mapped[int]=mapped_column(Integer)
    review:Mapped[str]=mapped_column(String)
    img_url:Mapped[str]=mapped_column(String)


# CREATE TABLE
with app.app_context():

    db.create_all()

class RatedMovieForm(FlaskForm):
    rating=StringField("Your Rating out of 10",validators=[DataRequired()])
    review = StringField("Your Review")
    submit = SubmitField("Done")




@app.route("/")
def home():
    result=db.session.execute(db.select(Movie))
    all_movies=result.scalars().all()
    return render_template("index.html",movies=all_movies)

@app.route("/edit",methods=["GET","POST"])
def edit():
    form=RatedMovieForm()
    movie_id=request.args.get("id")
    movie=db.get_or_404(Movie,movie_id)
    if form.validate_on_submit():
        movie.rating=float(form.rating.data)
        movie.review=str(form.review.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',movie=movie,form=form)

@app.route('/delete')
def delete():
    movie_id=request.args.get("id")
    movie=db.get_or_404(Movie,movie_id)

    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
