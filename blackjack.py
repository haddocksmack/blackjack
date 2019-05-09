import sys

import pygame
from random import shuffle

from settings import Settings
from card import Card
from button import Button
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
    
    # Make the buttons
    play_button = Button(settings, stats, screen, settings.play_msg,
                         settings.play_loc, settings.play_button_color)
    
    hit_button = Button(settings, stats, screen, settings.hit_msg,
                         settings.hit_loc, settings.hit_button_color)
    stay_button = Button(settings, stats, screen, settings.stay_msg,
                         settings.stay_loc, settings.stay_button_color)
    
    deal_button = Button(settings, stats, screen, settings.deal_msg,
                         settings.deal_loc, settings.deal_button_color)
    bet_1_button = Button(settings, stats, screen, settings.bet_1_msg,
                         settings.bet_1_loc, settings.bet_1_button_color,
                          (0, 0, 0))
    bet_5_button = Button(settings, stats, screen, settings.bet_5_msg,
                         settings.bet_5_loc, settings.bet_5_button_color)
    bet_10_button = Button(settings, stats, screen, settings.bet_10_msg,
                         settings.bet_10_loc, settings.bet_10_button_color)
    bet_buttons = [deal_button, bet_1_button, bet_5_button, bet_10_button]
    
    # Make and shuffle the deck
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
            
        func.update_screen(settings, stats, screen, bet_buttons)
        
run_game()