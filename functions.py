import sys

import pygame

from card import Card

def update_screen(settings, screen, deck):
    """Update images on the screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    
    deck[41].blitme()
    
    pygame.display.flip()
    
def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def get_deck(Card, settings, screen):
    """Creates a list with all cards in a standard deck of cards"""
    suits = ['clubs', 'hearts', 'spades', 'diamonds']    
    deck = [Card(rank, suit, settings, screen) for rank in range(1,14) for suit in suits]
    return deck