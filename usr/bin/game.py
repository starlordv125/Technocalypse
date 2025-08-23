import pygame
import math
from PIL import Image, ImageSequence
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Sound init will go here
menuTheme = pygame.mixer.Sound('usr/lib/technocalypse/assets/menu.mp3')
battleTheme = pygame.mixer.Sound('usr/lib/technocalypse/assets/battle.mp3')

# Ends Program
def quit_program():
    print('Quitting game...')
    quit()

# Screen setup
screen_info = pygame.display.get_desktop_sizes()
if screen_info:
    x, y = screen_info[0]
else:
    print('Error: could not determine resolution')
    quit_program()
screen = pygame.display.set_mode((x, y), pygame.FULLSCREEN)

# Font init
menuFontSize = y//5
font = pygame.font.Font('usr/lib/technocalypse/assets/Techno.ttf', menuFontSize)

# Picture init
background = pygame.image.load('usr/lib/technocalypse/assets/menu_background.jpg')
background = pygame.transform.scale(background, (x, y))

# Game state
health = 3 # May change later
main_menu = True

# Draw background
def draw_background():
    screen.blit(background, (0,0))

def draw_menu_text():
    menuText = font.render('TECHNOCALYPSE', True, (0, 0, 0,))
    screen.blit(menuText, menuText.get_rect(center=(x//2, y//2)))

# Main menu
while main_menu == True:
    draw_background()
    draw_menu_text()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
clock.tick(60)