import sys

import pygame

def update_screen(settings, stats, screen):
    """Update images on the screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    for card in stats.player_hand:
        card.render_card()
    for card in stats.dealer_hand:
        card.render_card()
    
    pygame.display.flip()
    
def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def get_deck(Card, settings, stats, screen):
    """Creates a list with all cards in a standard deck of cards"""
    suits = ['clubs', 'hearts', 'spades', 'diamonds']    
    stats.deck = [Card(rank, suit, settings, stats, screen) for rank
                  in range(1,14) for suit in suits]

def first_deal(settings, stats):
    """Deals out initial hand to dealer and player"""
    deal_player(settings, stats)
    deal_dealer(settings, stats)
    deal_player(settings, stats)
    deal_dealer(settings, stats)
    stats.hand_dealt = True
    
def deal_player(settings, stats):
    """Deals a card to the player and displays it"""
    stats.hand_value = stats.player_hand_value
    stats.player_hand.append(stats.deck.pop(0))
    num = len(stats.player_hand)
    stats.player_hand[-1].topleft = ((20 * num + settings.card_width * num),
                                     (stats.screen_bottom - 80
                                      - settings.card_height))
    stats.player_hand[-1].get_card_value(stats.player_hand_value)
    stats.player_hand_value += stats.player_hand[-1].value
    
def deal_dealer(settings, stats):
    """Deals a card to the dealer and displays it"""
    stats.hand_value = stats.dealer_hand_value
    stats.dealer_hand.append(stats.deck.pop(0))
    num = len(stats.dealer_hand)
    if num == 1:
        stats.dealer_hand[-1].facedown = True
    stats.dealer_hand[-1].topleft = ((20 * num + settings.card_width * num), 80)
    stats.dealer_hand[-1].get_card_value(stats.dealer_hand_value)
    stats.dealer_hand_value += stats.dealer_hand[-1].value
    
def check_deck(deck, stats):
    """Tools to check current state of deck."""
    # Delete function once game is finished
    for pcard in deck:
        print(str(pcard.rank) + " " + pcard.suit)
    print("There are " + str(len(deck)) + " cards left in the deck.")
    print("Dealer hand value: " + str(stats.dealer_hand_value))
    print("Player hand vaule: " + str(stats.player_hand_value))