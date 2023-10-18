"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9407966#search
Useful Operators
"""

######################
# Range is generator #
######################
mylist = [1, 2, 3]
for num in range(0, 10, 2):  # 0 start, 10 not included stop, 2 step
    print(num)

# So we saw above that range is generator if we want a list we have to cast it in a list like this:
print(list(range(0, 10, 2)))

#############
# Enumerate #
#############
print("")
print("Enumerate:")
index_count = 0
word = 'abcde'
for letter in word:
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

    # A better way to do what is above
for item in enumerate(word):
    print(item)

# With tuple unpacking we can do:
for index, letter in enumerate(word):
    print(index, letter)

#######
# ZIP #
#######
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
print("")
print("Zip")
print(zip(mylist1, mylist2, mylist3))  # we just get the adress on zip
for item in zip(mylist1, mylist2, mylist3):
    print(item)

# To get the list it is like with range we have to cast zip in a list:
print("")
print("Cast zip in a list:")
print(list(zip(mylist1, mylist2, mylist3)))

print("")
print("The 'in' operator to check if an object is in the list")
print('x' in [1, 2, 3])
print('a' in 'a world')

print("The 'in' operator to check if a key is in the dictionary or a value is in the dictionary")
print('mykey' in {'mykey': 345})
d = {'mykey': 345}
print(345 in d.values(), 345 in d.keys())

print("")
print("min and max")
mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))

print("")
print("shuffle, randint")
from random import shuffle  # from random library that is built into python import the shuffle function

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(shuffle(mylist))  # it doesn't return anything as this is an implace function
print(mylist)  # as this is an implace function mylist has been modified

from random import randint

print(randint(0, 100))  # lower range, upper range

print("")
print("Input function")
result = input('What is your name: ')
print(f"Your name is {result}")

result = input('Favorite Number: ')
print(f"the input function always return a string: {type(result)}")  # We can see that input returns a string
print(f"We cast the result of input function in int: {int(result)}")  # or you can do it directly with the input i.e:
result = int(input('Favorite Number: '))
print(f"this time we casted the input directly int(input...) {type(result)}")
