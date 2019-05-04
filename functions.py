import sys

import pygame

def update_screen(settings, stats, screen, deck):
    """Update images on the screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    
    if len(stats.deck) > 52:
        first_deal(settings, stats)
    
    pygame.display.flip()
    
def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def get_deck(Card, settings, screen):
    """Creates a list with all cards in a standard deck of cards"""
    suits = ['clubs', 'hearts', 'spades', 'diamonds']    
    deck = [Card(rank, suit, settings, screen) for rank in range(1,14)
            for suit in suits]
    return deck

def first_deal(settings, stats):
    """Deals out initial hand to dealer and player"""
    deal_player(settings, stats)
    deal_dealer(settings, stats)
    deal_player(settings, stats)
    deal_dealer(settings, stats)
    
def deal_player(settings, stats):
    """Deals a card to the player and displays it"""
    num = len(stats.player_hand)
    stats.player_hand.append(stats.deck.pop(0))
    stats.player_hand[-1].topleft = ((80 + (20 * num + settings.card_width
                                            * num)), 650)
    stats.player_hand[-1].render_card(settings)
    
def deal_dealer(settings, stats):
    """Deals a card to the dealer and displays it"""
    num = len(stats.dealer_hand)
    if num == 1:
        stats.dealer_hand[-1].facedown = True
    stats.dealer_hand.append(stats.deck.pop(0))
    stats.dealer_hand[-1].topleft = ((80 + (20 * num + settings.card_width
                                            * num)), 100)
    stats.dealerer_hand[-1].render_card(settings)
    
def check_deck(deck):
    """Tools to check current state of deck."""
    # Delete function once game is finished
    for pcard in deck:
        print(str(pcard.rank) + " " + pcard.suit)
    print("There are " + str(len(deck)) + " cards left in the deck.")