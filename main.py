import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboards import Scoreboard
import time

# TODO 1. Creating the screen or window having 800 width size and 600 height size
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
# Creating paddle in screen using Paddle Class
right_paddle = Paddle((350, 0))
# Adding a moving up and down feature in paddle
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
left_paddle = Paddle((-350, 0))
# Adding a moving up and down feature in paddle
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# Creating Ball in screen using Ball Class
ball = Ball()
# Showing an Scoreboard
score = Scoreboard()
# Main loop where game runs

is_game_on = True
while is_game_on:
    time.sleep(ball.increase_speed)
    # Updating the graphics
    screen.update()
    # Moving the ball from the center
    ball.move_ball()
    # If ball hit the top and bottom wall --> Ball will bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # Change the ball color
        ball.random_ball_color()
    # If ball hits the paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 330 or ball.distance(left_paddle) < 40 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect when R paddle missed
    if ball.xcor() > 370:
        left_paddle.paddle_move_increase()
        score.l_point()
        time.sleep(0.1)
        ball.reset_position()

    # Detect when L paddle missed
    if ball.xcor() < -370:
        right_paddle.paddle_move_increase()
        score.r_point()
        time.sleep(0.1)
        ball.reset_position()

    # if score reaches 10
    if score.r_score == 10 or score.l_score == 10:
        is_game_on = False
        score.count_points()

turtle.done()
