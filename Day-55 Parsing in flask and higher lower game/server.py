from flask import Flask
import random
import decorators

app = Flask(__name__)

correct_num = random.randint(0,9)

# declare using the <int:> that the value passed in the url is to be seen as a int
@app.route("/<int:number>")
def user_guess(number):
    print(correct_num)
    if number < correct_num:
        return "<h1 style='color: red'> TOO LOW TRY AGAIN <br>\
            <img src=https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcndoaDJxNWowaHVwdzBwanVydnVkeXlldHlobG9oYXRtMWpraHNsdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fSowHvGwiV4e8OekpX/giphy.gif>"
    
    elif number > correct_num:
        return "<h1 style='color: red'> TOO HIGH TRY AGAIN <br>\
            <img src=https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem4yY3dsZXM5NmxpM25ncWc2b2N0cGN5dnR1Z3c0a241YzIxazlpbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wHB67Zkr63UP7RWJsj/giphy.gif>"
    
    if number == correct_num:
        return "<h1 style='color: blue'> CORRECT <br> \
            <img src=https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3Z5MTIzMTBpbG5qZTE4YmtkbXpycG9kcjY0NWJwb3Y3bWxtbzN4MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif>"
    
# starting page
@app.route("/")
def hello_world():
    return "<h1> Guess the number between 0 and 9 <br>\
        <img src=https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXhlZzFodWU3cGIzdjdqdzQ5MnZ4Nmo5aHlsMWVhYzV1a2RlcHIzZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohfFopqHDT7vcMM2A/giphy.gif>"


# if the name of the function is the running class app is ran
if __name__ == "__main__":
    app.run(debug=True)