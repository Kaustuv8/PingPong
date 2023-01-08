import turtle as t
Z = 10 # Direction Control for Paddle 1
Z2 = 10 # Direction Control for Paddle 2

class Player_Start():

    def __init__(self):
        Timmy = []
        Pos = -380
        for i in range(2):
            Turt = t.Turtle("square")
            Turt.hideturtle()
            Turt.color("white")
            Turt.penup()
            Turt.turtlesize(4, 1)
            Turt.setpos(Pos, 0)
            Pos += 760
            Turt.showturtle()
            Timmy.append(Turt)
        # Player Data is now stored in the player attributes which is in form of a list
        self.players = Timmy
    def DefaultMove(self):
        global Z, Z2
        self.players[0].sety(self.players[0].ycor()+Z)
        self.players[1].sety(self.players[1].ycor() + Z2)

    def up1(self):
        # Controls for player 1
        global Z
        Z = 10
    def down1(self):
        # Controls for player 1
        global Z
        Z = -10

    def up2(self):
        # Controls for player 2
        global Z2
        Z2 = 10
    def down2(self):
        # Controls for player 2
        global Z2
        Z2 = -10

    def BoundaryCheck(self):
        #Reverse direction of the paddles when they hit the boundary
        global Z, Z2
        if self.players[0].ycor() > 250 or self.players[0].ycor()< -250:
            Z = -Z
        if self.players[1].ycor() > 250 or self.players[1].ycor()< -250:
            Z2 = -Z2


