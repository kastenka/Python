from turtle import Turtle


class Shape(Turtle):
    def __init__(self, goto, shape, color):
        super().__init__(shape)
        self.speed(1)  # speed of animation
        self.color(color)
        self.penup()  # does not show animation
        self.goto(goto)  # starting point of Shape
