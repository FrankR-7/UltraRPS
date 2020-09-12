import pygame as pg

class Hand:
    def __init__(self, img):
        self.img = img
        self.y = 400 - self.img.get_height()
        self.dec = None
        self.prevs = []

    def draw(self, win, bot=False):
        x = 75 if not bot else 625
        win.blit(self.img, (x, self.y))

class Button:
    def __init__(self, img, pos):
        self.img = pg.transform.scale(img, (100, 100))
        self.pos = pos
        self.y = 450
        if pos == 1:
            self.x = 175
        elif pos == 2:
            self.x = 400
        elif pos == 3:
            self.x = 625

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def is_pressed(self):
        mouse = pg.mouse.get_pos()
        return self.x < mouse[0] < self.x+100 and self.y < mouse[1] < self.y+100
