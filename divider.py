from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.2)
        self.color("white")
        self.goto(0, 290)
        self.draw_divider()

    def draw_divider(self):
        for _ in range(15):
            self.stamp()
            self.goto(self.xcor(), self.ycor() - 40)
