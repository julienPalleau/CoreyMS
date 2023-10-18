"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20385935#search
Methods and Functions Homework
"""
# exercice 1
# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as: 4/3*pi*r**3
print("exercice 1: ")
from math import pi


def vol(rayon):
    return (4 / 3) * pi * rayon ** 3


print(vol(2))

# execice 2
# Write a function that checks whether a number is in a given range (inclusive of high and low)
print("")
print("exercice 2: ")


def ran_check(num, low, high):
    if num in range(low, high + 1):
        return True
    else:
        return False


print(ran_check(5, 2, 7))
print(ran_check(3, 1, 10))
print(ran_check(4, 5, 10))

# exercice 3
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
print("")
print("exercice 3: ")


def up_low(s):
    upper_list = 0
    lower_list = 0
    for letter in s:
        if letter.isupper():
            upper_list += 1
        elif letter.islower():
            lower_list += 1
    return upper_list, lower_list


print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

# exercice 4
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
print("")
print("exercice 4: ")


def unique_list(lst):
    return set(lst)


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

# exercice 5
# Write a Python function to multiply all the numbers in a list.
print("")
print("exercice 5: ")


def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result


print(multiply([1, 2, 3, -4]))

# exercice 6
# Write a Python function that checks whether a word or phrase is palindrome or not.
"""Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, 
or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing 
with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing 
notation."""
print("")
print("exercice 6: ")


def palindrome(s):
    result = True
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[-i - 1]:
            result = False
    return result


print(palindrome('helleh'))

# HARD
# exercice 7
"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons
"""
print("")
print("exercice 7: ")
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if letter in str1:
            alphabet = alphabet.replace(letter, "")

    if len(alphabet) == 0:
        return True
    else:
        return False


print(ispangram("The quick brown fox jumps over the lazy dog"))
