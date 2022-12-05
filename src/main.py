# Library imports
import pygame
from pygame.locals import *

# User-library imports
import color

clock = pygame.time.Clock()

key_dict = {K_k:color.BLACK, K_r:color.RED, K_g:color.GREEN, K_b:color.BLUE,
    K_y:color.YELLOW, K_c:color.CYAN, K_m:color.MAGENTA, K_w:color.WHITE}

background = color.GRAY

pygame.init()
screen = pygame.display.set_mode((640, 240))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

                caption = 'background color = ' + str(background)
                pygame.display.set_caption(caption)

    screen.fill(background)
    pygame.display.update()
    # Limit frames per second to limit CPU usage
    clock.tick(60)


#Input handling: movement , attacking
#Sprite: pictures, images, font
#Run game sequence


pygame.quit()