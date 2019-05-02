import sys

import pygame

from settings import Settings
from card import Card
import functions as func

def run_game():
    # Initialize pygame, settings, and screen objects
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption('Blackjack')
    
    deck = func.get_deck(Card, settings, screen)
    
    # Start the main game loop
    while True:
        func.check_events()
        
        func.update_screen(settings, screen, deck)
        
run_game()