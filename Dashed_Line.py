from turtle import Turtle
class Linemaker(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(-280)
        self.left(90)
        Check = 1
        for i in range(-280,280,7):
            if Check == 1:
                self.pendown()
                self.forward(7)
                Check = 0
                self.penup()
            elif Check == 0:
                self.forward(7)
                Check = 1

