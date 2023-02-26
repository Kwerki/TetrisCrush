import random

class Figure:
    """
    A class representing a Tetris figure.

    This class includes a list of possible figure shapes and colors, as well as methods to initialize a figure with a
    random shape and color, and rotate the figure.
    """

    # A list of figure shapes
    figures = [
        [[1, 5, 9, 13], [0, 1, 2, 3]],
        [[1, 4, 5, 9], [1, 4, 5, 6], [1, 5, 6, 9], [0, 1, 2, 5]],
        [[5, 6, 9, 10]],
        [[0, 1, 2, 4], [0, 1, 5, 9], [2, 4, 5, 6], [0, 4, 8, 9]],
        [[0, 1, 2, 6], [1, 5, 8, 9], [0, 4, 5, 6], [0, 1, 4, 8]],
        [[1, 2, 4, 5], [0, 4, 5, 9]],
        [[0, 1, 5, 6], [1, 4, 5, 8]],
        [[0, 0, 0, 0]],  # Gravity
        [[0, 1, 0, 1], [0, 4, 0, 0]],  # Freez
        [[1, 1, 5, 9]]  # Plant
    ]

    # A list of figure colors
    colors = [
        (112, 161, 255),
        (255, 71, 87),
        (255, 127, 80),
        (46, 213, 115),
        (236, 204, 104),
        (55, 66, 250),
        (181, 52, 113),
        (100, 100, 100),  # Gravity
        (150, 150, 250),  # Freez
        (0, 255, 0),      # Plant
        (255, 255, 255)   # Growing part
    ]

    def __init__(self, x, y):
        """
        Initialize the block with a random shape and color.

        :param x: The x-coordinate of the top-left corner of the block.
        :param y: The y-coordinate of the top-left corner of the block.
        """
        self.x = x
        self.y = y
        self.type = random.randint(0, 9)
        self.current_rotation = 0

    def rotate(self):
        """
        Rotate the block 90 degrees clockwise.
        """
        self.current_rotation = (self.current_rotation + 1) % len(self.figures[self.type])

    def getFigure(self):
        """
        Get the indices of the figures that make up the current shape of the block.

        :return: The indices of the figures that make up the current shape of the block.
        """
        return self.figures[self.type][self.current_rotation]
