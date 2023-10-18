# """
# https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9497646#overview
# + For our version of the game we will only have a computer dealer and a human player.
# + We start with a normal deck of cards, you will create a representation of a deck with Python.
# """
# """
# In this milestone project you will be creating a Complete BlackJack Card Game in Python.
# Here are the requirements:
#     + You need to create a simple text-based BlackJack game
#     + The game needs to have one player versus an automated dealer.
#     + The player can stand or hit.
#     + The player must be able to pick their betting amount.
#     + You need to keep track of the player's total money.
#     + You need to alert the player of wins, losses, or busts, etc...
#
# And most importantly:
#     + You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use class
#       to help you define the Deck and the Players' hand. There are many ways to do this, so explore it well!
# """
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {'Two': 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # build card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n' + card.__str__()  # add each Card object's print string
        return "The deck has " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start wit zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # added to self.aces

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(bet, chips):
    try:
        if bet > chips.total:
            raise ValueError
    except ValueError:
        print("impossible vous ne disposez pas des fonds necessare pour ce pari !!!")


def hit(deck, hand):
    pass


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_chip = Chips()
print(take_bet(200, test_chip))
print(test_player.value)

print()


