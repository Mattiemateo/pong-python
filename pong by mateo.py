import turtle

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("Yellow")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("Black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("Black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("Black")
ball.penup()
ball.goto(0, 0)
balldx = 2
balldy = 2


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

#keycontroll
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    #ballmoving
    ball.setx(ball.xcor() + balldx)
    ball.sety(ball.ycor() + balldy) 

    #ballbounce
    if ball.ycor() >  290:
        ball.sety(290)
        balldy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        balldy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        balldx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        balldx *= -1

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        balldx *= -1

    if ball.xcor() > 340 and ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50:
        ball.setx(340)
        balldx *= -1