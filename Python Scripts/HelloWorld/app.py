# import shutil
# import math
# import sys

#######################
# 1 - Getting Started #
#######################
# print("Hello World !")
# print("*" * 13)

# ######################
# # 2 -Primitive Types #
# ######################
# #############
# # variables #
# #############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781593
# students_count = 1000
# rating = 4.99
# is_published = False
# course = "   python programming"

# #####################
# # Formatted Strings #
# #####################
# # https://codewithmosh.com/courses/417695/lectures/6781587
# first = "Mosh"
# last = "Hamedani"
# full = f"{len(first)} {2 + 2}"
# print(full)

# ##################
# # String Methods #
# ##################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781587
# print("Affichage et Variables")
# print(course.lower())
# print(course.upper())
# print(course.title())
# print(course.strip())
# print(course.find("pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)
# print("\n")

# ###########
# # Numbers #
# ###########
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3
# x += 3

# #############################
# # Working with Numbers #
# #############################
# import math
# print("Librairie mathematique")
# print (math.ceil(2.2))
# print("\n")

# ###################
# # Type Conversion #
# ###################
# print("Saisie et affectation dans une variable")
# x = input("x: ")
# y = int(x) + 1
# print("\n")

# print("Affichage formate")
# print(f"x: {x}, y: {y}")
# print("\n")

# falsy values:
# # ""
# # 0
# # None


####################
# 3 - Control flow #
####################
#######################
# Comparison Operator #
#######################
# https://codewithmosh.com/courses/417695/lectures/6781617

# #########################
# # conditional statement #
# #########################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781626
# print("Conditional statement")
# temperature = 15
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")
# print("\n")

# ####################
# # Ternary Operator #
# ####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781623
# print ("Ternary Operator")
# age = 22
# if age > 18:
#     message = "Eligibale"
# else:
#     message = "Not eliigible"
# print(message)

# # le code ci-dessus peut s'ecrire comme ci-dessous
# age = 12
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)
# print("\n")

# #####################
# # Logical Operators #
# #####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781619
# print("Logical Operator AND")
# high_income = False
# good_credit = True

# if high_income and good_credit:
#     print("Elligible")
# else:
#     print("Not Elligible")
# print("\n")


# # Logical Operators OR #
# print("Logical Operator OR")
# high_income = False
# good_credit = True

# if high_income or good_credit:
#     print("Elligible")
# else:
#     print("Not Elligible")
# print("\n")

# ############################
# # Short-circuit Evaluation #
# ############################
# print("Logical Operator NOT")
# high_income = False
# good_credit = True
# student = True

# if not student:
#     print("Elligible")
# else:
#     print("Not Elligible")
# print("\n")


# # Logical Operator or and not #
# print("Logical Operator or and not")
# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")
# print("\n")

# #######################
# # Chaining Comparison #
# #######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781627
# print("Chaining Comparison Operators")
# age = 22
# if age >-18 and age <65:
#     print("Eligible")
# # Those 2 methods are exactly equivalent
# # The one below is closer from mathematic notations
# if 18 <= age < 65:
#     print("Eligible")
# print("\n")
# #############
# # For loops #
# #############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781622
# print("For loop: \n")
# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")
# print("\n")

# ##############
# # For...Else #
# ##############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781624
# print("For...Else")
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")
# print("\n")

# ################
# # Nested loops #
# ################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781628
# print("Nested loops")
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# print("\n")

# ################
# # Iterables    #
# ################
# # https://codewithmosh.com/courses/417695/lectures/6781620
# print(type(5))
# range object is iterable which means you can iterates over it
# print(type(range(5)))

# Iterable
# for x in range(5):
# strings are also iterables
# for x in "Python":
#   print(x)
# for x in [1, 2, 3, 4]:
#     print(x)

# ###############
# # While loops #
# ###############
# # https://codewithmosh.com/courses/417695/lectures/6781616
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("Echo", command)

# count = 0
# for number in range(1,10):
#     if (number%2 == 0):
#         print (number)
#         count += 1

# print("\n")
# print (f"We have {count} even numbers")
# print("\n")

# ##################
# # Infinite Loops #
# ##################
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit"
#         break


# ###############
# #4 - Functions #
# ###############
# ######################
# # Defining functions #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781639
# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Julien", "Palleau")
# greet("Lucie", "Mottier")

# ############
# #Arguments #
# ############
# https://codewithmosh.com/courses/417695/lectures/6781646
# def greet(first_name, last_name): # these are parameters for the greet function
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
# greet("Julien", "PALLEAU") # these are arguments for the greet function

# !! parameter is the input you define for your function whereas argument is the actual value for a given parameter

# ######################
# # Types of Functions #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781650
# # In programming we have 2 types of functions:
# # 1 - Perform a task
# # 2 - Return a value
# def get_greeting(name):
#     print (f"Hi {name}")
#
# message = get_greeting("Julien")
# file = open("content.txt", "w") # later in the course we will see a better to open files.
# file.write(message)

# ######################
# # Keywords Arguments #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781642
# def increment(number, by):
#     return number + by
# print("The result of the increment function is : ", increment(2, by=1))

