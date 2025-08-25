#!/usr/bin/python3
#Technocalypse: A game made by the Virginia Western Community College
# Computer Science Club, written in python.
#Copyright (C) 2025  Cameron Reynolds

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.



import pygame
import math
from PIL import Image, ImageSequence
import os
import time

# Initialize pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Sound init will go here
menuTheme = pygame.mixer.Sound('usr/lib/technocalypse/assets/menu.mp3')
menuTheme.set_volume(0.55)
battleTheme = pygame.mixer.Sound('usr/lib/technocalypse/assets/battle.mp3')
roundStartTheme = pygame.mixer.Sound('usr/lib/technocalypse/assets/roundStart.mp3')

# Ends Program
def quit_program():
    print('Quitting game...')
    pygame.quit()
    exit()

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
roundFont = pygame.font.Font('usr/lib/technocalypse/assets/Technopath.otf', (y//10))

# Picture init
menuBackground = pygame.image.load('usr/lib/technocalypse/assets/menu.jpg')
menuBackground = pygame.transform.scale(menuBackground, (x, y))

# Game state
count = 0
score = 0
health = 3 # May change later

# Draw background
def draw_background():
    screen.blit(menuBackground, (0,0))

def draw_menu_text():
    for dx, dy in [(2, 2), (-2, -2), (2, -2), (-2, 2)]:
        outline_text_1 = titleFont.render('TECHNOCALYPSE', True, (255, 255, 255))
        screen.blit(outline_text_1, outline_text_1.get_rect(center=(x//2 + dx, y//2 + dy)))
        outline_text_2 = mediumFont.render('Press Space to Start', True, (255, 255, 255))
        screen.blit(outline_text_2, outline_text_2.get_rect(center=(x//2 + dx, (y//2 + y//6) + dy)))
    titleText = titleFont.render('TECHNOCALYPSE', True, (0, 0, 0,))
    screen.blit(titleText, titleText.get_rect(center=(x//2, y//2)))
    mediumText = mediumFont.render('Press Space to Start', True, (0, 0, 0,))
    screen.blit(mediumText, mediumText.get_rect(center=(x//2, y//2 + y//6)))

def draw_round_text(roundCount):
    stroundCount = str(roundCount)
    for dx, dy in [(2, 2), (-2, -2), (2, -2), (-2, 2)]:
        outline_text_2 = roundFont.render(('Round ' + stroundCount), True, (255, 255, 255))
        screen.blit(outline_text_2, outline_text_2.get_rect(center=(x//2 + dx, y//2 + dy)))

# Plan to expand this to gameplay events
def menu_handle_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_program()
            elif event.key == pygame.K_SPACE:
                menuTheme.stop()
                return 1

# Main menu
def main_menu():
    # Clears pygame event cache
    pygame.event.get()
    running = True
    menuTheme.play(loops=-1)
    while running == True:
        draw_background()
        draw_menu_text()
        pygame.display.update()
        # This is to make sure the cpu doesn't max out
        time.sleep(0.1)
        key = menu_handle_events()
        if key == 1:
            running = False
        

# Round start
def round_start():
    global count
    roundStartTheme.play()
    count += 1
    start_time = time.time()
    while (time.time() - start_time) < 4.5:
        time.sleep(0.1)
        screen.fill((0, 0, 0))
        draw_round_text(count)
        pygame.display.update()
    
# Main loop
def main():
    round_start()

main_menu()
main()
clock.tick(60)