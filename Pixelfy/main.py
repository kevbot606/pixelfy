from turtle import Screen
from scanner import Scanner
from dotter import Dotter

screen = Screen()
scanner = Scanner()
dotter = Dotter()

scanner.create_color_list()
dotter.print_dots()

screen.exitonclick()
