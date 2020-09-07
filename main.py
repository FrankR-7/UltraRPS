import pygame as pg
import os

ROCK = pg.transform.scale(pg.image.load(os.path.join('Assets','rock.webp')), (230,180))
PAPER = pg.transform.scale(pg.image.load(os.path.join('Assets','paper.webp')), (200,250))
SCISSOR = pg.transform.scale(pg.image.load(os.path.join('Assets','scissors.webp')), (180,250))

VICT = pg.transform.scale(pg.image.load(os.path.join('Assets','victory.webp')), (180,250))
LOSE = pg.transform.scale(pg.image.load(os.path.join('Assets','defeat.webp')), (180,200))

WIDTH, HEIGHT = 900, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Ultra RPS')
pg.display.set_icon(SCISSOR)

GAME = {'rock':'scissors',
        'paper': 'rock',
        'scissors':'paper'}

def main():
    while True:
        pg.draw.rect(WIN, (255,255,255), (0,0,WIDTH, HEIGHT))
        WIN.blit(ROCK, (50, 50))
        WIN.blit(LOSE, (500, 50))
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

main()