from flask import Flask
import decorators

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@decorators.make_bold
@decorators.make_italic

def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)