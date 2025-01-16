from flask import (
    Flask, #библиотека 
    render_template, 
    redirect,
    request
)
from turtle import *

app = Flask(__name__)


        

@app.route("/", methods = ["GET", "POST"])
def get_home():
    return render_template("home.html")


@app.route("/str1", methods = ["GET", "POST"])
def get_str1():
    if request.method == "POST":
        t = Turtle()
        for i in range(4):
            t.forward(100)
            t.left(90)
        done()
        return render_template("str1.html" )
    return render_template("str1.html")

@app.route("/str2", methods = ["GET", "POST"])
def get_str2():
    return render_template("str2.html")




if __name__ == '__main__':
    app.run(debug=True)