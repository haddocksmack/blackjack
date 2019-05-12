import pygame

class Card():
    """Class to contain attributes of a card"""
    
    def __init__(self, rank, suit, settings, stats, screen):
        """Initializes card settings"""
        self.rank = rank
        self.suit = suit
        self.screen = screen
        self.value = 0
        
        # Card image settings
        self.topleft = (0, 0)
        self.size = (settings.card_width, settings.card_height)
        self.image_path = 'images/' + str(self.rank) + '_' + self.suit + '.png'
        self.facedown = False
        self.screen_rect = stats.screen_rect
        
    def get_card_value(self, stats):
        """Assigns correct score to card"""
        if self.rank > 10:
            self.value = 10
        elif self.rank == 1:
            self.value = 11
        else:
            self.value = self.rank
        
        stats.hand_value += self.value
            
        if stats.in_player_hand:
            hand = stats.player_hand
            bust = stats.player_hand_bust
        else:
            hand = stats.dealer_hand
            bust = stats.dealer_hand_bust
            
        # Ace Check
        if stats.hand_value > 21:
            self.ace_check(stats, hand)
        
        if stats.hand_value > 21:
            bust = True
         
         
    def ace_check(self, stats, hand):
        """Checks for aces and adjusts if needed"""
        ace_count = 0
        for card in hand:
            if card.rank == 1:
                ace_count += 1
        
        while stats.hand_value > 21:
            if ace_count == 0:
                break
            stats.hand_value -= 10
                
    def get_image(self):
        """Loads and transforms correct image"""
        if self.facedown:
            self.image = pygame.image.load("images/card_back.png")
        else:
            self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.smoothscale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
    
    def render_card(self):
        """Draws card on screen in correct location and orientation"""
        self.get_image()
        self.screen.blit(self.image, self.rect)