# #####################
# # Default Arguments #
# #####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781648
# def increment(number, by=2): # should be read as number will be incremented by 2 as the optional increment is 2
#     return number + by
# print("result of increment with a default argument : ", increment(2)) # here we will get 4
# print("result of increment with a provided increment value of 5 :", increment(2, 5)) # This time the result will be 7 as this time the increment = 5 indeed we can overide the default value !
# print("\n")

# #########
# # xargs #
# #########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781640
# # There are cases where you want to take a variable numbers of arguments
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print("xargs :", multiply(2, 3, 4, 5))
# print("\n")

# ##########
# # xxargs #
# ##########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781644
# # variable number of keywords arguments (key value pairs)
# def save_user(**user):
#     print(user)

# print("xxargs")
# save_user(id=1, name="John", age=22)
# print("\n")

# #########
# # Scope #
# #########
# # https://codewithmosh.com/courses/417695/lectures/6781638

# #############
# # Debugging #
# #############
# # https://codewithmosh.com/courses/417695/lectures/6781641

##########################
# # VSCode Coding Tricks #
##########################
# # https://codewithmosh.com/courses/417695/lectures/6781647

# ################################
# # Exercie Section 4: Fizz_buzz #
# ################################
# # exercice : https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781645
# # Solution : https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781649
# My solution
# def fizz_buzz(input):
#     if input % 3 == 0:
#         if input % 5 == 0:
#             return "Fizz Buzz"
#         else:
#             return "Fizz"
#     elif (input % 5) == 0:
#         return "Buzz"
#     elif (not(input % 3) == 0 and (not(input % 5) == 0)):
#         return input
# Mosh's solution
# def fizz_buzz(input):
#     if (input % 3 ==0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input %5 == 0:
#         return "Buzz"
#     return input
# print(fizz_buzz(3))


#######################
# 5 - Data Structures #
#######################
# #########
# # Lists #
# #########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781704
# letters = ["a", "b", "c"]
# matrix =[[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")
# print(numbers)
# print(chars)
# print(len(chars))

# ###################
# # Accessing Items #
# ###################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781703
# letters = ["A", "b", "c", "d"]
# print(letters[-1])
# print(letters[0:3]) # this expression and the one below are equivalent
# print(letters[:3])
# print(letters[0:]) # this expression and the one below are equivalent
# print(letters[:])
# print(letters[::2]) # it returns the values of letters with a step 2 so in this case A and c
# numbers = list(range(20))
# print(numbers[::-1])

# ##################
# # List Unpacking #
# ##################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781696
# ###### traditional way to use element of the list
# numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# ###### Python way to use element of a list it is called list unpacking
# numbers2 = [1, 2, 3]
# first2, second2, thrid2 = numbers2

# ###### What if we don't want to assign all the element of the list
# numbers3 = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4]
# first3, second3, *other3 = numbers3
# print(first3)
# print(second3)
# print(other3)

# ###### What if we care about the first element and the last one
# numbers4 = [1, 2, 3, 4, 4, 4, 4, 4, 4, 9]
# first4, *other4, last4 = numbers4
# print(first4, last4)
# print(other4)

# ######################
# # Looping over lists #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781702
# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)

# # !!! ENUMERATE !!!
# ###### if we want to get the index of each letter but the output and syntax is bit uggly
# for letter in enumerate(letters):
#     print(letter)
#     print(letter[0], letter[1])

# ###### Let's do the same as above but in umpacking the result
# for index, letter in enumerate(letters):
#     print(index, letter)

# ############################
# # Adding or Removing Items #
# ############################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781709
# letters = ["a", "b", "c"]

# ###### Add
# letters = ["a", "b", "c"]
# letters.append("d") # append item at the end of the list
# letters.insert(0, "-") # add item at the begining of the list
# print(letters)

# Remove
# letters.pop(0) # remove item at the end of the list
# letters.remove("b") # remove an item but you don't know his index
# del letters[0:3] # remove elements using a range
# letters.clear # empty the list
# print(letters)

# #################
# # Finding Items #
# #################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781691
# letters = ["a", "b", "c"]
#
# print(letters.count("d")) # return the number of occurences of this letter in the list
#
# if "d" in letters:        # Ici on verifie que l'objet soit dans la liste avant de l'afficher
#     print(letters.index("d"))

# #################
# # Sorting Lists #
# #################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781698
# numbers = [3, 51, 2, 8, 6]
# numbers2 = [3, 51, 2, 8, 6]

# numbers.sort()
# print("numbers list is sorted in ascending:", numbers)
# print("")
# numbers.sort(reverse=True) # here the list numbers is modified to be sorted in reverse order so, descending order
# print("numbers list is sorted in reverse order :", numbers) # In this case the list is not changed
# print("")
# print("Let's now see the original list", numbers)
# print("")
# print("In the two cases above the numbers list is change from the original state to ascending then to descending order")
# print("So we lost the original order")
# print("")
# print("Now let's use sorted() function rather than number.sort")
# print("Sorted list :", sorted(numbers2))
# print("In this case the original list is not changes, let's see :")
# print("Original list :", numbers2)
# print("")

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]
# items.sort
# print("Here nothing is sorted", items) # nothing is sorted because python doesn't how to sort
# print("")

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print("Now the list is sorted as we told Python what to sort with sort_item (see the code)", items)

