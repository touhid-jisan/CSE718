import os
import math
import random
from turtle import back, title, width
import pygame

from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("2D Game Development Using Python")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5 #Speed of player


window = pygame.display.set_mode((WIDTH, HEIGHT))

# sprite will tell us if objects are colliding each other
# will handle collisions
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
        # how fast every single player move in every direction
        self.x_velocity = 0
        self.y_velocity = 0

        self.mask = None
        
        self.direction = "left"
        self.animation_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def move_left(self, velocity):
        self.x_velocity = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
            
            
    def mvoe_right(self, velocity):
        self.x_velocity = velocity
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
            
    def loop(self, fps):
        self.move(self.x_velocity, self.y_velocity)
        
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)
        
# get background information
def get_background(name):
    image = pygame.image.load(join("assets", "background", name))
    _, _, width, height = image.get_rect()
    
    tiles = []
    
    for i in range(WIDTH // width +1):
        for j in range(HEIGHT // height +1):
            position = [i * width, j *height]
            tiles.append(position)
            
    return tiles, image

# draw background
def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
        
    player.draw(window)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    
    player = Player(100, 100, 50, 50)
    
    run = True
    while run:
        clock.tick(FPS)  # run in 60 fps per second
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(window, background, bg_image, player)
    pygame.quit()
    quit()
    
    
if __name__ == "__main__":
    main(window)