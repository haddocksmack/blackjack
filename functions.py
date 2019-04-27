import sys

import pygame

def update_screen(settings, screen):
    """Update images on the screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    
    pygame.display.flip()
    
def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()