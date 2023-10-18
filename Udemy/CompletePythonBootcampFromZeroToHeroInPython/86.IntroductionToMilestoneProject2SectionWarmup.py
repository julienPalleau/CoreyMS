"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662938#search
Introduction to Milestone Project2 Section WARMUP
+ To warm up for the 2nd Milestone Project we will recreate the card game called "War".
+ Let's have a quick overview of the game.
    - wikipedia.org/wiki/War_(card_game)

+ The "war" process can be repeated in this case of back to back ties.
+ To construct this game, we will create:
    - Card Class
    - Deck Class
    - Player Class
    - Game Logic

https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662940#search
Card Class
"""

# CARD
# SUIT, RANK, VALUE
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {'Two': 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662942#search

Deck Class 1/2
    + Instantiate a new deck
        - Create all 52 Card objects
        - Hold as a list of Card objects
    + Shuffle a Deck through a method call
        - Random library shuffle() function
    + Deal cards from the Deck object
        - Pop method from cards list

Deck Class 2/2
    + We will see that the Deck class holds a list of Card objects.
    + This means the Deck class will return Card class object instances, not just normal python data types.
"""


class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662946#search

Player Class 1/3
+ This class will be used to hold a player's current list of cards.
+ A player should be able to add or remove cards from their "hand" (list of Card objects).

Player Class 2/3
+ We will want the player to be able to add a single card or multiple cards to their list, so we will also explore how
  to do this in one method call.

Player Class 3/3
 + The last thing we need to think about is translating a Deck/Hand of cards with a top and bottom, to a Python list.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662948#search
Game Logic - Part One and Two
+ Creating the overall logic is often the hardest part of a project like this!
+ It is important to note, that we planned the classes around the upcomiming logic, so in a real-world situation, you
often think of both the logic and class structures simultaneously.
"""

"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662956#search
Game Logic - Part Three
+ Now it's time to check the players's cards against each other.
+ There are lots of ways this can be done!
+ We have 3 situations:
    - Player One > Player Two
    - Player One < Player Two
    - Playere One == Player Two
"""

# Game Setup
print("")
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player_one.all_cards) < 5:
                print("Player ONE unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player TWO unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

# new_deck = Deck()
# new_deck.shuffle()
# mycard = new_deck.deal_one()
# print(mycard)
# print(len(new_deck.all_cards))
#
# new_player = Player("Julien")
# print(new_player)
# new_player.add_cards(mycard)
# print(new_player.all_cards[0])
# new_player.add_cards([mycard,mycard,mycard])
# print(new_player)
# new_player.remove_one()
# print(new_player)