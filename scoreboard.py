from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
       #  absolute - with open("C:\\Users\\irfan\\OneDrive\\Desktop\\data.txt",mode="r") as highscore: or ->
       #  absolute - with open("/Users/irfan/OneDrive/Desktop/data.txt",mode="r") as highscore:
       #  relitive path - the third (in code)
        with open("../../OneDrive/Desktop/data.txt",mode="r") as highscore:
            self.highscore =int(highscore.read())
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score:{self.highscore}", align=ALIGNMENT, font=FONT)
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_highscore(self):
        if self.score > self.highscore:
            with open("C:\\Users\\irfan\\OneDrive\\Desktop\\data.txt",mode = "w") as file:
                file.write(str(self.score))
            self.highscore= self.score
        self.score = 0
        self.update_scoreboard()
