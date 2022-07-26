from turtle import Turtle, circle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.bounce_x = 1
        self.bounce_y = 1
        self.move_speed = 0.1
        

    def move(self):
        new_x = self.xcor() + 10 * self.bounce_x
        new_y = self.ycor() + 10 * self.bounce_y
        self.goto(new_x, new_y)

    def hit_wall(self):
        self.bounce_y *= -1
    
    def hit_paddle(self):
        self.bounce_x *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x *= -1
        self.bounce_y *= -1 
        
