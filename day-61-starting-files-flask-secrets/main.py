from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


# for wtforms you create a class for the form
class LoginForm(FlaskForm):
    # the email variable you assign as a string or any other field
    # first attribute is the label then you can add validators
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8 ,message="Password must be at least 8 characters")])
    submit = SubmitField(label="Log In")





app = Flask(__name__)

bootstrap = Bootstrap5(app)

app.secret_key = "apples"
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        print(form.email.data)
        print(form.password.data)
        return render_template("denied.html")
        
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
