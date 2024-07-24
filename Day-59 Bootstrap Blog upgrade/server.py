from flask import Flask, render_template
import requests



app = Flask(__name__)

response = requests.get("https://api.npoint.io/3eae95e9302e6d46a3c9")
all_blogs = response.json()

@app.route("/")
def home():
    return render_template("index.html", blogs=all_blogs)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# this is the method to use to not make multiple post pages
# this method retrieves the index of the link that is pressed and therefor is able to render and select the correct part of the json
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_blogs:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)