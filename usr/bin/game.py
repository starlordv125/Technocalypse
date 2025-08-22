import pygame
import math
from PIL import Image, ImageSequence
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Font init will go here

# Sound init will go here

# Screen setup
screen_info = pygame.display.get_desktop_sizes()
if screen_info:
    x, y = screen_info[0]
else:
    pass # End program!!
screen = pygame.display.set_mode((x, y), pygame.FULLSCREEN)

