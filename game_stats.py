import functions as func

class GameStats():
    """A class to store the stats of Blackjack"""
    
    def __init__(self, screen):
        """Initializes stats"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_bottom = self.screen_rect.bottom
        
        # Lists needed to manage deck/hands
        self.deck = []
        self.discard = []
        self.dealer_hand = []
        self.dealer_hand_bust = False
        self.player_hand = []
        self.player_hand_bust = False
        self.in_player_hand = True
        
        self.game_active = False
        self.bet_round= False
        self.hand_dealt = False
        self.end_round = False
        
        self.bet_buttons = []
        self.player_buttons = []
        self.play_button = []
        
        self.new_game()
        
    def reset_for_deal(self):
        """Resets bet to 0 for the beginning of a new hand"""
        self.dealer_hand_value = 0
        self.player_hand_value = 0
        self.hand_value = 0
        self.bet = 0
        
    def new_game(self):
        """Resets values to allow starting new game"""
        self.reset_for_deal()
        self.player_wallet = 100
    
    def reset_hands(self):
        """
        Moves cards from hands to discards and checks to see if shuffle
        is needed.
        """
        self.discard.extend(self.player_hand)
        self.discard.extend(self.dealer_hand)
        self.player_hand = []
        self.dealer_hand = []
        if len(self.deck) > 14:
            self.deck.extend(self.discard)
            func.shuffle(self.deck)
            
        self.dealer_hand_bust = False
        self.player_hand_bust = False
        
        self.bet_round = False
        self.hand_dealt = False
        self.end_round = False
            
        self.reset_for_deal()
            