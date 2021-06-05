from turtle import Turtle


class score(Turtle):
    def __init__(self):
        super().__init__()

        self.current_score = 0
        self.update_score()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()

    def increment_score(self):
        self.current_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.current_score}', align='center')

    def game_over(self):
        self.setpos(0,0)
        self.write('Game Over')

