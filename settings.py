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
        self.button_x = self.screen_width / 5
        self.button_y = self.screen_height - 65
        
        # Play Button
        self.play_msg = "PLAY"
        self.play_loc = ((self.screen_width / 2), (self.screen_height / 2))
        self.play_button_color = (0, 0, 255)
        
        # Deal button
        self.deal_msg = "DEAL"
        self.deal_loc = ((self.button_x * 4), self.button_y)
        self.deal_button_color = (0, 0, 0)
        
        # Bet 1 button
        self.bet_1_msg = "BET $1"
        self.bet_1_loc = (self.button_x, self.button_y)
        self.bet_1_button_color = (255, 255, 255)
        
        # Bet 5 button
        self.bet_5_msg = "BET $5"
        self.bet_5_loc = ((self.button_x * 2), self.button_y)
        self.bet_5_button_color = (255, 0, 0)
        
        # Bet 10 Button
        self.bet_10_msg = "BET $10"
        self.bet_10_loc = ((self.button_x * 3), self.button_y)
        self.bet_10_button_color = (0, 0, 255)
        
        # Hit button
        self.hit_msg = "HIT"
        self.hit_loc = ((self.button_x * 2), self.button_y)
        self.hit_button_color = (255, 0, 0)
        
        # Stay Button
        self.stay_msg = "STAY"
        self.stay_loc = ((self.button_x * 3), self.button_y)
        self.stay_button_color = (0, 0, 255)