import sys

import pygame
from random import shuffle

def update_screen(settings, stats, screen, score):
    """Update images on the screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    if not stats.game_active:
        stats.play_button.draw_button()
    elif stats.game_active and not stats.hand_dealt:
        for button in stats.bet_buttons:
            button.draw_button()
            
    else:
        for card in stats.player_hand:
            card.render_card()
        for card in stats.dealer_hand:
            card.render_card()
        
        for button in stats.player_buttons:
            button.draw_button()
            
    score.show_score()
    
    pygame.display.flip()
    
def check_events(settings, stats):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if stats.end_round:
            if event.type == pygame.MOUSEBUTTONDOWN:
                stats.reset_hands(settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check for collision with buttons and mouseclicks
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not stats.game_active:
                check_play_button(stats, mouse_x, mouse_y)
            elif not stats.bet_round:
                check_bet_buttons(stats, mouse_x, mouse_y)
            elif stats.hand_dealt:
                check_player_buttons(settings, stats, mouse_x, mouse_y)
            
                
def check_play_button(stats, mouse_x, mouse_y):
    """Checks for mouse click on play button to start game"""
    button_clicked = stats.play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        stats.game_active = True
            
def check_bet_buttons(stats, mouse_x, mouse_y):
    """Checks for mouse click on bet buttons before a deal"""
    for button in stats.bet_buttons:
        button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            # stats.bet_buttons =
            # [bet_1_button, bet_5_button, bet_10_button, deal_button]
            if button == stats.bet_buttons[0]:
                if stats.player_wallet > 0:
                    stats.bet += 1
                    stats.player_wallet -= 1
            if button == stats.bet_buttons[1]:
                if stats.player_wallet > 4:
                    stats.bet += 5
                    stats.player_wallet -= 5
            if button == stats.bet_buttons[2]:
                if stats.player_wallet > 9:
                    stats.bet += 10
                    stats.player_wallet -=10
            if button == stats.bet_buttons[3]:
                if stats.bet != 0:
                    stats.bet_round = True
                    
def check_player_buttons(settings, stats, mouse_x, mouse_y):
    """Checks for mouse click on player buttons after a deal"""
    for button in stats.player_buttons:
        button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            # stats.player_buttons = [hit_button, stay_button]
            if button == stats.player_buttons[0]:
                deal_player(settings, stats)
                if stats.player_hand_bust:
                    stats.end_round = True
                    end_round(stats)
                    
            if button == stats.player_buttons[1]:
                dealer_round(settings, stats)
            
def get_deck(Card, settings, stats, screen):
    """Creates a list with all cards in a standard deck of cards"""
    suits = ['clubs', 'hearts', 'spades', 'diamonds']    
    stats.deck.extend([Card(rank, suit, settings, stats, screen) for rank
                  in range(1,14) for suit in suits])

def first_deal(settings, stats):
    """Deals out initial hand to dealer and player"""
    deal_player(settings, stats)
    deal_dealer(settings, stats)
    deal_player(settings, stats)
    deal_dealer(settings, stats)
    stats.hand_dealt = True
    
def deal_player(settings, stats):
    """Deals a card to the player and displays it"""
    stats.in_player_hand = True
    stats.player_hand.append(stats.deck.pop(0))
    num = len(stats.player_hand)
    stats.player_hand[-1].topleft = ((20 * num + settings.card_width * num),
                                     (stats.screen_bottom - 198
                                      - settings.card_height))
    get_hand_value(stats)
    
def deal_dealer(settings, stats):
    """Deals a card to the dealer and displays it"""
    stats.in_player_hand = False
    stats.dealer_hand.append(stats.deck.pop(0))
    num = len(stats.dealer_hand)
    if num == 1:
        stats.dealer_hand[-1].facedown = True
    stats.dealer_hand[-1].topleft = ((20 * num + settings.card_width * num), 80)
    get_hand_value(stats)
    
def dealer_round(settings, stats):
    """Dealer finishes his round, holding at 17 or above"""
    # Hit until dealer hand value is 17 or above
    while stats.dealer_hand_value < 17:
        deal_dealer(settings, stats)
    
    end_round(stats)    
    stats.end_round = True

def get_hand_value(stats):
    """Determines current value of hand"""
    if stats.in_player_hand:
        hand = stats.player_hand
    else:
        hand = stats.dealer_hand
    
    # Keeps track of aces in hand
    ace_count = 0
    
    for card in hand:
        if card.rank == 1:
            ace_count += 1
        card.get_card_value()
        stats.hand_value += card.value
    
    # Check for aces if hand value exceeds 21
    while stats.hand_value > 21:
        if ace_count == 0:
            break
        stats.hand_value -= 10
        ace_count -= 1
        
    if stats.hand_value > 21:
        if stats.in_player_hand:
            stats.player_hand_bust = True
        else:
            stats.dealer_hand_bust = True
        
    if stats.in_player_hand:
        stats.player_hand_value = stats.hand_value
    else:
        stats.dealer_hand_value = stats.hand_value
    stats.hand_value = 0
    
def end_round(stats):
    """Determines winner of hand and resets for a new round"""
    stats.dealer_hand[0].facedown = False
    if stats.player_hand_bust:
        stats.player_hand_bust = True
    elif stats.dealer_hand_bust:
        stats.player_wallet += (2 * stats.bet)
    # Tie
    elif stats.player_hand_value == stats.dealer_hand_value:
        stats.player_wallet += stats.bet
    # Player win
    elif stats.player_hand_value > stats.dealer_hand_value:
        stats.player_wallet += (2 * stats.bet)
    # Dealer win - nothing needs done - bet just needs reset to 0
        
def shuffle_deck(deck):
    """Shuffles deck"""
    shuffle(deck)
    
def check_deck(stats):
    """Tools to check current state of deck."""
    # Delete function once game is finished
    for pcard in stats.deck:
        print(str(pcard.rank) + " " + pcard.suit)
    print("There are " + str(len(stats.deck)) + " cards left in the deck.")
    print("Dealer hand value: " + str(stats.dealer_hand_value))
    print("Player hand vaule: " + str(stats.player_hand_value))
    
def make_buttons(settings, stats, screen, Button):
    """Creates all buttons for game"""
    # Play button
    stats.play_button = Button(settings, stats, screen, settings.play_msg,
                               settings.play_loc, settings.play_button_color)
    
    # Player buttons
    hit_button = Button(settings, stats, screen, settings.hit_msg,
                         settings.hit_loc, settings.hit_button_color)
    stay_button = Button(settings, stats, screen, settings.stay_msg,
                         settings.stay_loc, settings.stay_button_color)
    
    # Bet buttons
    bet_1_button = Button(settings, stats, screen, settings.bet_1_msg,
                         settings.bet_1_loc, settings.bet_1_button_color,
                          (0, 0, 0))
    bet_5_button = Button(settings, stats, screen, settings.bet_5_msg,
                         settings.bet_5_loc, settings.bet_5_button_color)
    bet_10_button = Button(settings, stats, screen, settings.bet_10_msg,
                         settings.bet_10_loc, settings.bet_10_button_color)
    deal_button = Button(settings, stats, screen, settings.deal_msg,
                         settings.deal_loc, settings.deal_button_color)
    
    stats.bet_buttons = [bet_1_button, bet_5_button, bet_10_button, deal_button]
    stats.player_buttons = [hit_button, stay_button]