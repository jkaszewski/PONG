import turtle

# Okno gry
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paletka gracza A
paddle_a = turtle.Turtle()
paddle_a.speed(50)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paletka gracza B
paddle_b = turtle.Turtle()
paddle_b.speed(50)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Piłka
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Prędkość piłki w osi x
ball.dy = 0.2  # Prędkość piłki w osi y

# Wynik
score_a = 0
score_b = 0

# Tekst wyświetlający wynik
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Gracz A: 0  Gracz B: 0", align="center",
                     font=("Courier", 24, "normal"))


# Ruch paletki gracza A
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)


# Ruch paletki gracza B
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)


# Przypisanie klawiszy do ruchu paletki gracza A
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

# Przypisanie klawiszy do ruchu paletki gracza B
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# Główna pętla gry
while True:
    win.update()

    # Poruszanie piłką
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Odbicie piłki od górnej ściany
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Odbicie piłki od dolnej ściany
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Odbicie piłki od paletki gracza A
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1

    # Odbicie piłki od paletki gracza B
    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1

    # Piłka poza planszą - punkt dla gracza A
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.color("white")
        ball.dx *= -1
        score_a += 1
        score_display.clear()
        score_display.write("Gracz A: {}  Gracz B: {}".format(score_a, score_b), align="center",
                            font=("Courier", 24, "normal"))

    # Piłka poza planszą - punkt dla gracza B
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.color("white")
        ball.dx *= -1
        score_b += 1
        score_display.clear()
        score_display.write("Gracz A: {}  Gracz B: {}".format(score_a, score_b), align="center",
                            font=("Courier", 24, "normal"))
