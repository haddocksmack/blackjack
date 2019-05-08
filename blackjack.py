import sys

import pygame
from random import shuffle

from settings import Settings
from card import Card
import functions as func
from game_stats import GameStats

def run_game():
    # Initialize pygame, settings, and screen objects
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    stats = GameStats(screen)
    pygame.display.set_caption('Blackjack')
    func.get_deck(Card, settings, stats, screen)
    deck = stats.deck
    shuffle(deck)
      
    # Start the main game loop
    while True:
        func.check_events()
        
        if stats.game_active:
            if not stats.hand_dealt:
                func.first_deal(settings, stats)
                func.check_deck(deck, stats)
            
        func.update_screen(settings, stats, screen)
        
run_game()