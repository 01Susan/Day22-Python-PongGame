from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
        self.paddle_move_length = 20

    # TODO 2. Creating a paddle
    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    # TODO 3. Controling both paddle

    def move_up(self):
        new_y = self.ycor() + self.paddle_move_length
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - self.paddle_move_length
        self.goto(self.xcor(), new_y)

    # TODO Increase the capacity of paddle

    def paddle_move_increase(self):
        self.paddle_move_length += 1

