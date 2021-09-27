from Circle import Circle
from Square import Square
from turtle import Screen


wn = Screen()
wn.title("Ping Pong by Kastenka_Masha")  # title of window
wn.bgcolor("yellow")  # background color of window
wn.setup(width=800, height=600)  # size of window
wn.tracer(0)  # disable automatic screen refresh, to increase the speed of the game

# Create shapes
paddle_a = Square((-350, 0))
paddle_b = Square((350, 0))
ball = Circle()

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")

# Main game loop
while True:
    wn.update()  # refresh the screen when the loop starts

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() - 40 < ball.ycor() < paddle_a.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1