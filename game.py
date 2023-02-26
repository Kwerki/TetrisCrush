import pygame
from board import Board

class Game():
    def __init__(self):
        self.board = Board()
        self.frame = 0
        self.left_key_down = False
        self.right_key_down = False
        self.down_key_down = False
        self.PlantFigure_Grew = False

    def run(self, screen):
        run = True
        while run:
            if self.board.figure is None:
                self.board.create_figure()
                if self.board.intersect():
                    self.board.score.save_score()
                    self.board = Board()
                    continue

            self.frame = self.frame + 1

            if self.frame >= 6:
                if not (self.board.figure.type == 8):
                    self.board.go()
                    self.frame = 0

            run = self.check_events()
            self.draw_frame(screen)
            self.end_fall()
            pygame.time.Clock().tick(10)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.board.down()
                    self.board.stop()
                elif event.key == pygame.K_LEFT:
                    self.left_key_down = True
                elif event.key == pygame.K_RIGHT:
                    self.right_key_down = True
                elif event.key == pygame.K_UP:
                    self.board.figure.rotate()
                elif event.key == pygame.K_DOWN:
                    self.down_key_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left_key_down = False
                elif event.key == pygame.K_RIGHT:
                    self.right_key_down = False
                elif event.key == pygame.K_DOWN:
                    self.down_key_down = False

        if self.left_key_down:
            self.board.move(-1)
            if self.board.intersect():
                self.board.move(1)
        if self.right_key_down:
            self.board.move(1)
            if self.board.intersect():
                self.board.move(-1)
        if self.down_key_down:
            self.board.go()
            self.frame = 0

        return True

    def draw_frame(self, screen):
        screen.fill((0, 0, 0))
        self.board.score.draw_score(screen)

        # Draw Bord
        for i in range(self.board.height):
            for j in range(self.board.width):
                pygame.draw.rect(screen, (12, 12, 12), pygame.Rect(j * 40, i * 40, 40, 40), 1)
                # If there is a placed block in the grid position, draw it
                if self.board.board[i][j] > 0:
                    pygame.draw.rect(screen, self.board.figure.colors[self.board.board[i][j] - 1],
                        pygame.Rect(j * 40, i * 40, 40, 40))

        # Draw falling blocks
        if self.board.figure is not None:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.board.figure.getFigure():
                        pygame.draw.rect(screen, self.board.figure.colors[self.board.figure.type],
                            pygame.Rect((j + self.board.figure.x) * 40, (i + self.board.figure.y) * 40, 40, 40))

        pygame.display.flip()

    def end_fall(self):
        if self.board.intersect():

            # Plant Figure
            if not self.PlantFigure_Grew:
                for i in range(18):
                    for j in range(10):
                        if self.board.board[i][j] == 10 and self.board.board[i + 1][j] == 10 and \
                                self.board.board[i + 2][j] == 10:
                            for x in range(i, 0, -1):
                                if self.board.board[x][j] == 0 and not self.PlantFigure_Grew:
                                    self.board.board[x][j] = 11
                                    self.PlantFigure_Grew = True

            # GravityFigures
            if self.board.figure.type == 7:
                for y in range(10):
                    last_row = 19
                    for x in range(19, 0, -1):
                        if self.board.board[x][y] != 0:
                            if x != last_row:
                                self.board.board[last_row][y] = self.board.board[x][y]
                            last_row -= 1
                    for x in range(last_row, -1, -1):
                        self.board.board[x][y] = 0

            self.board.figure = None
            self.board.break_lines()
            self.PlantFigure_Grew = False