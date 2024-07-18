from flask import Flask, render_template
import time
import requests


app = Flask(__name__)

@app.route("/")
def home():
    current_year = time.strftime("%Y")
    name = "MICHAL K"
    return render_template("index.html", year=current_year, name=name)

@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    response = requests.get(f"https://api.genderize.io?name={name}")
    data = response.json()
    gender = data["gender"]
    probability = data["probability"]

    return render_template("name.html",name=name,gender=gender,probability=probability,age=age)
    


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)