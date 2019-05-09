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
        self.player_hand = []
        self.dealer_hand_value = 0
        self.player_hand_value = 0
        self.hand_value = 0
        
        self.game_active = False
        self.bet_made= False
        self.hand_dealt = False
        
        self.bet_buttons = []
        self.player_buttons = []
        self.play_button = []