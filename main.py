# Assets:
import pygame
from pyradice.constants import GAME_WIDTH, GAME_HEIGHT
from pyradice.game import Game

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Py Ra Dice')

# def get_row_col_from_mouse(pos):
#     x, y = pos
#     row = y // SQUARE_SIZE
#     col = x // SQUARE_SIZE
#     return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        # if game.winner() != None:
        #     print(game.winner())
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # row, col = get_row_col_from_mouse(pos)
                # game.select(row, col)

        game.update()

    pygame.quit()

main()