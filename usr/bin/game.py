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
titleFont = pygame.font.Font('usr/lib/technocalypse/assets/Techno.ttf', (y//5))
mediumFont = pygame.font.Font('usr/lib/technocalypse/assets/Techno.ttf', (y//10))

# Picture init
background = pygame.image.load('usr/lib/technocalypse/assets/menu.jpg')
background = pygame.transform.scale(background, (x, y))

# Game state
health = 3 # May change later
main_menu = True

# Draw background
def draw_background():
    screen.blit(background, (0,0))

def draw_menu_text():
    for dx, dy in [(2, 2), (-2, -2), (2, -2), (-2, 2)]:
        outline_text_1 = titleFont.render('TECHNOCALYPSE', True, (255, 255, 255))
        screen.blit(outline_text_1, outline_text_1.get_rect(center=(x//2 + dx, y//2 + dy)))
        outline_text_2 = mediumFont.render('Press Space to Start', True, (255, 255, 255))
        screen.blit(outline_text_2, outline_text_2.get_rect(center=(x//2 + dx, (y//2 + 200) + dy)))
    titleText = titleFont.render('TECHNOCALYPSE', True, (0, 0, 0,))
    screen.blit(titleText, titleText.get_rect(center=(x//2, y//2)))
    mediumText = mediumFont.render('Press Space to Start', True, (0, 0, 0,))
    screen.blit(mediumText, mediumText.get_rect(center=(x//2, y//2 + 200)))

# Main menu
while main_menu == True:
    draw_background()
    draw_menu_text()
    menuTheme.play(loops=-1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
clock.tick(60)