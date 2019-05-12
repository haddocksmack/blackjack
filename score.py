import pygame.font

class Score():
    """A class to display player money/bet information"""
    
    def __init__(self, settings, stats, screen):
        """Initializes scoreboard info"""
        self.screen = screen
        self.settings = settings
        self.stats = stats
        
        # Fonts settings for scoring information
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        
        # Get placement locs for text
        self.wallet_left = settings.screen_width / 4
        self.bet_left = 3 * settings.screen_width / 4
        self.bottom_text = settings.screen_height - 40
        
        
    def prep_wallet(self):
        """Turn the wallet info into a rendered image"""
        wallet_str = "WALLET: $" + str(self.stats.player_wallet)
        self.wallet_image = self.font.render(wallet_str, True, self.text_color,
                                             self.settings.bg_color)
        
        # Display the wallet at the bottom left of the screen
        self.wallet_rect = self.wallet_image.get_rect()
        self.wallet_rect.bottomleft = (self.wallet_left, self.bottom_text)
        
    def prep_bet(self):
        """Turn the bet info into a rendered image"""
        bet_str = "BET: $" + str(self.stats.bet)
        self.bet_image = self.font.render(bet_str, True, self.text_color,
                                             self.settings.bg_color)
        
        # Display the wallet at the bottom right of the screen
        self.bet_rect = self.bet_image.get_rect()
        self.bet_rect.bottomright = (self.bet_left, self.bottom_text)
        
    def show_score(self):
        """Draw the score on the screen"""
        self.prep_wallet()
        self.prep_bet()
        self.screen.blit(self.wallet_image, self.wallet_rect)
        self.screen.blit(self.bet_image, self.bet_rect)