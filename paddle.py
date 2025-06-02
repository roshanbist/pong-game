from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def move_up(self):
        if self.ycor() < 260:
            new_y_pos = self.ycor() + 20
            self.goto(self.xcor(), new_y_pos)

    def move_down(self):
        if self.ycor() > -240:
            new_y_pos = self.ycor() - 20
            self.goto(self.xcor(), new_y_pos)
