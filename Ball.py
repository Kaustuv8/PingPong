from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.turtlesize(1,1)
        self.ymove = 10
        self.xmove = 10
    def move(self):
        self.setpos(self.xcor() + self.xmove, self.ycor() + self.ymove)
    def Bounce(self):
        self.ymove*=-1
    def Bounce2(self):
        self.ymove*=-1
        self.xmove*=-1
    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.xmove*=-1