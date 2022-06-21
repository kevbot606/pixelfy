from turtle import Turtle, Screen
from scanner import Scanner


class Dotter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.screen = Screen()
        self.screen.colormode(255)
        self.screen.listen()
        self.dot_size = round(Scanner.detail * 0.08)
        self.spacing = self.dot_size * 1.25
        self.dots_drawn = 0

    def print_dots(self):
        """Iterates through Scanner.color_data and prints a dot for each RGB tuple."""
        starting_x = 0
        starting_y = 0
        for color_tuple in Scanner.color_data:
            if self.dots_drawn % Scanner.columns == 0:
                starting_x = 0
                starting_y -= self.spacing
            elif self.dots_drawn == Scanner.area:
                break
            starting_x += self.spacing
            self.goto(starting_x, starting_y)
            self.dot(self.dot_size, color_tuple)
            self.dots_drawn += 1
