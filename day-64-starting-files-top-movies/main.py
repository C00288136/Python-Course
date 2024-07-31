from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.getenv("api")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
# Define base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, nullable=False, unique=True)
    year : Mapped[str] = mapped_column(String)
    description : Mapped[str] = mapped_column(String)
    rating : Mapped[Float] = mapped_column(Float, nullable=True)
    ranking : Mapped[int] = mapped_column(Integer, nullable=True)
    review : Mapped[str] = mapped_column(String, nullable=True)
    img_url : Mapped[str] = mapped_column(String)

with app.app_context():
    db.create_all()

class movieForm(FlaskForm):
    rating = StringField(u'Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(u'Your review', validators=[DataRequired()])
    submit = SubmitField("Done")

class add_movie(FlaskForm):
    title = StringField(u"Movie Title",validators=[DataRequired()])
    submit = SubmitField("Add")


@app.route("/")
def home():
    # fetch all db tables
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = movieForm()
    movie_id = request.args.get("id")
    if request.method == "POST":    
        movie_update = db.get_or_404(Movie,movie_id)
        movie_update.rating = float(form.rating.data)
        movie_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    
    movie = db.get_or_404(Movie,movie_id)
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = add_movie()
    if request.method == "POST":
        
        url = f"https://api.themoviedb.org/3/search/movie?query={form.title.data}&include_adult=false&language=en-US&page=1"
        headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMzg3NjNmNjA4NmRiYjljYzlhNDA4MmY4YTEyOTBiNiIsIm5iZiI6MTcyMjQzNDk0My4xMjUxMjksInN1YiI6IjY2YWE0MjM3MWI2ZTIyNmMxMGExMGRiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xjAkYjw0KrpHI7GMQ5NFMJZnMAvF4Rt57RZsVU0gVUA"
}
        response = requests.get(url, headers=headers)
        data = response.json()["results"]

        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find_movie")
def find_movie():
    id = request.args.get('id')
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMzg3NjNmNjA4NmRiYjljYzlhNDA4MmY4YTEyOTBiNiIsIm5iZiI6MTcyMjQzNDk0My4xMjUxMjksInN1YiI6IjY2YWE0MjM3MWI2ZTIyNmMxMGExMGRiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xjAkYjw0KrpHI7GMQ5NFMJZnMAvF4Rt57RZsVU0gVUA"
}

    response = requests.get(url, headers=headers)
    data = response.json()
    year = data["release_date"][:4]
    

    MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/original/"
    new_movie = Movie(
    title=data['original_title'],
    year=data['release_date'][0:4],  # Extract the year from the release date
    description=data['overview'],
    img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}"
)
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('home'))


    
if __name__ == '__main__':
    app.run(debug=True)
