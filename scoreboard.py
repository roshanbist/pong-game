from turtle import Turtle


class Scoreboard(Turtle):
    ALIGN = "center"
    FONT = ('Arial', 14, 'normal')
    FINAL_POINT = 5

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        positions = [(-100, 270), (100, 270)]
        scores = [self.left_score, self.right_score]
        labels= ["Player left: ", "Player right: "]

        # zip() function create a zip object i.e. ((pos[0], scores[0]), labels[0] ...)
        for position, score, label in zip(positions, scores, labels):
            self.goto(position)
            self.write(f"{label} {score}", align=self.ALIGN, font=self.FONT)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.left_score = 0
        self.right_score = 0
        if self.left_score == self.FINAL_POINT:
            self.write(f"Player Left wins", align=self.ALIGN, font=self.FONT)
        else:
            self.write(f"Player Right wins", align=self.ALIGN, font=self.FONT)