# ####################
# # Lambda Functions #
# ####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781706
# items.sort(key=lambda item: item[1])
# print("See code, much better solution, in using lambda expression", items)

# ################
# # Map Function #
# ################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781705
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# # This is not elegant
# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)

# # A better and more elegant way to achieve the same result
# prices = list(map(lambda item: item[1], items))
# print(prices)

# ####################
# # Filter Functions #
# ####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781689
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)

# #######################
# # List Comprehensions #
# #######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781687
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# prices = list(map(lambda item: item[1], items)) # this expression and the one below are equivalent map // list comprehesions
# prices = [item[1] for item in items] # it is called list comprehensions
# print(prices)

# filtered = list(filter(lambda item: item[1] >= 10, items)) # this expression and the one below are equivalent filter //  list comprehensions
# filtered = [item for item in items if item[1] >= 10] # it is called list comprehensions
# print(filtered)

# ################
# # Zip Function #
# ################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781700
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))
# print(list(zip("abc", list1, list2))) # we can add abc directly inside the zip function

# ##########
# # Stacks #
# ##########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781699
# # A stack has a lifo (Last in - first out) or fifo (first in - first out) behaviour

# ##########
# # Queues #
# ##########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781688
# # A queue has a fifo (First in - first out) behaviour
# # A fifo model can be very inneficient with a long list for example let's say we have a list of 1001 numbers
# # then you delete the first number of the list then you need to shift the 1000 numbers on the left.
# # so in this case it is better to use deque let'see
# from collections import deque # on appel un module (plus de details sur collections module plus bas)
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")

# ##########
# # Tuples #
# ##########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781707
# point1 = 1, # ici on defini un tuple
# point2 = 1 # ici on defini un entier
# point3 = () # ici on defini un liste de tuple vide
# point4 = (1, 2) + (3, 4) # we use + to concatenate two tuples
# point5 = (1, 2) * 3 # we use * to repeat a tuple
# point6 = tuple("Hello World") # Conversion from a string into a tuple
# print(type(point1))
# print(type(point2))
# print(type(point3))
# print(point4)
# print(point5)
# print(point6)

# point = (1, 2, 3)
# print(point[0]) # index
# print(point[0:2]) # range
# x, y, z = point # unpacking
# if 10 in point:
#     print("exists")

# # The tuples are immutable !!! therefore you can't change or modify a tuple !!!
# # point[0] = 10 if you try to run this code you'll get an error: TypeError: 'tuple' object does not support item assignment

# ######################
# # Swapping Variables #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781695
# x = 10
# y = 11

# x, y = y, x # this swap values from x to y and from y to x, cool! No need of a third value like in C or other languages
# print("x", x)
# print("y", y)

# ##########
# # Arrays #
# ##########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781690
# # The array are more efficient than list for large sequence of numbers
# # However if you not deal with 10 000 numbers no need to use array and
# # prefere lists.
# from array import array

# numbers = array("i", [1, 2, 3]) # the i correspond to the type code which define the type of what you store in your array search in google python3 typecode and you'll get the list of code
# numbers.append(4) # you've got, like for list, insert, append, pop, remove, methods
# However unlike list, in an array you can only have 1 type of objects in this case integers so you can't mix integer with letters or any other type.
# numbers[0] # you can also access item by their index


# ########
# # Sets #
# ########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781697
# # Sets is basically a collection with no duplicates
# numbers = [1, 1, 2, 3, 4]
# uniques = set(numbers)
# first = set(numbers)
# second = {1, 5} # when you create a sets you use {}
# second.add(5)     # add and remove like for the lists
# second.remove(5)
# second.add(5) # I add it again for the union (|) examples below
# len(second)

# print(uniques)
# print(second)
# print(len(second))

# print(first | second) # this is an union from first and second
# print(first & second) # this is the intersection between first and second
# print(first - second) # this is the difference between 2 sets
# print(first ^ second) # symetric difference (return item which are either in first set or second set but not both)
# # set doesn't support access by indexing so print(first[0]) won't work
# if 1 in first:
#     print("yes")

# ################
# # Dictionaries #
# ################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781692
# point = {"x": 1, "y": 2} # this line and the one below are equivalent
# point = dict(x=1, y=2) # however this line is clearer as there is no "" and : so easier and faster to type
# print(point["x"])
# point["x"] = 10
# point["z"] = 20
# print(point)
# # print(point["a"]) this return an error as a doesn't exist: KeyError: 'a'
# # So to avoid this error we can check for the existance of the key like this:
# if "a" in point:
#     print(point["a"])

# # the other solution is to use the get method
# print(point.get("a", 0)) # we say if the key a doesn't exist return 0
# del point["x"]
# print(point)

# for key in point:
#     print(key, point[key])

# for key, value in point.items():
#     print(key, value)

# #############################
# # Dictionary Comprehensions #
# #############################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781693
# values = []
# for x in range(5):
#     values.append(x * 2)

