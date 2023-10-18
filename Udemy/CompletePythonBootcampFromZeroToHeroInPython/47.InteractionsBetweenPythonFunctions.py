"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20548634#search
Interactions Between Functions
"""
from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]


# shuffle(example)  # it happens all in place, so it doesn't return anything.
# print(example)


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(example)
print(result)

mylist = [' ', 'O', ' ']
shuffle_list(mylist)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")

    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# INITIAL LIST
mylist = [' ', 'O', ' ']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS

guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list, guess)


def myfunc(name):
    print('Hello {}'.format(name))


myfunc('Julien')
