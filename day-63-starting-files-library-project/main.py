from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        new_book = {
            "title": data["title"],
            "author" : data["author"],
            "rating" : data["rating"]
            }
        all_books.append(new_book)
        print(all_books)
        return redirect(url_for("home"))
        
        
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

