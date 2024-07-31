from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Define base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with custom base class
db = SQLAlchemy(model_class=Base)

# Create Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"

# Initialize the application with the database
db.init_app(app)

# Define the Book model
class Book(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, nullable=False)
    author : Mapped[str] = mapped_column(String, nullable=False)
    rating : Mapped[float]= mapped_column(Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    # Fetch all books from the database, ordered by title
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    
    # Render the index template with the list of books
    return render_template("index.html", books=all_books)

# Route for adding a new book
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Get form data
        data = request.form
        # Create a new Book object
        book = Book(title=data["title"],author=data["author"],rating=data["rating"])
        # Add the new book to the database
        db.session.add(book)
        db.session.commit()
        
        # Redirect to the home page
        return redirect(url_for("home"))
    
    # If it's a GET request, render the add book form
    return render_template("add.html")

# Route for editing a book's rating
@app.route("/edit", methods=["GET","POST"])
def edit():
    if request.method == "POST":
        # Get the book ID from the form
        book_id = request.form["id"]
        # Fetch the book from the database
        book_update = db.get_or_404(Book,book_id)
        # Update the book's rating
        book_update.rating = request.form["rating"]
        # Commit the changes
        db.session.commit()
        # Redirect to the home page
        return redirect(url_for("home"))
    
    # If it's a GET request, render the edit form
    book_id = request.args.get("id")
    book = db.get_or_404(Book,book_id)
    return render_template("edit.html",book=book)

# Route for deleting a book
@app.route("/delete", methods=["GET"])
def delete():
    # Get the book ID from the URL parameters
    book_id = request.args.get("id")
    
    # Fetch the book from the database
    book = db.get_or_404(Book, book_id)
    # Delete the book
    db.session.delete(book)
    db.session.commit()
    # Redirect to the home page
    return redirect(url_for("home"))

# Run the application
if __name__ == "__main__":
    app.run(debug=True)