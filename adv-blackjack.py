
### This version of the game is advanced as it uses OOP
### and functions and all the additional rules in BlackJack played in casinos


## This block of code creates the Deck class with class methods to generate the decks for each game
class Deck(object):

    diamonds = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    hearts = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    spades = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    clubs = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = diamonds + hearts + spades + clubs

    def __init__(self, decks = 0):
        self.decks = decks

    ### Deck methods
    def deck_creation(self):
        del self.decks[:]

        return Deck(
        decks = deck * random.randrange(1,8,1))
