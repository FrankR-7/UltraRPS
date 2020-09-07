import pygame as pg

class Hand:
    def __init__(self, img):
        self.img = img
        self.disp = 250 - img.width # displacement
        self.y = 50
        self.dec = None
        self.prevs = []
