from Shape import Shape


class Circle(Shape):
    dx = 0.1  # x-offset
    dy = 0.1  # y-offset

    def __init__(self, goto=(0, 0), shape="circle", color="black"):
        super().__init__(goto, shape, color)