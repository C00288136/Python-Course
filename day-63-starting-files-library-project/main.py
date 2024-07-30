from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"

db.init_app(app)

class Book(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, nullable=False)
    author : Mapped[str] = mapped_column(String, nullable=False)
    rating : Mapped[float]= mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        book = Book(title=data["title"],author=data["author"],rating=data["rating"])
        db.session.add(book)
        db.session.commit()
        
        return redirect(url_for("home"))
        
        
    return render_template("add.html")

@app.route("/edit", methods=["GET","POST"])
def edit():
    
    if request.method == "POST":
        book_id = request.form["id"]
        book_update = db.get_or_404(Book,book_id)
        book_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book = db.get_or_404(Book,book_id)
    return render_template("edit.html",book=book)
    


if __name__ == "__main__":
    app.run(debug=True)