# # we can use Comprehensions here which is under the form:
# # [expression for item in items]
# values1 = [x * 2 for x in range(5)] # this line of code is identical to the 3 lines above !!!
# print(values1)

# # now if we take the same expression as above and replace [] bu {} we get a set
# values2 = {x * 2 for x in range(5)}
# print(values2)

# # below is a dictionary and print the keys and their value
# values3 = {x: x * 2 for x in range(5)}
# print(values3)

# #########################
# # Generator Expressions #
# #########################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781708
# # Generator generate a value to each iteration so it is more memory efficient in case of large range for instance 1 000 000
# from sys import getsizeof

# values = (x * 2 for x in range(10000)) # here because we replaced the [] by () values is no longer a list it is now a generator object
# for x in values:
#     print(x)

# print("Generator :", getsizeof(values))

# # lets compare with a list
# values = [x * 2 for x in range (10000)]
# print ("list :", getsizeof(values))

# ######################
# # Unpacking Operator #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781701
# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers) # here we unpack the containor with *

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

# first = [1, 2]
# second = [3]
# values = [*first, "a", *second, *"Hello"]
# print(values)

# # We can do the same with a dictionary
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 1}
# print(combined)

# ######################
# # Exercise section 5 #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6781694
#
# # Attention !!! Il n'est pas possible de trier un dictionnaire il faut transformer le dictionnaire en liste
# from pprint import pprint
# sentence = "This is a common interview question"

# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# pprint(char_frequency, width=1) # With this function we have more control over printing stuff

# # how to sort a dictinary ? answer: look at the line broken in 3 just below:
# char_frequency_sorted = sorted(char_frequency.items(), # this line is broken in 3
# key=lambda kv:kv[1],
# reverse=True) # Sorted dictionnary

# print(char_frequency_sorted[0])


##################
# 6 - Exceptions #
##################
# #######################
# # Handling Exceptions #
# #######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880894
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a vailid age.")
# else:
#     print("No exceptions were thrown.")

#################################
# Handling Different Exceptions #
#################################
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except(ValueError, ZeroDivisionError):  # python will exit as soon as a condition is satisfied
#     print("You didn't enter a valid age.")
# except ZeroDivisionError:       # that condition is ignored because if true that will be executed above so this line and the one below should be removed
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")

# ###############
# # Cleaning Up #
# ###############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880892
# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a vailid age.")
# else:
#     print("No exceptions were thrown.")
# finally:           # This is finally close used to be executed even in case of exception
#     file.close()   # it is used when a file or a connection or a file is opened as you always want to close them.

# ######################
# # The With Statement #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880897
# try:
#     with open("app.py") as file: # the with will autmatically released the file at the end so no need to close it.
#         print("File opened.")

#     age = int(input("Age : "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")

# ######################
# # Raising Exceptions #
# ######################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880891
# # According to Mosh it is better to avoid raising exceptions as it is costly it is better to use
# # existing excption like above
# def calculate_xfactor(age):
#     if age <= 10:
#         raise ValueError("Age cannot be 0 or less.") # go to google and search for "python 3 built-in exceptions
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# ##############################
# # Cost of Raising Exceptions #
# ##############################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880893
# from timeit import timeit

# code1 = """
# def calculate_xfactor(age):
#     if age <= 10:
#         raise ValueError("Age cannot be 0 or less.") # go to google and search for "python 3 built-in exceptions
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     pass
# """

# code2 = """
# def calculate_xfactor(age):
#     if age <= 10:
#         return None
#     return 10 / age


# xfactor = calculate_xfactor(-1)
# if xfactor == None:
#     pass
# """
# print("First code=",timeit(code1, number=10000))
# print("Second code=",timeit(code2, number=10000))


# ###############
# # 7 - Classes #
# ###############
###########
# Classes #
###########
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880920
# class Point: # For class we use Pascal convention (every work start with a capital for instance MyPoint)
#     def draw(self):
#         print("draw")

# point = Point()
# print(type(point))
# print(isinstance(point, Point)) # this function allow you to know if the object point is an instance of class Point

####################
# Creating Classes #
####################
# https://codewithmosh.com/courses/417695/lectures/6880937
# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, int))

# ###############
# # Constructor #
# ###############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880927
# class Point:
#     def __init__(self, x, y): # self is a reference to the current object
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# point.draw()

# ################################
# # Class vs Instance Attributes #
# ################################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880932
# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
# Point.default_color = "yellow"

# point = Point(1, 2)
# print(point.default_color)
# print(Point.default_color)
# point.draw()

# another = Point(3, 4)
# print(another.default_color)
# another.draw()

#############################
# Class vs Instance Methods #
#############################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880926
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls): # cls is a convention which mean class
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point.zero()
# point.draw()

#################
# Magic Methods #
#################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880930
# # to get the list of magic methods search for python3 magic methods and go to A guide to Python's Magic Methods
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# print(str(point))

#####################
# Comparing Objects #
#####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880928
# in order to compare two objects you need to call a magic Methods/function
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

# point = Point(10, 20)
# other = Point(1, 2)
# print(point > other)

