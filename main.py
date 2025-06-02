import time
from turtle import Screen

from paddle import Paddle
from divider import Divider
from ball import Ball
from scoreboard import Scoreboard

# screen initial setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))

divider = Divider()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_on = True

while game_on:
    screen.update()
    
    # the lesser the value -> higher the speed
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # distance is measured from the center of ball to the center of paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() >= 350
            or ball.distance(left_paddle) < 50 and ball.xcor() <= -350):
        ball.x_bounce()

    # right player miss the ball
    if ball.xcor() > 371:
        ball.reset_position()
        scoreboard.left_point()

    # left player miss the ball
    if ball.xcor() < -371:
        ball.reset_position()
        scoreboard.right_point()

    # game over
    if (scoreboard.left_score == scoreboard.FINAL_POINT or
            scoreboard.right_score == scoreboard.FINAL_POINT):
        game_on = False
        scoreboard.game_over()


screen.exitonclick()
