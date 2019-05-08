class Settings():
    """A class to store all settings for Blackjack"""
    
    def __init__(self):
        """Initializes the games's static settings"""
        self.screen_width = 1440
        self.screen_height = 770
        self.bg_color = (40, 120, 20)
        
        # Card settings
        self.card_width = 138
        self.card_height = 211
        
        # Button settings
        # Deal button
        self.deal_msg = "DEAL"
        self.deal_loc = (100, 100)
        self.deal_button_color = (0, 0, 0)