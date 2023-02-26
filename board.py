from figure import Figure
from score import Score

class Board:
    # Set the width and height of the game board, and the initial score to 0
    width = 10
    height = 20
    # Set the game board, falling block, next block to None
    board = []
    figure = None
    next_figure = None

    #Initialize the game board to a 2D list of 0s.
    def __init__(self):
        self.score = Score()
        self.board = []
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(0)
            self.board.append(line)


    # Creates a new falling block and sets the next block for the game.
    # If there is no next block, a new one is created.
    def create_figure(self):
        if self.next_figure is None:
            self.next_figure = Figure(4, 0)
        self.figure = self.next_figure
        self.next_figure = Figure(4, 0)


    # Move the falling block down by one unit.
    # If the falling block intersects with a placed block, move it back up and stop it.
    def go(self):
        self.figure.y += 1
        if self.intersect():
            self.figure.y -= 1
            self.stop()

    # Force the falling block to stop
    def down(self):
        while not self.intersect():
            self.figure.y += 1  # Move the block down
        self.figure.y -= 1  # Move the block back up by one unit


    # Move the falling block horizontally
    def move(self, d):
        self.figure.x += d # Move the block by the specified number of units


    # Stop the falling figure and place it on the game board
    def stop(self):
        for i in range(4):      # Iterate through the current block and set the positions on the game board to the current block's type
            for j in range(4):
                if i * 4 + j in self.figure.getFigure():
                    self.board[i + self.figure.y][j + self.figure.x] = self.figure.type + 1


    # Checks if a position is within the bounds of the game board
    # @param x The x position to check.
    # @param y The y position to check.
    # @return True if the position is within the bounds of the game board, False otherwise.
    def in_bounds(self, x, y):
        if self.width > x >= 0 and self.height > y >= 0:
            return True
        return False


    # Check if the falling block intersects with a placed block.
    # @return True if the falling block intersects with a placed block, False otherwise.
    def intersect(self):
        is_intersecting = False
        for i in range(4):      # Iterate through the current block
            for j in range(4):
                if i * 4 + j in self.figure.getFigure():      # Check if the current block position is out of bounds or if there is a placed block at the same position
                    if not self.in_bounds(j + self.figure.x, i + self.figure.y) or self.board[i + self.figure.y][j + self.figure.x] > 0:
                        is_intersecting = True
        return is_intersecting


    #Removes any complete lines
    #A complete line is defined as a row on the game board that is completely filled with placed blocks.
    #If a complete line is found, the rows above it are shifted down by one unit.
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):  # Iterate through the rows of the game board
            complete_line = True
            for j in range(self.width):
                if self.board[i][j] == 0:  # If there is an empty position in the current row, set to False
                    complete_line = False
            if complete_line:   # If complete_line still True, shit row down by one unit
                for x in range(i, 1, -1):
                    for y in range(self.width):
                        self.board[x][y] = self.board[x - 1][y]
                lines += 1
                self.score.set_score(lines * 100)

        # self.score += (lines * 100) score is not implemented yet