# ####################################
# # Performing Arithmetic Operations #
# ####################################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880931
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# point = Point(10, 20)
# other = Point(1, 2)
# # if we try to print Point we'll get the adress of Point as we removed __str__
# # however we can comined point and other like this:
# combined = point + other
# print(combined.x, combined.y)

# ############################
# # Making Custom Containers #
# ############################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880938
# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)

# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)

# ##################
# # Private member #
# ##################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880935
# # A private tag doesn't prevent to access it but it is bit more complex and warning is returned the class user: hey don't touch this, this is private !
# # So unlike C# or Java we don't really have the concept of private members these private members are still
# # accessible from the outside

# class TagCloud:
#     def __init__(self):
#         self.__tags = {} # self.tags = {} make the tags accessible while self.__tags make tags private therefore it is not accessible any more.

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# # print(cloud.__tags) you can't write this as now tags is private.

# # however in python you can still access a private members let's see how:
# print(cloud.__dict__)
# print(cloud._TagCloud__tags) # we've been able to access __dict__ even if it is a private variable
# # Conclusion in Python we don't really have the concept of private members these private members are still accessible from the outside !!!

# ##############
# # Properties #
# ##############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880936
# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value): # it is not pythonic (it is not exploiting full potential of python,
#                                 # let's see how achieve the same in a more pthon way.)
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     # here we are going to use properties in order to achieve the same as above
#     # price = property(get_price, set_price)

# # the method set_price and get_price are poluting the interface of our object, so we use @property and @price.setter to keep clean the interface of our object
# product = Product(-10)
# # product.price = -1   this line throw the exception ValueError defined above
# print(product.price)

# ###############
# # Inheritance #
# ###############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880925
# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")

# # We refer to
# # Animal: as Parent or as Base class
# # Normal: as Child or Sub class
# class Mammal(Animal):
#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")

# m = Mammal()
# m.eat()
# print(m.age)

# ####################
# # The Object Class #
# ####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880917

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")

# class Mammal(Animal):
#     def walk(self):
#         print("walk")

# m = Mammal()
# print(isinstance(m, Mammal)) # tell us if m is an instance of Mammal object
# print(isinstance(m, Animal)) # tell us if m is an instance of Animal and it says True as m comes from Mammal which inherit from Animal

# # In python all classes directly or indirectly derives from the object class !
# print(isinstance(m, object))
# print(issubclass(Mammal, Animal)) # tells us if Mammal is a subclass from Animal

# #####################
# # Method Overriding #
# #####################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880924

# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")

# class Mammal(Animal):
#     def __init__(self):
#         super().__init__() # appel la methode init de la class mere: Animal, Note that super could be call after self.weight = 2
#         print("Mammal Constructor")
#         self.weight = 2

#     def walk(self):
#         print("walk")

# m = Mammal()
# print(m.age)
# print(m.weight)

###########################
# Multi-level Inheritance #
###########################
# https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880934
# speech about the danger of making too much modelisation and too long hierachy with inheritance
# you should only modelise what you need to solve your problem: i.e Animal -> bird(with fly method) -> chicken which is wrong
# if the fly method is not necessary to solve a problem then it should not exist ! And if i has to exist then you need another
# bird's subclass to properly modelise the chicken !

# ########################
# # Multiple Inheritance #
# ########################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880923
# # Similar to Multi-level Inheritance, Multiple Inheritance is a source of issue and if not used properly bugs will be introduced in programs
# class Employee:
#     def greet(self):
#         print("Employee Greet")

# class Person:
#     def greet(self):
#         print("Person Greet")

# class Manager(Employee, Person):
#     pass

# # class Manager(Employee, Person):
# #     pass

# # if you comment the class Manager and uncomment the one below you'll get a different result:
# # First case you'll get: Employee Greet
# # Second case you'll get: Person Greet
# # because the first class use will have his print used but not the second one. Therefore it is
# # extremly dangerous because another coder might not see the problem so Multiple Inheritance should
# # be avoided
# # !!! However multiple inheritence is not a bad thing !!! it is bad if not used properly !!!
# # To use it properly the classes should not have things in common like in our example above
# # where they have greet method in common.
# manager = Manager()
# manager.greet()

# # let's now see a good example of multiple inheritance
# class Flyer:
#     def fly(self):
#         pass

# class Swimmer:
#     def swim(self):
#         pass

# # now we can combine the features of this two classes so we can create a flying fish that knows
# # how to fly and how to swim
# class FlyingFish(Flyer, Swimmer):
#     pass

# #################################
# # A Good Example of Inheritance #
# #################################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880921

# class InvalidOperationError(Exception):
#     pass

# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# ##########################
# # Abstract Base Classses #
# ##########################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880929
# # First issue Stream is an abstract concept therefore we should not be able to open a Stream, but
# # we should be able to open a FileStream or a NetworkStream. So we should not be able to directly create an
# # instance of Stream class.
# # Second issue if we look at the implementation of FileStream and NetworkStream classes you can see
# # both these classes have a read method this is why we hadded @abstractmethod and the 2 lines
# # below

# from abc import ABC, abstractmethod # which stands for abstract base class

