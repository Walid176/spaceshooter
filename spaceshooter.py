import pygame
import os
import time
import random
pygame.font.init()

WIDTH = 750
HEIGHT = 750
WIN =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

Red_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
Green_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
Blue_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

Yellow_space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

Red_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
Blue_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
Green_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
Yellow_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png"))), (WIDTH, HEIGHT)

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    
    def collision(self, obj):
        return collide(self, obj)