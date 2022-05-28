# Start of project: May 27, 2022
# Simulation of the card game "Gypsy Wars"

# Basic rules of the game:
# Cards are divided into 2 different categories
# Numbers - [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Face cards - [A, J, Q, K]
# Each player takes turns putting down a card in the center
# Face cards have special effects, A = 4, J = 1, Q = 2, K = 3
# If you put down a face card, opponent has to put n cards down consecutively,
# if they don't get another face card, you take the pile

# Cards
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
    """A class that represents a player in the game, who is in posession of a deck
    