# class InvalidOperationError(Exception):
#     pass

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a stream")

# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream.")

# # stream = Stream() # as Stream is an abstract class (Stream(ABC) where ABC stands for Abstract Base Class)
# stream = MemoryStream()
# stream.open()

# ################
# # Polymorphism #
# ################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880919
# from abc import ABC, abstractmethod

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")

# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")

# def draw(controls):
#     for control in controls:
#         control.draw()

# ddl = DropDownList()
# textbox = TextBox()
# draw([ddl, textbox])

# ###############
# # Duck Typing #
# ###############
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880922

# ############################
# # Extending Built-in Types #
# ############################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880933

# class Text(str):
#     def duplicate(self): # in this case self is an instance of str class
#         return self + self

# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object) # here we call the base class

# list = TrackableList()
# list.append("1")

# ################
# # Data Classes #
# ################
# # https://codewithmosh.com/courses/python-programming-course-beginners/lectures/6880918
# from collections import namedtuple

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # so to solve the issue in comparing point issue object:
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# p1 = Point(1, 2)
# p2 = Point(1, 2)
# # Python returns false as it is comparing memory address from p1 and p2 which are obviously (you have to remove def __eq__ for this result)
# print(id(p1)) # look at p1 address
# print(id(p2)) # look at p2 address
# # the two address are different !

# # now with def __eq__ the problem is solved and we can tess the equality of the two instance of class point
# print(p1 == p2)

# Point = namedtuple("Point", ["x", "y"])
# p1 = Point(x=1, y=2)
# p2 = Point(x=1, y=2)
# print(p1 == p2)
# # Do not forget that you can't change value of tuple so P1 can't be changed, if need to then you have to recreate a P1 point with different value like this:
# p1 = Point(x=10, y=20)
# print(p1)
# print(p1 == p2)


###############
# 8 - Modules #
###############
# ####################
# # Creating Modules #
# ####################
# # https://codewithmosh.com/courses/417695/lectures/8417531
# # Two ways to import functions from sales.py file
# # What approach you choose is purely your personal preference there is no right or wrong choice
# # import specific object from sales module
# from sales import calc_shipping, calc_tax
# calc_shipping()
# calc_tax()

# import sales # import the entire module as an object
# sales.calc_shipping()

#########################
# Compiled Python files #
#########################
# https://codewithmosh.com/courses/417695/lectures/8417533

######################
# Module search Path #
######################
# https://codewithmosh.com/courses/417695/lectures/8417536
# import ecommerce.sales
# import sys
# ecommerce.sales.calc_tax() # that is a bit tidious to have to write ecommerce.sales each time

# from ecommerce.sales import calc_tax # so this is one way but if there are too many
# calc_tax() # so it is much more shorter with this way to import a module

# print(sys.path)

# ############
# # Packages #
# ############
# https://codewithmosh.com/courses/417695/lectures/8417532
# here we need to specify ecommerce which is the directory containing sales.py
# from ecommerce.sales import calc_tax, calc_shipping # however this can quickly become noisy so let's have another approach
# ecommerce.sales.calc_tax    # however it is tedious
# # so there is a better way like this:
# from ecommerce.sales import sales # like this you can access all the members of this module !
# sales.calc_tax  # this is much better
# sales.calc_shipping

################
# Sub-Packages #
################
# https://codewithmosh.com/courses/417695/lectures/8417537
# from ecommerce.shopping import sales

#############################
# Intra-packages References #
#############################
# https://codewithmosh.com/courses/417695/lectures/8417534


# ####################
# # The dir function #
# ####################
# # https://codewithmosh.com/courses/417695/lectures/8417530
# from ecommerce.shopping import sales

# # print(dir(sales)) # we get all the atributes and methods define in an object
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)

################################
# Executing Modules as Scripts #
################################
# https://codewithmosh.com/courses/417695/lectures/8417535
# from ecommerce.shopping import sales


###############################
# 9 - Python Standard Library #
###############################
###########################
# Python standard library #
###########################
# https://codewithmosh.com/courses/417695/lectures/8417577

# ######################
# # Working with Paths #
# ######################
# # https://codewithmosh.com/courses/417695/lectures/8417574
# from pathlib import Path

# #Path(r"C:\Program Files\Microsoft") # with r option no needs to write \\ and you can directly write \
# path = Path(r"HELLOWORLD\ecommerce\__init__.py")  # this is a relative path
# Path.home()
# print(path)
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)  # returns only the filename in this path
# print(path.stem)  # returns the filename without the extension
# print(path.suffix)  # returns only the extension
# print(path.parent)  # the parent folder of this path
# # here se change the file name at the end of the path so replace __init__.py by file.txt
# path = path.with_name("file.txt")
# print(path)
# print(path.absolute())
# with suffix allow to change the extension of a file
# path = path.with_suffix(".txt")
# print(path)

# ############################
# # Working with Directories #
# ############################
# # https://codewithmosh.com/courses/417695/lectures/8417581
# from pathlib import Path
# path = Path("ecommerce")

# print(path.exists())
# # path.mkdir()
# # path.rmdir()
# # path.rename("ecommerce2")

