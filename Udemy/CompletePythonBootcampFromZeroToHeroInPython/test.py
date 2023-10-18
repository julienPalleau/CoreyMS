"""
Section 8
Object Oriented Programming
"""
# import math
#
#
# class Line:
#
#     def __init__(self, coor1, coor2):
#         self.cord1x, self.cord1y = coor1
#         self.cord2x, self.cord2y = coor2
#
#     def distance(self):
#         return math.sqrt((self.cord2x - self.cord1x) ** 2 + (self.cord2y - self.cord1y) ** 2)
#
#     def slope(self):
#         return (self.cord2y - self.cord1y) / (self.cord2x - self.cord1x)
#
#
# coordinate1 = (3, 2)
# coordinate2 = (8, 10)
#
# li = Line(coordinate1, coordinate2)
# print(li.distance())
#
# print(li.slope())
#
#
# class Cylinder:
#
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         return math.pi * self.radius ** 2 * self.height
#
#     def surface_area(self):
#         return 2 * math.pi * self.radius ** 2 + 2 * math.pi * self.radius * self.height
#
#
# c = Cylinder(2, 3)
# print(c.volume())
# print(c.surface_area())
#
#
# class Account:
#     def __init__(self, owner: str, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, dep_amt: int):
#         print('Deposit Accepted')
#         self.balance += dep_amt
#         print(f"Added {dep_amt} to the balance")
#
#     def withdrawal(self, wd_amt: int):
#         if self.balance - wd_amt >= 0:
#             print("Withdrawal Accepted")
#             self.balance -= wd_amt
#         else:
#             print("Sorry not enough funds!")
#
#     def __str__(self):
#         return f"Owner: {self.owner} \nBalance:{self.balance}"
#
#
# # 1. Instantiate the class
# print(2*"\n")
# acct1 = Account('Sam', 500)
# print(acct1.balance)
# print(acct1.owner)
# print("\n")
# print(acct1)
# acct1.deposit(100)
# print(acct1)
# acct1.withdrawal(600)
# print(acct1)
# acct1.withdrawal(1)
# print(acct1)


"""
Section 10
82.Errors and Exception Handling
"""

"""
Problem 1
"""
# for i in ['a', 'b', 'c']:
#     try:
#         print(i ** 2)
#     except:
#         print("the power of 2 is only available on a number")
#
# """
# Problem 2
# Handle the exception thrown by the code below using try and except blocks. Then use finally block to print 'All Done'
# """
# try:
#     x = 5
#     y = 0
#     z = x / y
# except ZeroDivisionError:
#     print("Attention un nombre n'est pas divisible par 0")
# finally:
#     print('All Done')
#
# """
# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with try, except, else block
# to account for incorrect inputs.
# """
#
#
# def ask():
#     while True:
#         try:
#             number = int(input("Inuput an integer: "))
#         except:
#             print("An error occurred! Please try again!")
#             continue
#         else:
#             break
#     print(f"Thank you, your number squared is: {number ** 2}")
#
# ask()

"""
86.Introduction to Milestone Project 2 Section Warmup
"""
"""
87.Card Class
"""

# CARD
# SUIT, RANK, VALUE
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Create a new Deck
print("Creation of a new Deck")
new_deck = Deck()
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
print(first_card)
print(last_card)

# Shuffle the Deck
print("\nAfter we shuffle the Deck")
new_deck.shuffle()
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
print(first_card)
print(last_card)

# Print lenght deck
print(f"Lenght of deck \n{len(new_deck.all_cards)}")

# Deal on card
print("\nDeal one card")
mycard = new_deck.deal_one()
print(mycard)

# Print lenght deck aftere a card has been dealt
print(f"Lenght of deck after a card has been dealt \n{len(new_deck.all_cards)}")

# two_hearts = Card("Hearts", "Two")
# print(two_hearts)
# print(two_hearts.suit)
# print(two_hearts.rank)
# print(two_hearts.value)
# three_of_clubs = Card("Clubs", "Three")
# print(three_of_clubs)
# print(three_of_clubs.rank)
# print(three_of_clubs.suit)
# print(three_of_clubs.value)
