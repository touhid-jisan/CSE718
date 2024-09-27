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
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)
        
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    
    run = True
    while run:
        clock.tick(FPS)  # run in 60 fps per second
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(window, background, bg_image)
    pygame.quit()
    quit()
    
    
if __name__ == "__main__":
    main(window)