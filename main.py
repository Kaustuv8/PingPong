from turtle import Turtle, Screen
import random as rand
from Dashed_Line import Linemaker
from Scoreboard import Scoreboard
import Player as P
import Ball as B
import time
# Making the Screen
Sc = Screen()
Sc.bgcolor("Black")

# Marking the central line
Line = Linemaker()

# Making the two Vertical Bars
Players = P.Player_Start()
Sc.setup(800,600)
#Making the controls
Sc.listen()
Sc.onkey(Players.up1,"w")
Sc.onkey(Players.down1,"s")
Sc.onkey(Players.up2,"Up")
Sc.onkey(Players.down2,"Down")
# Making the Scoreboard
Board = Scoreboard()
# Calling the Ball
Ball = B.Ball()
#While Loop to make things go
while True:
    Players.DefaultMove()
    Players.BoundaryCheck()
    Ball.move()
    if Ball.ycor() > 280 or Ball.ycor()<-280:
        Ball.Bounce()
    if Ball.distance(Players.players[1]) < 50 and Ball.xcor() > 340:
        Ball.Bounce2()
    if Ball.distance(Players.players[0]) < 50 and Ball.xcor() < -340:
        Ball.Bounce2()
    if Ball.xcor() > 380:
        Ball.reset()
        Board.Update(0)
    if Ball.xcor() < -380:
        Board.Update(1)
        Ball.reset()

Sc.exitonclick()