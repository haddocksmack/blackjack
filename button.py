import pygame.font

class Button():
    """A class to generate buttons to facilitate gameplay"""
    
    def __init__(self, settings, stats, screen, msg, loc, button_color,
                 text_color = (255, 255, 255)):
        """Initializes button settings"""
        self.settings = settings
        self.stats = stats
        self.screen = screen
        self.screen_rect = stats.screen_rect
        
        # Sets dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's Rect and place it in the correct location
        self.loc = loc
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.loc
        
        # Prepare the message
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """Turn msg into a rendered image centered in the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw a blank button then draw the text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)