class Card():
    """Class to contain attributes of a card"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = 0
        
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
        