# we can use an iterator object:
# for p in path.iterdir():    # This is important this is a generator object
#     print(p)

# # we can use a list comprehension
# paths = [p for p in path.iterdir()]
# print("Le path est:", paths)

# # let's say now we only want the directories, however this method is not looking for a pattern or recursively
# paths = [p for p in path.iterdir() if p.is_dir()]
# print("Le path avec que les directories est:", paths)

# # let's see another way to look for which allow RECURSIVE and pattern finding
# py_files = [p for p in path.glob("*.py")]  # look for a pattern
# print("Tous les py_files : ", py_files)

# py_files = [p for p in path.glob("**/*.py")]  # look for recursilvely
# py_files2 = [p for p in path.rglob("*.py")]  # other way to do the same.
# print("\n")
# print("Recursively tous les py_files : ", py_files)
# print("\n")
# print("Seconde recursive methode pour tous les py_files : ", py_files)

# ######################
# # Working with Files #
# ######################
# # https://codewithmosh.com/courses/417695/lectures/8417578
# from pathlib import Path
# from time import ctime
# import shutil

# path = Path("ecommerce/__init__.py")
# # path.exists()
# # path.rename("init.txt")
# # path.unlink()
# print(ctime(path.stat().st_ctime))

# print(path.read_text()) # This is just shorter and easier than using: with open("__init__.py", "r") as file:
# path.write_text("...")
# path.write_bytes()

# # However to copy a file this path is not the best way to proceed let's have a look
# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"


# # so the path object is a little bit tedious let's see another way to achieve the same
# target.write_text(source.read_text())
# # this approach below is easier and cleaner than using a path object
# shutil.copy(source, target)

# ##########################
# # Working with Zip Files #
# ##########################
# https://codewithmosh.com/courses/417695/lectures/8417584
# from pathlib import Path
# from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     zip.getinfo("ecommerce/__init__.py")
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")

# ##########################
# # Working with CSV files #
# ##########################
# # https://codewithmosh.com/courses/417695/lectures/8417580
# import csv  # (Comma Separeted Value)

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

# with open("FILM-VU.csv") as file:
#     reader = csv.reader(file, delimiter=';')
#     # print(list(reader))
#     for row in reader:
#         print(row[0] + " " + row[1])

# #####################
# # Working with JSON #
# #####################
# # https://codewithmosh.com/courses/417695/lectures/8417589
# import json  # (Java Script Object Notation)
# from pathlib import Path

# movies = [{"id": 1, "title": "Terminator", "Year": 1989},
#           {"id": 2, "title": "Kindergarten Cop", "year": 1993}
#           ]
# # Writting data into a json file
# data = json.dumps(movies)
# Path("movies.json").write_text(data)

# # Reading data from a json file
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies[0]["title"])

# ##################################
# # Working with a SQLite Database #
# ##################################
# # https://codewithmosh.com/courses/417695/lectures/8417579
# import sqlite3
# import json
# from pathlib import Path

# # movies = json.loads(Path("movies.json").read_text()) # read file to inject in DB

# # Connexion to DB to insert data read in the file above
# # with sqlite3.connect("db.sqlite3") as conn:
# #     command = "INSERT INTO Movies VALUES(?, ?, ?)"
# #     for movie in movies:
# #         conn.execute(command, tuple(movie.values()))
# #     conn.commit

# # Connexion to DB to read the DB's content
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)

#     # another equivalent solution
#     movies = cursor.fetchall()
#     print(movies)

# ###########################
# # Working with Timestamps #
# ###########################
# # https://codewithmosh.com/courses/417695/lectures/8417590
# import time
# print(time.time())

# def send_emails():
#     for i in range(10000):
#         pass

# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)

# ##########################
# # Working with DateTimes #
# ##########################
# # https://codewithmosh.com/courses/417695/lectures/8417587
# from datetime import datetime
# import time

# dt1 = datetime(2018, 1, 1)
# dt2 = datetime.now()
# # we convert a string in datetime object, find more details in looking for pthon 3 stptime in google
# dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
# dt = datetime.fromtimestamp(time.time())

# print(dt)
# print(f"{dt.year}/{dt.month}")
# print(dt.strftime("%Y/%m")) # Here we convert a datetime object in a string

# print(dt2 > dt1)

# ############################
# # Working with Time Deltas #
# ############################
# # https://codewithmosh.com/courses/417695/lectures/8417576
# from datetime import datetime, timedelta

# dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1)
# dt2 = datetime.now()

# duration = dt2 - dt1
# print(duration)
# print("days", duration.days)
# print("seconds", duration.seconds)
# print("total_seconds", duration.total_seconds())

# ############################
# # Generating Random Values #
# ############################
# # https://codewithmosh.com/courses/417695/lectures/8417586
# import random
# import string

