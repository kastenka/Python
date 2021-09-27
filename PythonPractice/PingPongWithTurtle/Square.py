from Shape import Shape


class Square(Shape):
    def __init__(self, goto, shape="square", color="red", shape_w=5, shape_l=1):
        super().__init__(goto, shape, color)
        self.shape_w = shape_w
        self.shape_l = shape_l
        self.shapesize(stretch_wid=self.shape_w, stretch_len=self.shape_l)  # set size of Square

    # function to move square (our paddle) up
    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    # function to move square (our paddle) down
    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
