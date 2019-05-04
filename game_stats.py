import pygame

import functions as func

from card import Card
from settings import Settings

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width,
                                  settings.screen_height))

class GameStats():
    """A class to store the stats of Blackjack"""
    
    def __init__(self):
        """Initializes stats"""
        # Lists needed to manage deck/hands
        self.deck = func.get_deck(Card, settings, screen)
        self.discard = []
        self.dealer_hand = []
        self.player_hand = []
        
        self.game_active = True
        self.hand_dealt = False