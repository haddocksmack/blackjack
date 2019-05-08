class Button():
    """A class to generate buttons to facilitate gameplay"""
    
    def __init__(self, stats, msg):
        """Initializes button settings"""
        self.stats = stats
        self.screen_rect = stats.screen_rect
        
        
        