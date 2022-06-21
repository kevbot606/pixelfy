from turtle import Turtle, Screen
from PIL import Image


class Scanner(Turtle):
    img = None
    path = None
    detail = 10
    img_width = None
    img_height = None
    columns = None
    rows = None
    x = 1
    y = 1
    x_jump = 1
    y_jump = 1
    area = 0
    color_data = []

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.hideturtle()
        self.screen.colormode(255)
        self.screen.screensize(2000, 2000)
        self.screen.listen()
        self.color_data = []
        self.get_img()
        self.set_res()
        self.calculations()

    def get_img(self):
        """Prompts for a file path, and opens the given image."""
        Scanner.path = self.screen.textinput("Locate IMG", "Copy/Paste IMG file path here:")
        Scanner.img = Image.open(Scanner.path)

    def set_res(self):
        """Prompts for a number between 1 and 10, which sets the number and size of dots to be printed, and in turn
        the level of abstraction. Numbers can be given outside this range, but these are the recommended ends for
        best results."""
        Scanner.detail = 10 * self.screen.numinput("Set definition", "Select the level of detail. 10 being the lowest "
                                                                     "and 1 being the highest level of detail.")
        # print(Scanner.detail)

    def calculations(self):
        """Performs calculations based on given image dimensions and desired detail level."""
        Scanner.img_width, Scanner.img_height = Scanner.img.size
        Scanner.rows = int(Scanner.img_height // Scanner.detail)
        Scanner.columns = int(Scanner.img_width // Scanner.detail)
        Scanner.x_jump = Scanner.img_width // Scanner.columns
        Scanner.y_jump = Scanner.img_height // Scanner.rows
        Scanner.area = Scanner.rows * Scanner.columns
        # print(Scanner.img_width, Scanner.img_height, Scanner.rows, Scanner.columns, Scanner.x_jump, Scanner.y_jump)

    def create_color_list(self):
        """Scans through given image, pulls color data from individual pixels, and appends them into a list."""
        for row in range(Scanner.rows):
            for column in range(Scanner.columns):
                pixel_color = Scanner.img.getpixel((Scanner.x, Scanner.y))
                Scanner.color_data.append(pixel_color)
                Scanner.x += Scanner.x_jump
            Scanner.y += Scanner.y_jump
            Scanner.x = 1
        # print(Scanner.color_data)
