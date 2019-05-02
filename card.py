import pygame

class Card():
    """Class to contain attributes of a card"""
    def __init__(self, rank, suit, settings, screen):
        self.rank = rank
        self.suit = suit
        self.screen = screen
        self.value = 0
        
        # Load the card images and get its rect
        self.image_path = self.get_image()
        self.front_image = pygame.image.load(self.image_path)
        self.front_image = pygame.transform.smoothscale(self.front_image,
                                                        (settings.card_width,
                                                         settings.card_height))
        self.back_image = pygame.image.load("images/card_back.png")
        self.back_image = pygame.transform.smoothscale(self.back_image,
                                                       (settings.card_width,
                                                        settings.card_height))
        
        self.facestate_image = self.front_image
        self.facedown = False
        
        self.rect = self.front_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
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
    
    def get_image(self):
        """Determines correct image for card based on rank and suit"""
        image_path = "images/" + str(self.rank) + '_' + self.suit + '.png'
        
        return image_path

    def is_facedown(self):
        """Determines if a card is to be rendered faceup or facedown"""
        if self.facedown:
            self.facestate_image = self.back_image
        else:
            self.facestate_image = self.front_image
    
    def blitme(self):
        """Draws the card at its current position"""
        self.screen.blit(self.facestate_image, self.rect)