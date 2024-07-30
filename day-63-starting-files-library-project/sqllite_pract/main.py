import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-book-collection.db"

db.init_app(app)

class Books(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, nullable=False)
    author : Mapped[str] = mapped_column(String, nullable=False)
    rating : Mapped[float]= mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

with app.app_context():

    book = Books(
        title="Harry Potter",
        author="JK",
        rating=5.0
    )
    db.session.add(book)
    db.session.commit()








if __name__ == "__main__":
    app.run(debug=True)

