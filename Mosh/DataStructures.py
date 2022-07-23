#############################
# DRY Don't Repeat Yourself #
#############################

print("list accessing:")
########################
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters)
print(letters[0:3])
print(letters[0:])
print(letters[:])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

print("\n list unpacking:")
###########################
# List unpacking
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)

numbers = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, third, *other = numbers
print(other)

print("\n looping over list:")
##############################
# looping over lists
letters=["a", "b", "c", "d"]
for index, letter in enumerate(letters):
    print(index, letter)

letters.insert(0,"-")
print(letters)

del letters[0:3]
print(letters)

letters.pop()
print(letters)

Characters = ["alivin et les chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat pote", "kirikou", "Babar"]

if "Babar" in Characters:
    print(Characters.index("Babar"))

print(Characters.count("Babar"))

numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(sorted(numbers))
print(numbers)

print("\nsorting lists")
########################
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort(key=lambda items: items[1])
print(items)

prices = []
for item in items:
    prices.append(item[1])

print(prices)


print("\nMap function")
#######################
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
prices = list (map(lambda item: item[1], items))
print(prices)


print("\nFilter function")
##########################
filtered = list(filter(lambda item: item[1]>=10, items))
print(filtered)


print("\nList comprehension")
#############################
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
prices = [item[1] for item in items]
print(prices)

# Let's re-write what we have on line 82 with list comprehension
filter = [item for item in items if item[1] >= 10]
print(filter)

print("stacks") # Last In First Out
###############
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.pop() # to remove the item on top of the stack
browsing_session[-1] # to get the item on top of the stack

print("\nqueues") # First In Last Out
#################
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
print(browsing_session) # 3 has been removed

print("\nTuples")
#################
point1 = (1, 2, 3)
point2 = (1, 2) + (3, 4)
point3 = (1, 2) * 3
point4 = tuple([1, 2]) # transform a list in tuple
print(point1[0]) # we can use index
print(point2[0:2]) # we can get a range of items
x, y, z = point1 # upacking tuples
if 4 in point2: # le mot clef in est disponible avec les tuples comme avec les lists
    print("exists")

print("\nSet")
##############
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4}
second.add(5)
print(second)
second.remove(5)
len(second)
print(second)

first = set(numbers)
second = {1, 5}
print(first | second) # union of first and second
print(first & second) # intersection of first and second
print(first - second) # soustraction de deux ensembles
print(first ^ second) # symetric difference (everything which is not in both set)

print("\nDictionaries")
#######################
values = {x * 2 for x in range(5)}
print(values)

print("\nGenerator object")
###########################
from sys import getsizeof

values = (x * 2 for x in range(100000))
#print(len(values))

print("\nUnpacking")
####################
values = list(range(5))
print(values)

values = [*range(5), *"hello"]
print(values)

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)

print("\nExercise")
sentence = "This is a common interview question"
resultat = {}

# comptage des mots
resultat = {word:sentence.count(word) for word in sentence.split(" ")}
print(sorted(resultat.items(), key=lambda r: r[1], reverse=True))

# correction
from pprint import pprint
sentence = "This is a common interview"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True))

print("\n Exceptions")
######################
try:
    with open("DataStructures.py") as file:
        print("File opened.")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
print("Execution continues")

print("\n The with statement")


print("\n Raising Exceptions")
def calculate_xfactor(age):
    if age <=0:
        raise ValueError("Age cannot be 0 or less.") # go to google and look for python3 built-in exception
    return 10 / age                                  # raising its own exception is costly

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)