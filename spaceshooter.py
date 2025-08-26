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
    
class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health  = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

