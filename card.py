import pygame

class Card():
    """Class to contain attributes of a card"""
    def __init__(self, rank, suit, settings, screen):
        self.rank = rank
        self.suit = suit
        self.screen = screen
        self.value = 0
        
        # Card image settings
        self.size = (settings.card_width, settings.card_height)
        self.image_path = self.get_image_path()
        self.image = pygame.image.load("images/card_back.png")
        self.image = pygame.transform.smoothscale(self.image, self.size)
        self.facedown = False
        
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.topleft = self.rect.topleft
        self.topleft = (0, 0)
        
    def get_card_value(self, rank, hand_value):
        """Assigns correct score to card"""
        if self.rank > 10:
            self.value = 10
        elif self.rank == 1:
            if hand_value > 10:
                self.value = 1
            else:
                self.value = 11
        else:
            self.value = self.rank
        
        return self.value
    
    def get_image_path(self):
        """Determines correct face image for card based on rank and suit"""
        self.image_path = "images/" + str(self.rank) + '_' + self.suit + '.png'

    def get_image(self, settings):
        """Loads and transforms correct image"""
        if self.facedown:
            self.image = pygame.image.load("images/card_back.png")
            self.image = pygame.transform.smoothscale(self.image, self.size)
        else:
            self.image = pygame.image.load(self.image_path)
            self.image = pygame.transform.smoothscale(self.image, self.size)
    
    def render_card(self, settings):
        """Draws card on screen in correct location and orientation"""
        self.get_image(settings)
        self.screen.blit(self.image, self.rect)