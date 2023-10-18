"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9442634#search
Function Practice Problems:
"""

# Exercice 1
print("Exerice 1")


# Lesser of two evens: Write a function that returns the lesser of two given numbers if both numbers are even, but
# returns the greater if one or both numbers are odd
# lesser_of_two_evens(2, 4) --> 2
# lesser_of_two_evens(2, 5) --> 5

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))

# Exercice 2
print("")
print("Exerice 2")


# ANIMAL CRACKERS: Write a function takes two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    text1, text2 = text.split()
    if text1[0] == text2[0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

print("")
print("Exerice 3")


# Exercice 3
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
def makes_twenty(n1, n2):
    if sum((n1, n2)) == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


# LEVEL1 PROBLEMS

# Exercice 4
# OLD MACDONALD: Write a function that capitalizes the firs and fourth letters of a name
def old_macdonald(name):
    count = 0
    result = ""
    for letter in name:
        if count == 0 or count == 3:
            result += letter.upper()
        else:
            result += letter.lower()
        count += 1
    return result


print(old_macdonald('macdonald'))

# Exercice 5
print("")
print("Exercice 5")
# MASTER YODA: Give a sentence, return a sentence with the words reversed

print("Solution 1: ")


def master_yoda(text):
    result = ""
    for letter in reversed(text.split()):
        result += letter + " "

    return result


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print("")
print("Solution 2: ")


def master_yoda2(text):
    res = text.split()
    res.reverse()
    return res


print(master_yoda2('I am home'))
print(master_yoda2('We are ready'))

# Exercice 6
print("")
print("Exercice 6")


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# LEVEL2 PROBLEMS

# Exercice 7
print("")
print("Exercice 7")


# FIND 33: Given a list of ints, return True if the array contains 3 next ot a 3 somewhere.


def has_33(nums):
    check_value = False
    for number in nums:
        if number == 3 and not check_value:
            check_value = True
        elif number == 3 and check_value:
            return True
        else:
            check_value = False
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 1, 3, 1, 3, 3, 1, 3]))

# Exercice 8
print("")
print("Exercice 8")


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters.


def paper_doll(text):
    result = ""
    for letter in text:
        result += 3 * letter
    return result


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# Exercice 9
print("")
print("Exercice 9")


# BLACKJACK: Given Three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. if their
# sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds
# 21, return 'BURST'


def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) > 21 and (a == 11 or b == 11 or c == 11):
        return sum((a, b, c)) - 10
    elif sum((a, b, c)) > 21:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

# Exercice 10
print("")
print("Exercice 10")


# SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


def summer_69(arr):
    skip_seq = False
    result = 0
    for number in arr:
        if number == 6:
            skip_seq = True

        elif number == 9:
            skip_seq = False

        elif not skip_seq:
            result += number

    return result


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# CHALLENGING PROBLEMS
# Exercice 11
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
print("")
print("Exercice 11")


def spy_game(nums):
    result = ""
    for num in nums:
        if num == 0:
            result += '0'
        if num == 7:
            result += '7'
        if result == '007':
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# Exercice 12
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
print("")
print("Exercice 12")

from math import sqrt


def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def nombres_premiers(b):
    maliste = []
    for i in range(2, b + 1):
        if is_prime(i):
            maliste.append(i)
    return len(maliste), maliste


# print(is_prime(9))
print(nombres_premiers(100))

# CHALLENGING PROBLEMS
# Exercice 12
# PRINT BIG: Write a function that takes in a single letter, and return a 5x5 representation of that letter
print("")
print("Exercice 12")


def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4:'*****', 5:'****', 6:'  * ', 7:' *  ', 8:'*  * ', 9:'*   '}
    alphabet = {'A':[1, 2, 4, 3, 3], 'B':[5, 3, 5, 3, 5], 'C':[4, 9, 9, 9, 4], 'D':[5, 3, 3, 3, 5], 'E':[4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print(print_big('a'))
print(print_big('b'))
print(print_big('c'))
print(print_big('d'))
print(print_big('e'))
