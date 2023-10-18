print("Exercice 1")
# Exercice1
"""
Use for, .split(), and if to create a Statement that will print out words that start with 's':
"""
st = 'Print only the words that start with s in this sentence'
print(st.split())
for word in st.split():
    if word.startswith('s'):
        print(word)

print("\nExercice 2")
# Exercice2
"""
Use range() to print all the even numbers from 0 to 10.
"""
result = [res for res in range(0, 11) if res % 2 == 0]
print(result)

# Solution fourni
print(list(range(0, 11, 2)))

print("\nExercice 3")
# Exercice 3
"""
Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
"""
result = [res for res in range(1, 51) if res % 3 == 0]
print(result)

print("Exercice 4")
# Exercice 4
"""
Go through the string below and if the length of a word is even print "even!"
"""
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(f'"{word}" is even')

# Exercice 5
print("\nExercice 5")
"""
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Exercice 6
print("\nExercice 6")
"""
Use List Comprehension to create a list of the first letters of every word in the string below:
"""
st = 'Create a list of the first letters of every word in this string'
result = [word[0] for word in st.split()]
print(result)

# Documentation in python:
mylist=[]
help(mylist.insert)

# Documentation is also available @:
# https://docs.python.org/

mylist.insert(3, 'c')
mylist.insert(0, 'a')
mylist.insert(1, 'b')
print(mylist)