# print(random.random()) # take a random floating between 0 - 1
# print(random.randint(1, 10)) # take a random int between 1-10
# print(random.choice([1, 2, 3, 4])) # take a random int between 1, 2, 3, 4
# print(random.choices([1, 2, 3, 4], k=2)) # take 2 random int between 1, 2, 3, 4
# print(random.choices("abcdefghijklmnopqrstuvwxyz", k=4)) # # take 4 random letters in the alphabet and print them
# print("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=4))) # take 4 random letters in the alphabet and print them outside of an array, note that we need to provide the
#                                                                   # alphabet which is tedious let's be more clever with string module
# print("".join(random.choices(string.ascii_lowercase, k=4)))         # much better as we don't have to provide the alphabet !!!
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))         # here we provide alphabet lower and upper case + digits 0-9

# numbers = [1, 2, 3, 4]
# random.shuffle(numbers)
# print(numbers)

# #######################
# # Opening the browser #
# #######################
# # https://codewithmosh.com/courses/417695/lectures/8417582
# import webbrowser

# print("Deployment completed")
# webbrowser.open("http://google.com")

# ##################
# # Sending Emails #
# ##################
# https://codewithmosh.com/courses/417695/lectures/8417583
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# import smtplib

# message = MIMEMultipart()
# message["from"] = "PALLEAU Julien"
# message["to"] = "ptitsawyer@gmail.com"
# message["subject"] = "Hello !!"
# message.attach(MIMEText("Ce message à été envoyé depuis un programme python ! et avec une piece jointe !!"))
# message.attach(MIMEImage(Path("python.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("jpalleau@gmail.com", "xxud etmd yiyt jzis")
#     smtp.send_message(message)
#     print("Sent...")

# #############
# # Templates #
# #############
# # https://codewithmosh.com/courses/417695/lectures/8417575
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib


# template = Template(Path("template.html").read_text())

# message = MIMEMultipart()
# message["from"] = "PALLEAU Julien"
# message["to"] = "jpalleau@gmail.com"
# message["subject"] = "Hello !!"
# body = template.substitute({"name" : "Julien"})
# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("python.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("jpalleau@gmail.com", "xxud etmd yiyt jzis")
#     smtp.send_message(message)
#     print("Sent...")

# ##########################
# # Command-line Arguments #
# ##########################
# # https://codewithmosh.com/courses/417695/lectures/8417585
# import sys
# print("Hello !")

# if len(sys.argv) == 1:
#     print("USAGE: python3 app.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password", password)

# print("Bye !")

# #############################
# # Running External Programs #
# #############################
# # https://codewithmosh.com/courses/417695/lectures/8417588
# import subprocess

# result = subprocess.run(["explorer"])
# completed = subprocess.run([r"C:\Users\MOTTIER LUCIE\AppData\Local\Programs\Python\Python37-32\python.exe",
#                             r"C:\Users\MOTTIER LUCIE\Documents\Python Scripts\HELLOWORLD\other.py"],
#                             shell = True,
#                             capture_output = True,
#                             text = True)

# print("args", completed.args)
# print("returncode", completed.returncode)
# print("stderr", completed.stderr)
# print("stdout", completed.stdout)


#############################
# 10 - Python package index #
#############################
########
# Pypi #
########
# https://codewithmosh.com/courses/417695/lectures/8417619
# everything is available @ https://pypi.org

# #######
# # Pip #
# #######
# # https://codewithmosh.com/courses/417695/lectures/8417624
# import requests

# response = requests.get("http://google.com")
# print(response)

########################
# Virtual Environments #
########################
# https://codewithmosh.com/courses/417695/lectures/8417616

##########
# Pipenv #
##########
# https://codewithmosh.com/courses/417695/lectures/8417617

##################################
# Virtual Environments in VSCode #
##################################
# https://codewithmosh.com/courses/417695/lectures/8417615

###########
# Pipfile #
###########
# https://codewithmosh.com/courses/417695/lectures/8417621

#########################
# Managing Dependencies #
#########################
# https://codewithmosh.com/courses/417695/lectures/8417623

#######################
# Publishing Packages #
#######################
# https://codewithmosh.com/courses/417695/lectures/8417622

#############
# Docstring #
#############
# https://codewithmosh.com/courses/417695/lectures/8417620

#########
# Pydoc #
#########
# https://codewithmosh.com/courses/417695/lectures/8417618


###############################
# 11- Popular Python Packages #
###############################
################
# Introduction #
################
# https://codewithmosh.com/courses/417695/lectures/8481668

#################
# What are APIs #
#################
# https://codewithmosh.com/courses/417695/lectures/8481671

############
# Yelp API #
############
# https://codewithmosh.com/courses/417695/lectures/8417618

############################
# Searching for Businesses #
############################
# https://codewithmosh.com/courses/417695/lectures/8481665
# open the directory PyYelp and watch the course above

#########################
# Sending Text Messages #
#########################
# https://codewithmosh.com/courses/417695/lectures/8481674

################
# Web Scraping #
################
# https://codewithmosh.com/courses/417695/lectures/8481670

######################
# Browser Automation #
######################
# https://codewithmosh.com/courses/417695/lectures/8481670


##################
# GUY with PyQt5 #
##################
# https://www.youtube.com/watch?v=nnHnlivK1Rg
# import time
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# if __name__ == '__main__':

#     app = QApplication(sys.argv)

#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Simple')
#     w.show()

#     sys.exit(app.exec_())
