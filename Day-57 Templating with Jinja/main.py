from flask import Flask, render_template
import requests


app = Flask(__name__)

# requesting data from the api
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_blogs = response.json()

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    return render_template("index.html",all=all_blogs)


@app.route("/blog/<num>")
def blog(num):
    return render_template(f"post{num}.html",all=all_blogs )

if __name__ == "__main__":
    app.run(debug=True)
