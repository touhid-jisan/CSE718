import os
import math
import random
import pygame

from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("2D Game Development Using Python")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5 #Speed of player


window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)  # whill loop run in 60 fps per second
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()
    
    
if __name__ == "__main__":
    main(window)