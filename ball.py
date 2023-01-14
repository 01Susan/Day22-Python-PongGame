from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ball_x_move = 10
        self.ball_y_move = 10
        self.increase_speed = 0.1
        self.colors = ["white", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
                       "SeaGreen", "SlateGray"]

    # TODO 4. Creating a ball
    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")

    # TODO 5. Move the ball

    def move_ball(self):
        ball_new_x = self.xcor() + self.ball_x_move
        ball_new_y = self.ycor() + self.ball_y_move
        self.goto(ball_new_x, ball_new_y)

    # TODO 6. Detect wall and bounce the ball

    def bounce_y(self):
        self.ball_y_move *= -1

    def bounce_x(self):
        self.ball_x_move *= -1
        self.increase_speed *= 0.9

    # TODO 7. Bouncing the ball when it hit the paddle
    def bounce_paddle(self):
        ball_y_move = self.ycor() + self.ball_y_move
        ball_x_move = self.xcor() - self.ball_x_move
        self.goto(ball_x_move, ball_y_move)

    # TODO 8 Resetting the ball position to 0,0 when paddle miss the ball

    def reset_position(self):
        self.goto(0, 0)
        self.increase_speed = 0.1
        self.bounce_x()

    # TODO 9 Ball random color
    def random_ball_color(self):
        self.color(random.choice(self.colors))
