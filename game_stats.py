import functions as func

class GameStats():
    """A class to store the stats of Blackjack"""
    
    def __init__(self):
        """Initializes stats"""
        # Lists needed to manage deck/hands
        self.deck = []
        self.discard = []
        self.dealer_hand = []
        self.player_hand = []