class Card:
    """A class that represents a card in a deck of 52 cards (no jokers)
    attributes:
    name -> str
    is_face -> bool
    value -> int
    """

    def __init__(self, name: str, value: int) -> None:
        """Initialize a new instance of a card"""
        self.name = name
        self.value = value
        if value in [1, 11, 12, 13]:
            self.is_face = True
        else:
            self.is_face = False
        
class Deck:
    """ A class that represents a deck of cards 
    attributes: 
    cards -> List[Card]
    """ 
    def __init__(self, cards: List[Card]) -> None:
        """Initialize a new instance of a deck"""
        self.cards = []
        for card in cards:
            self.cards.append(card)
    
    def is_empty(self):
        """Return whether or not this deck is empty"""
        return len(self.cards) == 0
    
class Player:
    """A class that represents a player in the game, who is in posession of a deck"""

    def __init__(self, turn):
        self.turn = False 