import pygame

class Card():
    """Class to contain attributes of a card"""
    def __init__(self, rank, suit, settings, screen):
        self.rank = rank
        self.suit = suit
        self.screen = screen
        self.value = 0
        
        # Card image settings
        self.topleft = (0, 0)
        self.size = (settings.card_width, settings.card_height)
        self.image_path = 'images/' + str(self.rank) + '_' + self.suit + '.png'
        self.facedown = False
        self.screen_rect = self.screen.get_rect()
        
    def get_card_value(self, hand_value):
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