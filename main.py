import pygame as pg
import os
from classes import Hand, Button

ROCK = pg.transform.scale(pg.image.load(os.path.join('Assets','rock.webp')), (230,180))
PAPER = pg.transform.scale(pg.image.load(os.path.join('Assets','paper.webp')), (200,250))
SCISSOR = pg.transform.scale(pg.image.load(os.path.join('Assets','scissors.webp')), (180,250))

VICT = pg.transform.scale(pg.image.load(os.path.join('Assets','victory.webp')), (180,250))
LOSE = pg.transform.scale(pg.image.load(os.path.join('Assets','defeat.webp')), (180,200))

WIDTH, HEIGHT = 900, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Ultra RPS')
pg.display.set_icon(VICT)

game = {'rock':'scissor',
        'paper': 'rock',
        'scissor':'paper'}

counter = {y:x for x,y in game.items()}

sprites = {'vict': Hand(VICT),
           'lose': Hand(LOSE),
           'rock': Hand(ROCK),
           'paper': Hand(PAPER),
           'scissor': Hand(SCISSOR)}

buttons = [Button(ROCK, 1), Button(PAPER, 2), Button(SCISSOR, 3)]


def main():
    clock = pg.time.Clock()

    def main_menu():
        return

    def game():
        pSelect = 'rock'
        bSelect = 'rock'

        def update():
            WIN.fill((255,255,128))
            sprites[pSelect].draw(WIN)
            sprites[bSelect].draw(WIN, True)

            for button in buttons:
                button.draw(WIN)

            pg.display.update()

        while True:
            clock.tick(30)
            update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()

            if pg.mouse.get_pressed()[0]:
                if buttons[0].is_pressed():
                    pSelect = 'rock'
                elif buttons[1].is_pressed():
                    pSelect = 'paper'
                elif buttons[2].is_pressed():
                    pSelect = 'scissor'

            bSelect = counter[pSelect]


    def game_over():
        return

    while True:
        main_menu()
        game()
        game_over()

main()