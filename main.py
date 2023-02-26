import pygame
from game import Game

def main():

    # Starte PyGame Stuff
    pygame.init()
    screen = pygame.display.set_mode((500, 800))
    pygame.display.set_caption("Tetris Crush")

    # Starte Game Modul Tetris Crush
    game = Game()
    game.run(screen)

    pygame.quit()

main()