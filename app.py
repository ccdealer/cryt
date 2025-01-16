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
        # x = request.form.get("word", type=int)
        # t = Turtle()
        # z = 100
        # c = 90
        # for i in range(x):
        #     if i%4 == 0:
        #         z += 10
        #     t.forward(z)
        #     t.left(90)
        # done()

        def draw_circle(color, x, y, radius):
            """Рисует круг заданного цвета, координат и радиуса."""
            penup()
            goto(x, y - radius)
            pendown()
            fillcolor(color)
            begin_fill()
            circle(radius)
            end_fill()

        def draw_ear(x, y, radius):
            """Рисует ухо."""
            draw_circle("brown", x, y, radius)

        def draw_eye(x, y, radius):
            """Рисует глаз."""
            draw_circle("black", x, y, radius)

        def draw_nose():
            """Рисует нос."""
            penup()
            goto(0, 40)
            pendown()
            dot(15, "pink")

        def draw_mouth():
            """Рисует рот."""
            penup()
            goto(-10, 20)
            pendown()
            setheading(-60)
            circle(20, 120)

        # Настройка окна
        bgcolor("lightblue")
        speed(5)

        # Тело
        draw_circle("orange", 0, -50, 100)

        # Голова
        draw_circle("orange", 0, 50, 70)

        # Уши
        draw_ear(-50, 120, 30)
        draw_ear(50, 120, 30)

        # Глаза
        draw_eye(-30, 80, 10)
        draw_eye(30, 80, 10)

        # Нос
        draw_nose()

        # Рот
        draw_mouth()

        # Лапы
        draw_circle("brown", -60, -150, 20)
        draw_circle("brown", 60, -150, 20)

        # Завершаем
        done()

        return render_template("str1.html" )
    return render_template("str1.html")

@app.route("/str2", methods = ["GET", "POST"])
def get_str2():
    return render_template("str2.html")




if __name__ == '__main__':
    app.run(debug=True)