import turtle as t
class Scoreboard:
    def __init__(self):
        Score = []
        self.Score1 = 0
        self.Score2 = 0
        pos = -40
        for i in range(2):
            Board = t.Turtle()
            Board.hideturtle()
            Board.penup()
            Board.setpos(pos, 275)
            Board.color("white")
            Board.write("Score : 0", False, "center", font=('Ariel', 12, 'normal'))
            pos+=80
            Score.append(Board)
        self.scoreboard = Score

    def Update(self,i):
        if i == 0:
            self.Score1+=1
            self.scoreboard[i].clear()
            self.scoreboard[i].write(f"Score : {self.Score1}", False, "center", font=('Ariel', 12, 'normal'))
        if i == 1:
            self.Score2+=1
            self.scoreboard[i].clear()
            self.scoreboard[i].write(f"Score : {self.Score2}", False, "center", font=('Ariel', 12, 'normal'))

