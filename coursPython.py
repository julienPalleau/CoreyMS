# Working with Textual Data
# https://www.youtube.com/watch?v=k9TUPpGqYTo
'''
1 - Working with strings
2 - Working with numeric Data
3 - Comparisons
4 - Lists, Tuples, and Sets
5 - Dictionaries - Working with Key-Value Pairs
6 - Conditionals and Boolean - If, Else and Elif Statements
7 - Loops and Iterations - For / While Loops
8 - Functions
9 - Import Modules and Exploring The Standard Library
10 - OS Module - Use Underlying Operating System Functionality
11 - File Objects - Reading and Writing Files
12 - How to Set the Path Witch Between Different Versions/Executables
13 - Variable Scope - Understanding the LEGB rule and global/nonlocal statements
14 - VENV - How to Use Virtual Environmnets with the Built-In venv Module
15 - Common Python Mistakes and How to Fix Them
16 - How to work with Dates, Times, Timdeltas, and Timezones
17 - Calculate Number of Days, Weeks, or Months to Reach Specific Goals
18 - Slicing Lists and Strings
19 - Comprehension - How tey work and why you should be using them
20 - Sorting Lists, Tuples, and Objects
21 - Try/Except Blocks for Error Handling
22 - Iterators & Iterables
23 - Iterator Functions for Efficient Looping
24 - Python OOP - Class and Instances - 1
25 - Python OOP - Class Variables - 2
26 - Python OOP - classmethods and staticmethods - 3
27 - Python OOP - Inheritance creating a subclass - 4
28 - Python OOP - Special(Magig/Dunder) Methods
29 - Generate Random Numbers and Data Using the random Module
30 - Python OOP - Property Decorators - Getters, Setters, and Deleters - 6
31 - Module CSV - Comment lire, analyser et ecrire des fichiers csv
32 - Python Tips and Tricks For Writting Better Code
33 - Else Clauses on Loops
34 - Env var windows
35 - Automate Parsing and Renaming of Multiple Files
36 - First Class Functions
37 - Closure
'''

print('###############################################################')
print(f'1 - Working with strings                                     #')
print('###############################################################')
# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2

message = 'Hello World'
print(f'1-1 - longueur de la chaine "{message}" avec len(message): {len(message)}')

print(f'1-2 - affichons les 5 premiers caracteres avec message[0:5], 0 inclu, 5 exclu: {message[0:5]}')
print(f'1-3 - affichons la meme chose que ci-dssus mais avec la syntax suivante: message[:5]:\n'
      f'qui signifie du debut de la chaine au 4eme caratere: {message[:5]}')
print(f"1-4 - affichons maintenant du 6eme caractere jusqu'a la fin de la string avec la syntax suivante:"
      f"message[6:] {message[6:]}")

print(f"1-5 - affichons en minuscule {message.lower()}")
print(f"1-6 - affichons en majuscule {message.upper()}")

print(f"1-7 - Combien de hello dans le message '{message}' avec message.count('Hello'): {message.count('Hello')}")
print(f"1-8 - Combien de l dans le message '{message}' avec message.count('l'): {message.count('l')}")

print(f"1-9 - Recherche du mot 'world' dans '{message}' avec message.find('World') et cela"
      f"renvoie la position de la premiere lettre du mot recherche {message.find('World')}")

message = message.replace('World', 'World')
print(f"1-10 - replace the word 'World' by 'Universe' in '{message}' with message.replace('World', 'Universe') "
      f"{message.replace('World', 'Universe')}")

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'
print(f"1-11 - concatenation de chaine avec l'operateur '+' {'Hello' + ' ' + 'Michael'}")
print(f"1-12 - concatenation mais en utilisant les variables greeting: {greeting} et name: {name}: {message}")

print("1-13 - In order to see the syntax for old print syntax and formated string you need to have a look to the code:")
message = ' + old print syntax {}, {}. Welcome!'.format(greeting, name)
print(message)
message = f' + formated string {greeting}, {name.upper()}. Welcome!'
print(message)

print(f'1-14 Build the set if built-in functions for the object name with dir(name) {dir(name)}')
print(f'1-15 Print the help for dict with help(dict: {help(dict)}')

print('###############################################################')
print(f'2 - Working with numeric Data                                #')
print('###############################################################')
# https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3
print('''
Arithmetic Operators:
Additions: 3 + 2
Subtraction: 3 - 2
Multiplication: 3 * 2
Division: 3 / 2
Floor Division: 3 // 2
Exponent: 3 ** 2
Modulus: 3 % 2
''')

num = 3
print(f'2-1 Print the variable type with type(num): {type(num)}')

print(f"2-2 3 a la puissance 2 s'ecrit 3**2 et est egal a {3 ** 2}")

print(f"2-3 2 modulo 2 est egal a: {2 % 2}")
print(f"2-4 - 3 modulo 2 est egal a: {3 % 2}")
print(f"2-5 - 4 modulo 2 est egal a: {4 % 2}")
print(f"2-6 - 5 modulo 2 est egal a: {5 % 2}")

num = 1
print(f"2-7 - lets set the variable num to 1 with num = {num}")
num = num + 1
print(f"2-8 - the first way to increment a variable num=num+1 equal {num}")
num += 1
print(f"2-9 - the second way to increment a variable num+=1 equal {num}")

print(f"2-10 - valeur absolue de -3 s'ecrit abs(-3)) et vaut: {abs(-3)}")
print(f"2-11 - arrondi de 3.75 s'ecrit round(3.75) et vaut: {round(3.75)}")
print(f"2-12 - arrondi de 3.75 a 1 digit apres la virgule, s'ecrit round(3.75,1) et vaut: {round(3.75, 1)}\n")

print('###############################################################')
print(f"3 - Comparisons                                              #")
print('###############################################################')
print('''Equal: 3==2
Not Equal: 3 != 2
Greater Than: 3 > 2
Less Than: 3 < 2
Greater or Equal: 3 >= 2
Less or Equal: 3 <= 2
''')

num_1 = 3
num_2 = 2
print(f'num_1 = {num_1}, num_2 = {num_2}')
print(f'num_1 == num_2: {num_1 == num_2}')
print(f'num_1 != num_2: {num_1 != num_2}')
print(f'num_1 > num_2: {num_1 > num_2}')
print(f'num_1 < num_2: {num_1 < num_2}')
print(f'num_1 >= num_2: {num_1 >= num_2}')
print(f'num_1 <= num_2: {num_1 <= num_2}')

num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)
print(f'{num_1 + num_2}\n')

print('\n#############################################################')
print(f'4 - Lists, Tuples, and Sets                                  #')
print('###############################################################')
# https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=4
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(f'4-1 longueur de la liste courses ou nb elements dans la liste courses: {len(courses)}')
print(f'4-2 premier element de la liste courses: courses[0]: {courses[0]}')
print(f'4-3 dernier element de la liste courses: courses[-1]: {courses[-1]}')
print(f'4-4 The first index is inclusif the second index is not:{courses}\n courses[0:2] : '
      f'{courses[0:2]}')  # "The first index is inclusif the second index is not"

print(f'4-5 The following courses[:2] gives us the same result as before :{courses[:2]}')

print(f'4-6 Now lets have a look at the last 2: {courses[2:]}')

# Add a value at the end of the list
print('4-7 Add a value at the end of the list')
courses.append('Art')
print(f"4-7-1 Let's append Art to the list courses as follow courses.append('Art') {courses}")

# Add a value to a specific position within the list
print('Add a value to a specific position within the list')
courses.insert(0, 'Literature')
print(f"4-7-2 Let's insert Literature in first position in the list courses as follow "
      f"courses.insert(0, 'Literature') {courses}")

# Add multiple values to a list
courses_2 = ['Art', 'Education', 'Literature']
courses.insert(0, courses_2)
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.extend(courses_2)
print(f'4-7-3 If we add courses2 to our list and that courses2 is a list we get a list of list: {courses}')
print(f'4-7-4 To add multiple values to a list you must use extend: courses.extend(courses_2): {courses}')

# Remove values from our list
courses.remove('Math')
print(f"4-7-5 Remove a value from our list with courses.remove('Math') {courses}")

# Remove the las value of our list, in addition with pop, it returns the value it removes.
popped = courses.pop()
print(
    f"4-7-6 Remove the last value of our list with courses.pop(): {courses}\n in addition it returns the value it removes "
    f"with popped = courses.pop(): "
    f"{popped}")

# Sort list
print(f'\n4-7-7 # How can we sort a list.')
courses = ["History", "Math", "Physics", "CompSci"]
nums = [1, 5, 2, 4, 3]
courses.sort()
nums.sort()
print(f"4-7-8 Let's sort our courses list with courses.sort(): {courses}")
print(f"4-7-9 Let's sort our num list with num.sort(): {nums}")

print(f'\n4-7-10 # How can we sort a list in reverse order')
courses.sort(reverse=True)
nums.sort(reverse=True)
print(f'4-7-11 same list courses as above but in reverse order with course.sort(reverse=True) {courses}')
print(f'4-7-12 same numbs courses as above but in reverse order with nums.sort(reverse=True) {nums}')

# Sorted function
courses = ["History", "Math", "Physics", "CompSci"]
nums = [1, 5, 2, 4, 3]

# With sorted we do not alter the original list while with sort the alteration is made in place.
sorted_courses = sorted(courses)
print(f"\n4-7-13 - Here we use sorted which doesn't alter the original list as a consequence"
      f"you have to assign the result to a variable like this  sorted_courses = sorted(courses) {sorted_courses}")

# sum min and max
print('\n4-7-14 - How to sum a list, get the min and the max')
courses = ["History", "Math", "Physics", "CompSci"]
nums = [1, 5, 2, 4, 3]

print(f"4-7-14-1 - nums' sum with sum(nums) {sum(nums)}")
print(f"4-7-14-2 - min of the list with min(nums): {min(nums)}")
print(f"4-7-14-3 - max of the list with max(nums) {max(nums)}")

# Finding Value
print('\n4-7-15 - How to find a value, you have to look at the code')
courses = ['History', 'Math', 'Physics', 'CompSci']

# below we make the index start at 1 instead of 0
for index, course in enumerate(courses, start=1):
    print(index, course)

# Let's imagine that we want to turn our list in a string of , separated values
# or - separated values
print('\n4-7-15 - Joining values')
course_str = ', '.join(courses)
print(f"4-7-15-1 - Let's turn our list in a string of , separated values: {course_str}")
course_str = ' - '.join(courses)
print(f"4-7-15-2 - Let's turn our list in a string of - separated values: {course_str}")
print(f"4-7-15-3 - We get just a long string {course_str} de type: {type(course_str)} ")

# Let's split our string
print(f'\n4-7-16 - Splitting values')
new_list = course_str.split(' - ')
print(f'4-7-16-1 We are now back to our original list {new_list}')

# Tuples

# Tuples
print(f'\n4-8 - Tuples')

## Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)

## Immutable
list_1 = ('History', 'Math', 'Physics', 'CompSci')
list_2 = list_1
print(list_1)
print(list_2)

print("Since tuples are immutable it is not possible to run lis_1[0]='Art', if you do so you'll get an error")
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)

## Sets
print("\n4-9 - Sets")
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(f"4-9-1 Sets, remove duplicate here we initialise cs_courses like this: cs_courses = \n"
      f"\t{{'History', 'Math', 'Physics', 'CompSci', 'Math'}} and look at what we get {cs_courses}")

# search within a sets
print(f"4-9-2 search within sets "
      f"Sets is optimized to look for an element in a sets 'Math in cs_courses : {'Math' in cs_courses}")

# intersection
print(f"4-9-3 Result of the intersection of two sets cs_courses.intersection(art_courses): "
      f"{cs_courses.intersection(art_courses)}")

# How to create empty list, tuples or sets
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()

print('\n#############################################################')
print('# 5 - Dictionaries - Working with Key-Value Pairs             #')
print('###############################################################')
# https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=5
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(f"Create a dictionnary: student = {{'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}}")
print(f"5-2 To get the value of key 'name' {student['name']}")
print(f"5-3 To get the value of key 'courses' {student['courses']}")

# What happens if we try to access a key that doesn't exist
# print(f"5-3 Access a key that doesn't exixt {student['phone']}") this returns an error
# with the line below instead of an error if the key doesn't exist it returns None
print(f"5-3 Access a key that doesn't exist but without returning an error: student.get('name') {student.get('nam')}")

# We can pass a default key if the key doesn't exist
print(f"5-4 If the key doesn't exist returns a default value student.get('phone, Not Found') "
      f"{student.get('phone', 'Not Found')}")

# Add a new entry to our dictionary
student['phone'] = '555-5555'
print(f"5-5 Add a new entry to our dictionary student['phone']='555-5555' {student}")

# Let's add the phone number and update the name and update the age as well
print(f"5-6 Let's add the phone number and update the name, the age as well in one shot "
      f"student.update({{'name': 'Jane', 'age': 26}}")
student.update({'name': 'Jane', 'age': 26})
print(f"\twich give us {student}")

# Let's say we want to delete a specific key and its value
print(f"5-7 Let's say we want to delete a specific key and its value like this: del student['age']")
del student['age']
print(f'\t{student}')

# Another way we can remove a key and value is with pop method
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(f"5-8 Another way we can remove a key and value is with pop method like this: student.pop('age')"
      f"bear in mind that pop returns the value which is deleted")
age = student.pop('age')
print(f'    We can see that the age has been supressed {student}')
print(f'    As we use pop it returns the element suppressed that we stocked in age variable, age: {age}')

# Let's have a look at how we can loop through the keys and values of our dictionnary
print(f"5-9 Let's have a look at how we can loop through the keys and values of our dictionnary:\n"
      f"\t list of keys: use student.keys() {student.keys()}\n"
      f"\t list of values: use student.values() {student.values()}\n"
      f"\t if we want to see the keys and values: use student.items() {student.items()}")

# Loop through our dictionary
for key, value in student.items():
    print(key, value)

print('\n#############################################################')
print('# 6 - Conditionals and Boolean - If, Else and Elif Statements #')
print('###############################################################')
# https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=6
print('''
# Comparison:
# Equal:                ==
# Not Equal:            !=
# Greater Than          >
# Less Than             <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object Identity       is


''')

print('''
if, elif, else:
language = 'Java'

if language == 'Python':
    print('Language is Python\n')
elif language == 'Java':
    print('Language is Java\n')
elif language == 'JavaScript':
    print('Language is JavaScript\n')
else:
    print('No Match\n')
''')
language = 'Java'

if language == 'Python':
    print('Language is Python\n')
elif language == 'Java':
    print('Language is Java\n')
elif language == 'JavaScript':
    print('Language is JavaScript\n')
else:
    print('No Match\n')

print('''
\n
\n
and, or, not:
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
''')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

print('''
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
''')
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

print('''
is
''')
a = [1, 2, 3]
b = [1, 2, 3]

print(f'a = {a}, b = {b}')
print(f'id de a {id(a)}')
print(f'id de b {id(b)}')
print(f'a is b: {a is b}')
print(f'a == b: {a == b}')

print('''
# False Values:
    # False
    # None
    # Zero of any numeric Type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example {}.
''')
condition = False
if condition:
    print('Condition is set to True. Evaluated to True')
else:
    print(f'Condition is set to False. Evaluated to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Condition is set to None. Evaluated to False')

condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Condition is set to 0. Evaluated to False')

condition = 10
if condition:
    print('Condition is set to 10. Evaluated to True')
else:
    print('Evaluated to False')

condition = []
if condition:
    print('Evaluated to True')
else:
    print('Condition is set to []. Evaluated to False')

condition = ''
if condition:
    print('Evaluated to True')
else:
    print("Condition is set to ''. Evaluated to False")

condition = ()
if condition:
    print('Evaluated to True')
else:
    print("Condition is set to (). Evaluated to False")

condition = {}
if condition:
    print('Evaluated to True')
else:
    print("Condition is set to {}. Evaluated to False")

print('\n#############################################################')
print('# 7 - Loops and Iterations - For / While Loops                #')
print('###############################################################')
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=7
print('''
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
''')

print(f'7-1 break keyword')
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

print(f'\n7-2 continue keyword')
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

print(f'\n7-3 loop in a loop')
for num in nums:
    for letter in 'abc':
        print(num, letter)

print(f'\n7-4 range function:')
# in range the first number is inclusive the second number is not inclusive
for i in range(1, 11):
    print(i)

print("\n7-5 while True")
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

print('\n#############################################################')
print('# 8 - Functions                                               #')
print('###############################################################')


# https://www.youtube.com/watch?v=9Os0o3wzS_I

# https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=8

def hello_func(greeting, name='You'):
    return f'{greeting, name}'


print(hello_func('Hi', name='Julien'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)

# Let's recap
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2017, 2))

print('\n#############################################################')
print('# 9 - Import Modules and Exploring The Standard Library       #')
print('###############################################################')
# https://www.youtube.com/watch?v=CqvZ3vGoGs0

# the course must be watched

print('\n################################################################')
print('# 10 - OS Module - Use Underlying Operating System Functionality #')
print('##################################################################')
# https://www.youtube.com/watch?v=tJxcKyFMTGo
import os
from datetime import datetime

print(f'1- dir(os) will show you all attributes and methods for OS {dir(os)}')
print(f'2- print the working directory we are in with os.getcwd(): {os.getcwd()}')

print(f"\n3-Lets move in our tree")
print(f"3-1 we change directory with os.chdir('/Users/julienpalleau/PycharmProjects/GitHub/pythonProject1')")
os.chdir('/Users/julienpalleau/Desktop/')
print(f'3-2 our current directory is {os.getcwd()}')

print(f"\n4-Lets have a look at what is in the folder")
print(f"4-1 list what is in the directory with os.listdir() {os.listdir()}")

print(f"\n5-Let's say we want to create a folder in Desktop with this name OS-Demo-2")
print(f"5-1 There are two ways to create directory")
print(f"5-1-a os.mkdir('OS-Demo-2')")
print(f"5-1-b os.makedirs('OS-Demo-2/Sub-Dir-1') if you want to create a directory that is "
      f"few levels deep")

print(f"\n6 Deleting folders")
print(f"6-1 Like for directory creation there are 2 ways to delete directory")
print(f"6-1-a os.rmdir('OS-Demo-2")
print(f"6-1.b os.rmdirs('OS-Demo-2/Sub-Dir-1")

print(f"\n7 Rename a file")
print(f"7-1 os-rename('text.txt', 'demo.txt'")

print(f"\n8 Get info about a file")
print(f"8-1 os.stat('demo.txt')")
os.chdir('/Users/julienpalleau/PycharmProjects/GitHub/pythonProject1/')
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print(f"\n9 Get the entire directory tree with files from desktop")
for dirpath, dirnames, filenames in os.walk('/Users/julienpalleau/Desktop/'):
    print('Current Path', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
    print()

print(f"\n10 Get the environment variable with os.environ.get('HOME') {os.environ.get('HOME')}")

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print("file_path = os.path.join(os.environ.get('HOME'), 'test.txt')")
print(f"lets print file_path {file_path}")

print(f"print the file name with os.path.basename('/tmp/test.txt') {os.path.basename('/tmp/test.txt')}")
print(f"print the directory name with os.path.dirname('/tmp/test.txt') {os.path.dirname('/tmp/test.txt')}")
print(f"print file name and directory name os.path.split('/tmp/test.txt') {os.path.split('/tmp/test.txt')}")
print(f"check the exsistance of the path with os.path.exists('/tmp/test.txt') {os.path.exists('tmp/test.txt')}")

print(f"\n11 Check if a path exists if it is a file or a directory:")
print(f"os.path.exists('tmp/test.txt') {os.path.exists('tmp/test.txt')}")
print(f"os.path.isfile('/tmp/fgdfgdf') {os.path.isfile('/tmp/fgdfgdf')}")
print(f"os.path.isdirecotry('/tmp/fgdfgdf') {os.path.isdir('/tmp/fgdfgdf')}")
print(f"the following will split the root of the path and the extension os.path.splitext('/tmp/text.txt')"
      f"{os.path.splitext('/tmp/text.txt')}")

print('\n###############################################')
print('# 11 - File Objects - Reading and Writing Files #')
print('#################################################')
# https://coreyms.com/development/python/python-tutorial-file-objects-reading-writing-files
os.chdir('/Users/julienpalleau/PycharmProjects/GitHub/pythonProject1')

# The way to open a file without context manager
print('''11-1
Opening a file without context manager: 
f=open('test.txt', 'r') 
Let's have a look to how the file has been opended with f.mode}
!!! The most important: 
When you open the file this way DO NOT FORGET to close the file like fhis f.close()")
''')
f = open('test.txt', 'r')
f.close()

# The way to open a file with context manager
print('''11-2
The way to open a file with context manager
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
''')

print(f'11-3 read a file with context manager with f.read()')
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    # or

print(f'\n11-4 read a file with context manager with f.readline()')
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')  # The end is not necessary in this case it is to suppress too much return line

# The Right Way to read a file with context manager, as we don't store all the file in memory avoiding outage of memory.
# However we still read the complete file.
print(f"\n11-5 The Right Way to read a file, as we don't store all the file in memory avoiding outage of memory. "
      f"However we still read the complete file.")
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Now let's go back to f.read() but with an option f.read(100)
print(f"\n\n11-6 Let's do it again with f.read() but with an option f.read(100)")
with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents)

print(f"\n\n11-7 In this example we are going to read by chunk of 10 characters")
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

print(f"\n\n11-8 How to see the position of our cursor? with f.tell()")
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    print(f'it says we are currently at {f.tell()}th position in the file with f.tell()')

print(f"\n\n11-9 Let's have a look at the first 10 characters ")
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    print('\nwe change our position to position 0 with f.seek(0) and print 10 characters')
    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)

print(f"\n11-10 Write in the file test2.txt, be carrefull you'll erase everything whitch is already in the file")
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

print(f"\n11-11 Append in a file")
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

print(f"\n11-11 Use the binary mode and copy an image")
with open('75083.jpg', 'rb') as rf:
    with open('75083_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

print('\n#######################################################################')
print('# 12 - How to Set the Path Witch Between Different Versions/Executables #')
print('#########################################################################')
# https://www.youtube.com/watch?v=PUIE7CPANfo

print('\n##################################################################################')
print('# 13 - Variable Scope - Understanding the LEGB rule and global/nonlocal statements #')
print('####################################################################################')
# https://www.youtube.com/watch?v=QVdf0LgmICw
print('''
LEGB 
Local, Enclosing, Global, Built-in
''')


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()

print('\n##################################################################################')
print('# 14 - VENV - How to Use Virtual Environmnets with the Built-In venv Module        #')
print('####################################################################################')
# https://www.youtube.com/watch?v=Kg1Yvry_Ydk
'''
create a project: 
    mkdir my_project
create the virtual environment for my_project: 
    python -m venv my_project/venv
    source my_project/venv/bin/activate
    cd my_project

How to save your list of packages:
    pip freeze > requirements.txt

From now we have two option 
    1/  either we have a requirement.txt file with the list of package we want to install:
        pip install -r requirement.txt
    2/  or you duplicate your environment within your virtual environment:
        deactivate
        rm -rf venv
        python -m venv --system-site-packages
        source venv/bin/activate

To deactivate the virtual environment
    deactivate
'''

print('\n##################################################################################')
print('# 15 - Common Python Mistakes and How to Fix Them                                  #')
print('####################################################################################')

''' 1- tab and space issues
    2- import a local module with the same name as a module from standard library
    3- use a variable name with the same name as an imported function
    4- Mutable Default arguments:
        def add_employee(emp, emp_list=[]):
            emp_list.append(emp)
            print(emp.list)
        emps = ['John', 'Jane')
        add_employee('John')
        
        the code above will return  ['John', 'Jane', 'Corey'] so it works as expected.
        
        Now if we restart the same exp like this but with one more line the last one:
        def add_employee(emp, emp_list=[]):
            emp_list.append(emp)
            print(emp.list)
        emps = ['John', 'Jane')
        add_employee('Corey')
        add_employee('John')
        add_employee('Jane')
        We get one list:
        ['Corey', 'John', 'Jane']
        
        What happens is that in python default arguments are evaluated once at the time it creates the function.
        
        def add_employee(emp, emp_list=[]):
            emp_list.append(emp)
            print(emp.list)
            
        print(add_employee.__defaults__)
        add_employee('Corey')
        print(add_employee.__defaults__)
        add_employee('Jane')
        print(add_employee.__defaults__)
        
        We got:
        ([],)
        ['Corey']
        {['Corey',])
        ['Corey', 'John']
        (['Corey', 'John',)
        
            
        def add_employee(emp, emp_list=None):
            if emp_list is None:
                emp_list = []
            emp_list.append(emp)
            print(emp_list)
        
        print(add_employee_fixed.__defaults__)
        add_employee('Corey')
        print(add_employee_fixed.__defaults__)
        add_employee('John')
        
        We got:
        (None,)
        ['Corey']
        (None,)
        ['John']
        
        
        This create only 1 list and not 2. If you keep adding employee the list keep growing.
        If we want a new list per user then we have to do:
        def add_employee(emp, emp_list=None): 
    
    5- TIME Default arguments again
        import time
        from datetime import datetime
        
        def display_time(time=datetime.now()):
            print(time.strftime('%B %d, %Y %H:%M:%S'))
            
        display_time()
        time.sleep(1)
        display_time()
        time.sleep(1)
        display_time()
        
        we expect to see the time incremented by 1s each time it is displayed.
        However this is not the case because as above it only execute those default arguments (%B %d, %Y %H:%M:%S)
        once when the function is declared and not each time the function is run.
        To fix the problem let's do:
        def display_time(time=None)
            if time is None:
                time = datetime.now()
            print(time.strftime('%B %d, %Y %H:%M:%S'))
        now if we run this we can see that it sleeps 1 s between each function call.
        
    6 - How iterators work
        names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
        heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
        identities = zip(names, heroes)
        
        print(identitites)
        Pytnon2 -> [('Peter Parker', 'Spiderman'), ('Clark Kent', 'Superman), ('Wade Wilson', 'Deadpool'), 
        ('Bruce Wayne', 'Batman')]
        
        Python3 -> zip object at 0x10791eb08
        python3 you'll have to cast the zip in a list like this: identities=list(zip(names, heroes))
        print(identities) and now we get:
        [('Peter Parker', 'Spiderman'), ('Clark Kent', 'Superman), ('Wade Wilson', 'Deadpool'), 
        ('Bruce Wayne', 'Batman')]
        
    7 - imports, avoid from os import *, this is a bad practice because
        - it makes the code harder to debug
        - it can confused people introduce but ex:
            from html import escape as h_escape
            from glob import escate as h_escape
            
            if we used from html import *
                            glob import *
            it is not possible to know which escape we will use.        
'''

print('\n##################################################################################')
print('# 16 - How to work with Dates, Times, Timdeltas, and Timezones                     #')
print('####################################################################################')
# https://www.youtube.com/watch?v=eirjjyP2qcQ
import datetime
import pytz

# # !!! be careful to not pass in the date for instance 7 and not 07
# d = datetime.date(2016, 7, 24)
# print(f'date with datetime.date(2016, 7, 24) {d}')
#
# tday = datetime.date.today()
# print(tday)
# print(tday.day)
# print(f'Monday is 0 and Sunday 6 for tday.weekday() {tday.weekday()}')
# print(f'Monday is 1 and Sunday 7 fir tday.isoweekday() {tday.isoweekday()}')
# tdelta = datetime.timedelta(days=7)
# print(f'tdelta= {tdelta}')
# print(f'{tday - tdelta}')
#
# # date2 = date1 + tdelta
# # tdelta = date1 + date2
#
# bday = datetime.date(2024, 5, 8)
# till_bday = bday - tday
# print(f"Nombre de jours restant de aujourd'hui au 8 mai 2024: {till_bday.days}")
# print(f"Nombre de secondes restantes de ajourd'hui au 8 mai 2024: {till_bday.total_seconds()}")
#
# # this one is not often used usually the one after is more used
# t = datetime.time(9, 30, 45, 100000)
# print(t.hour)
#
# dt = datetime.datetime(2022, 7, 26, 12, 30, 45, 100000)
# print(f'in using datetime like this dt = datetime.datetime(2022, 7, 26, 12, 30, 45, 100000) we can have the '
#       f'full date and time with dt: {dt}')
# print(f'the year only with dt.year: {dt.year}')
# print(f'the date only with dt.date(): {dt.date()}')
# print(f'the time only with dt.time(): {dt.time()}')
# tdelta = datetime.timedelta(hours=12)
# print(dt + tdelta)
#
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
#
# # Use the timezone
# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(f'time with timezone {dt}')
#
#
# # The two syntax below are doing the same but the first one is preferred as it is shorter
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
#
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)
#
# dt_fr = dt_utcnow.astimezone(pytz.timezone('Europe/Paris'))
# print(f"Affiche l'heure dans la timezone Europe/Paris {dt_fr}")
#
# for tz in pytz.all_timezones:
#     print(tz)

dt_fr = datetime.datetime.now()
dt_uk = pytz.timezone('Europe/London')
dt_fr = dt_uk.localize(dt_fr)
print(dt_fr)

dt_fr = datetime.datetime.now(tz=pytz.timezone('EUROPE/Paris'))
# Using is format
print(dt_fr.isoformat())

# strftime: Datetime to a String
print(dt_fr.strftime('%B %d, %Y'))
dt_str = 'June 08, 2023'

# strptime: String to Datetime
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

print('\n##################################################################################')
print('# 17 - Calculate Number of Days, Weeks, or Months to Reach Specific Goals          #')
print('####################################################################################')
# https://www.youtube.com/watch?v=k8asfUbWbI4
import datetime
import calendar

balance = 10000
interest_rate = 13 * 0.01
monthly_payment = 1000

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)

current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week

print(f'Date at which you are supposed to reach the goal {end_date}')
print(f'Reached goal in {(end_date - start_date).days // 7} weeks')

import math

goal_subs = 150000
current_subs = 85000
subs_to_go = goal_subs - current_subs

avg_subs_day = 200
days_to_go = math.ceil(subs_to_go / avg_subs_day)

today = datetime.date.today()
print(today + datetime.timedelta(days=days_to_go))

print('\n##################################################################################')
print('# 18 - Slicing Lists and Strings                                                   #')
print('####################################################################################')
# # https://www.youtube.com/watch?v=ajrtAuDg3yw
#
# my_list =           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # positive index:    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# # negative index:  -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
#
# print('How to access a single value:')
# print(f'first element of the list with index 0: {my_list[0]}')
# print(f'sixth element of the list witn index 5: {my_list[5]}')
# print(f'last element of the list with index -1: {my_list[-1]}')
# print(f'first element of the list with index -10: {my_list[-10]}')
#
# print('\nHow to access a range of values:')
# # list[start:end:step]
# print(f'values from index 0 to index of 5 with my_list[0:6] 6 as the second value is not inclusive {my_list[0:6]}')
# print(f'values from index 3 to 7 with my_list[3:8]: {my_list[3:8]}')
# print(f'values from index -7 to -2 with my_list[-7:-2]: {my_list[-7:-2]}')
# print(f'values from index 1 to -2 with my_list[1:-2]: {my_list[1:-2]}')
# print(f'values from index 1 to the end my_list[1:]: {my_list[1:]}')
# print(f'values from beginning to the end with my_list[:-1]: {my_list[:-1]}')
# print(f'entire list with my_list[:]: {my_list[:]}')
# print(f'entire list with a step of 2 my_list[::2]: {my_list[::2]}')
# print(f'values from index -1 to index of 2 and a step of -1 with my_list[-1:2:-1]: {my_list[-1:2:-1]}')
# print(f'values from index 8 to index of 2 and a step of -1 with my_list[-2,2:-1]: {my_list[-2:2:-1]}')
# print(f'entire list reversed my_list[::-1]: {my_list[::-1]}')
#
# sample_url='http://coreyms.com'
#
# # Reverse the url
# print(sample_url[::-1])
#
# # Get the top level domain
# print(sample_url[-4:])
#
# # Print the url without the http://
# print(sample_url[7:])
#
# # Print the url without the http:// or the top level domain
# print(sample_url[7:-4])


print('\n##################################################################################')
print('# 19 - Comprehension - How tey work and why you should be using them               #')
print('####################################################################################')
# https://www.youtube.com/watch?v=3dt4OGnU5sM

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'\n19-1 List comprehension')
# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#   if n%2 == 0:
#       my_list.append(n)
# print my_list

# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abc':
    for num in range(4):
        my_list.append((letter, num))
    print(my_list)

my_list = [(letter, num) for letter in 'abc' for num in range(4)]
print(my_list)

# Dictionnary Comprehensions
print(f'\n19-2 Dictionnary Comprehnesions')
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'DeadPool']
test = zip(names, heros)
print(list(test))

# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

# If name not equal to Peter
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

print(f'\n19-3 Set Comprehensions')
# Set Comprehensions
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

my_set = {n for n in nums}
print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def gen_func(nums):
#     for n in nums:
#         yield n * n


# my_gen = gen_func(nums)

my_gen = (n * n for n in nums)

for i in my_gen:
    print(i)

print('\n##################################################################################')
print('# 20 - Sorting Lists, Tuples, and Objects                                          #')
print('####################################################################################')
# # https://www.youtube.com/watch?v=D3JvDWO-BY4
# # List
# print("\n List:")
# li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
# s_li = sorted(li)
# a = 1
# b = 2
#
# print(f'Sorted Variable li with sorted function s_li=sorted(li) :\t\t\t\t\t\t\t{s_li}')
#
# print(f'Sorted Variable li to sort in reverse order :\t\t\t\t\t\t\t\t\t\t{sorted(li, reverse=True)}')
# li.sort()
# print(f'Sort li variable with li.sort() operate in place as a consequence li is modified :\t{li}')
#
# # Tuple
# print("\nTuple:")
# tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# s_tup = sorted(tup)
# print(f"tuple d'origine: {tup}")
# print(f'A tuple can be sorted with sorted() and not with tup.sort() Tuple', s_tup)
#
# # Dictionary
# print("\nDictionary:")
# di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
# s_di = sorted(di)
# print(f"A dictionary d'origine Dict: {s_di}")
# print(f'A dictionary can be sorted with sorted(di) Dict: {s_di}')
#
# # With functions other than list you need sorted
# print('With functions other than list you need sorted')
#
# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li)
# print(f'list sorted with s_li=sorted(li): {s_li}')
#
# print(f'\nTransform the list in a list of absolute values with sorted(li, key=abs):')
# s_li = sorted(li, key=abs)
# print(f"sort the list {li} as absolute values {s_li}")
#
# # Objects
# print("\nObjects")
#
#
# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def __repr__(self):
#         return f'{self.name}, {self.age}, ${self.salary}'
#
#
# from operator import attrgetter
#
# e1 = Employee('Carl', 37, 70000)
# e2 = Employee('Sarah', 29, 80000)
# e3 = Employee('John', 43, 90000)
#
# employees = [e1, e2, e3]
#
#
# def name_sort(emp):
#     return emp.name
#
#
# s_employees = sorted(employees, key=name_sort)
# s_employees = sorted(employees, key=lambda e: e.name)
# print(s_employees)
#
#
# def age_sort(emp):
#     return emp.age
#
#
# s_employees = sorted(employees, key=age_sort)
# s_employees = sorted(employees, key=attrgetter('age'))
# print(s_employees)
#
#
# def salary_sort(emp):
#     return emp.salary
#
#
# s_employees = sorted(employees, key=salary_sort, reverse=True)
# print(s_employees)

print('\n##################################################################################')
print('# 21 - Try/Except Blocks for Error Handling                                        #')
print('####################################################################################')
# # https://www.youtube.com/watch?v=NIWwJbo-9_8
#
#
# try:
#     f = open('test.txt')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print('Executing Finally...')
#
# # It is also possible to raise an exception on its own
# try:
#     f = open('test2.txt')
#     if f.name == 'test2.txt':
#         raise Exception
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print("Error !")
# else:
#     print(f.read())
#     f.close()
# finally:
#     print('Executing Finally...')

print('\n##################################################################################')
print('# 22 - Iterators & Iterables                                                       #')
print('####################################################################################')
# # https://www.youtube.com/watch?v=jTYiNjvnHZY
#
# # iterables is something that can be looped over
# nums = [1, 2, 3]
# # for num in nums:
# #     print(num)
#
# # How can we tell if something is iterable ?
# # If something is iterable it needs to have a special method called __iter__()
# # Let's check with dir if our list of numbs is an iterable
# # print(dir(nums))
# # we can see __iter__ so this list is iterable
#
# # Now, what make something an iterator?
# # An iterator is an object with a state, so that it remembers where it is during iteration.
# # An iterator as a state where it knows where it is during iteration and iterators also know how to get the next value
# # they get their next value with __next__ method. Now look at our list nums, it doesn't have a state and it doesn't
# # know how to look at its next value, so therefor, it is not an iterator.
#
# # The two lines below are equivalent but the first one is a bit ugly.
# #i_nums = nums.__iter__()
# i_nums = iter(nums)
#
# # print(i_nums)
# # print(dir(i_nums))
#
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
#
# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break


# # Iterator
# class MyRange:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current
#
#
# nums = MyRange(1, 10)
#
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# # Generator
# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1
#
#
# nums = my_range(1, 10)
#
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
#
# for num in nums:
#     print(num)


# Iterator Problem

# # First possible solution with a class
# class Sentence:
#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration
#         index = self.index
#         self.index += 1
#         return self.words[index]
#
#
# my_sentence = Sentence('This is a test')
#
# for word in my_sentence:
#     print(word)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))


# # Second possible solution with a Generator
# def sentence(sentence):
#     for word in sentence.split():
#         yield word
#
#
# my_sentence = sentence('This is a test')
#
# # for word in my_setence:
# #     print(word)
#
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))


print('\n##################################################################################')
print('# 23 - Iterator Functions for Efficient Looping                                    #')
print('####################################################################################')
# # https://www.youtube.com/watch?v=Qu3dThVy6KQ
import itertools

#
#
# def lt_2(n):
#     if n < 2:
#         return True
#     return False
#
#
# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['Corey', 'Nicole']
# selectors = [True, True, False, True]
#
# print('\nAn iterator is sequential data that we can iterate or loop over')
#
# print('\n1 - create a counter with itertools.count(start=5, step=-2.5)')
# counter = itertools.count(start=5, step=-2.5)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
#
# print("\n2 - ZIP")
# # # Let's have a look to a scenario where it can be useful
# # data = [100, 200, 300, 400]
# #
# print("\n 2-1 Classic ZIP")
# # daily_data = list(zip(range(10), data))
# # print(daily_data)
# #
# print("\n 2-2Longest Zip")
# # daily_data = list(itertools.zip_longest(range(10), data))
# # print(daily_data)
#
# print('\n3 - itertools')
# # # Itertools.cycle
# print("\n3-1 itertools.cycle()")
# # counter = itertools.cycle(('On', 'Off'))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
#
# print("\n3-2 itertools.repeat()")
# # # Itertools.repeat
# # counter = itertools.repeat(2)
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
#
# # # we can define how many times we want to repeat, this will raise an error when you go beyond 3
# # counter = itertools.repeat(2, times=3)
# # squares = map(pow, range(10), itertools.repeat(2))
# # print(list(squares))
# #
# # # print(next(counter))
# # # print(next(counter))
# # # print(next(counter))
# # # print(next(counter))
# # # print(next(counter))
# # # print(next(counter))
#
# print('\n4 - starmap')
# # # we use starmap
# print('\n4-1 starmap make from multiple tuples a list')
# # counter = itertools.repeat(2, times=3)
# # squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
# # print(list(squares))
#
#
# # The most popular function from itertools:
# # Combination and Permutation
# print('\n5 - combination')
# # result = itertools.combinations(letters, 2)
#
# print('\n6 - Permutation')
# # result = itertools.permutations(letters, 2)
#
# print("\n7 - Repeat n times")
# result = itertools.product(numbers, repeat=4)
#
# for item in result:
#     print(item)
#
# print("\n7 - combined n lists in one: itertools.chain(letters, numbers, names)")
# combined = itertools.chain(letters, numbers, names)
#
# for item in combined:
#     print(item)
# print("----------")
# print('\n8 - Slice')
# # In a range 0-9, slice from 0 to 4
# print('\n8-1 In a range of 0-9, slice from 0 to 4')
# result = itertools.islice(range(10), 5)
#
# for item in result:
#     print(item)
#
# # In a range 0-9 from 1 to 4
# print("\n8-3 In a range of 0-9, slice from 1 to 4")
# result = itertools.islice(range(10), 1, 5)
#
# for item in result:
#     print(item)
#
# # # In a range 0-9, from 1 to 4 with a step of 2
# print("\n8-4 In a range of 0-9, slice from 1 to 4 with a step of 2")
# result = itertools.islice(range(10), 1,  5, 2)
#
# for item in result:
#     print(item)
#
# # # Why is this useful? This is useful because we may have an iterator which is to big to be put into memory.
# # # For example let's imagine we have a log file with hundred of thousands lines
# # # We could use islice to efficiently deal with this huge log file
# print("\n8-5 islice allow you to slice a huge log file that you need to read in multiple smaller chunk/slice")
# with open('test.log', 'r') as f:
#     header = itertools.islice(f, 3)
#
#     for line in header:
#         print(line, end='')
#
# print('\n9 - Selector')
# # # Selector allow us to combine a list letters for example with a list of booleans and then print only when True
# # result = itertools.compress(letters, selectors)
# #
# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['Corey', 'Nicole']
# selectors = [True, True, False, True]
#
# print('\n10 - Filter')
# # Filter it filter value based on associated selector
# print("----------")
# print("Filter")
# result = filter(lt_2, numbers)
# for item in result:
#     print(item)
# print("----------")
# result = itertools.filterfalse(lt_2, numbers)
# for item in result:
#     print(item)
#
# print('\n11 - Dropwhile')
# # Dropwhile it will drop values < 2 till it meets a value which doesn't meet the condition
# numbers = [0, 1, 2, 3, 2, 1, 0]
# result = itertools.dropwhile(lt_2, numbers)
#
# for item in result:
#     print(item)
#
# print("----------")
# print("\n12 - Takewhile")
# # Takewhile is the opposite of Dropwhile ang grab all the values that return true until it hits a value that returns
# # false and after he got a value that returns false he just return the values that add up until that point.
# result = itertools.takewhile(lt_2, numbers)
# for item in result:
#     print(item)

# print("\n10 - accumulate")
# # accumulate it just keeps a running total of values he has just seen so far
# letters = ['a', 'b', 'c', 'd']
# numbers = [1, 2, 3, 0]
# names = ['Corey', 'Nicole']
#
# result = itertools.accumulate(numbers)
# for item in result:
#     print(item)
#
# print("----------")
# print("\n11 - accumulate with multiply")
# # multiply all values in a list with each other
# import operator
# result = itertools.accumulate(numbers, operator.mul)
# for item in result:
#     print(item)

# print("----------")
# print("\n12 - group by")
#
# def get_state(person):
#     return person['state']
#
# people = [
#     {'name': 'John Doe',
#      'city': 'Gothman',
#      'state': 'NY'
#      },
#     {
#         'name': 'Jane Doe',
#         'city': 'Kings Landing',
#         'state': 'NY'
#     },
#     {
#         'name': 'Corey Schafer',
#         'city': 'Boulder',
#         'state': 'CO'
#     },
#     {
#         'name': 'Al Einstein',
#         'city': 'Denver',
#         'state': 'CO'
#     },
#     {
#         'name': 'John Henry',
#         'city': 'Hinton',
#         'state': 'WV'
#     },
#     {
#         'name': 'Randy Moss',
#         'city': 'Rand',
#         'state': 'WV'
#     },
#     {
#         'name': 'Nicole K',
#         'city': 'Asheville',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jim Doe',
#         'city': 'Charlotte',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jane Taylor',
#         'city': 'Faketown',
#         'state': 'NC'
#     }
# ]
#
#
# person_group = itertools.groupby(people, get_state)
# for key, group in person_group:
#     print(key, len(list(group)))
#     # for person in group:
#     #     print(person)
#     # print()
#
# print("----------")
# print("\n13 - Replicate iterator")
# person_group = itertools.groupby(people, get_state)
# copy1, copy2 = itertools.tee(person_group)
# for key, group in person_group:
#     print(key, len(list(group)))

print('####################################################################################')
print('# 24 - Python OOP - Class and Instances - 1                                        #')
print('####################################################################################')
# collection class
# https://www.youtube.com/results?search_query=corey+schafer+class+variable

# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return f'{self.first} {self.last}'


# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)
#
# # print(emp_1)
# # print(emp_2)
#
# print(emp_1.email)
# print(emp_2.email)
#
# print(f'{emp_1.first} {emp_1.last}')
# print(f'{emp_2.first} {emp_2.last}')
#
# print(f'{emp_1.fullname()}')
# print(f'{emp_2.fullname()}')

print('####################################################################################')
print('# 25 - Python OOP - Class Variables - 2                                            #')
print('####################################################################################')
# https://www.youtube.com/watch?v=BJ-VvGyQxho

# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# print(Employee.num_of_emps)
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)
#
# print(Employee.__dict__)
#
# emp_1.raise_amount = 1.05
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.num_of_emps)


print('####################################################################################')
print('# 26 - Python OOP - classmethods and staticmethods - 3                             #')
print('####################################################################################')

# https://www.youtube.com/watch?v=rq8cL2XMM5M

# # Classmethod
# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)
#
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

# # Static method
# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)
#
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# import datetime
#
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))

print('####################################################################################')
print('# 27 - Python OOP - Inheritance creating a subclass - 4                            #')
print('####################################################################################')
# # https://www.youtube.com/watch?v=RSl87lqOXDE
#
# print("\n27-1 Inheritance")
# class Employee:
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#
# class Developper(Employee):
#     raise_amt = 1.10
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#
#
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emps(self):
#         for emp in self.employees:
#             print(f'-->{emp.fullname()}')
#
#
# dev_1 = Developper('Corey', 'Schafer', 50000, 'Python')
# dev_2 = Developper('Test', 'Employee', 60000, 'Java')
#
# mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
# print(mgr_1.email)
#
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()
#
# # print(dev_1.email)
# # print(dev_1.prog_lang)
#
# # print(help(Developper))
#
# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)
#
# # Let's have a look to is_instance or is_subclass
# print("\n27-2 Let's have a look to is_instance or is_subclass")
# print(f'Is mgr_1 an instance of Employee with isinstance(mgr_1, Employee): {isinstance(mgr_1, Employee)}')
# print(f'Is Manager a Subclass of Employee with issubclass(Manager, Employee): {issubclass(Manager, Employee)}')


print('####################################################################################')
print('# 28 - Python OOP - Special (Magic/Dunder) Methods - 5                             #')
print('####################################################################################')

# # https://www.youtube.com/watch?v=3ohzBxoFHAY
#
# class Employee:
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#     # repr is meant to be an unambiguous representation of the object and should be use for debugging and logging and
#     # things like that it is really meant to be seen by other developers. And str is meant to be more of a readable
#     # representation of an object and is meant to be used as a display to the end user.
#
#     def __repr__(self):
#         return f"Employee({self.first}, {self.last}, {self.pay})"
#
#     def __str__(self):
#         return f"{self.fullname()}, {self.email}"
#
#     def __add__(self, other):
#         return self.pay + other.pay
#
#     def __len__(self):
#         return len(self.fullname())
#
#
# # All special methods: https://docs.python.org/3/reference/datamodel.html#special-method-names
#
# emp_1 = Employee('Corey', 'Schafer', 5000)
# emp_2 = Employee('Test', 'Employee', 6000)
#
# print(len(emp_1))
#
# # print(emp_1 + emp_2)
#
# # print(repr(emp_1))
# # print(str(emp_1))
# # # the lines above are equivalent to the lines below
# # print(emp_1.__repr__())
# # print(emp_1.__str__())
#
#
# # The 3 special methods above are the most used,
# # Now Let's have a look to a few more


print('####################################################################################')
print('# 29 - Generate Random Numbers and Data Using the random Module                    #')
print('####################################################################################')
# https://www.youtube.com/watch?v=KzqSDvzOFNA
# https://docs.python.org/3/library/random.html

import random

print('\n29 - Random')

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert',
               'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth',
               'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson',
              'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore',
              'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor',
               'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg',
               'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria',
               'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
          'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
          'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

print('29 - 1 random.random(), random.randint(), radom.choice()')
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
# value = random.random() # random takes no argument
value_1 = random.random()
value_2 = random.randint(0, 10)
print(value_1, value_2)

value_3 = random.choice(greetings)
print(value_3 + ', Corey!')

colors = ['Red', 'Black', 'Green']
print("we set ['Red', 'Black', 'Green'] and ask 10 times to take one randomly")
results = random.choices(colors, k=10)
print(results)

print("Let's pass an additional argument weights, which will be a list to put weight on each array value")
results = random.choices(colors, weights=[18, 18, 2], k=10)

print("Let's pickup a list of numbers between 1 and 53 and shuffle it")
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

print("Let's create a hand in taking 5 cards take off a card twice (so you don't repeat a same number)")
hand = random.sample(deck, k=5)

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(1000, 9999)
    address = f'{street_num} {street} St., {state} {zip_code}'
    email = first.lower() + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')

print('####################################################################################')
print('# 30 - Python OOP - Property Decorators - Getters, Setters, and Deleters - 6       #')
print('####################################################################################')
# # https://pythonforge.com/property/
# # https://www.youtube.com/watch?v=jCzT9XFZ5bw
# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
#     @property
#     def fullname(self):
#         return f'{self.first}, {self.last}'
#
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name!')
#         self.first = None
#         self.last = None
#
#
# emp_1 = Employee('John', 'Smith')
# emp_1.fullname = 'Corey Schafer'
# # emp_1.first = 'Jim'
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
#
# del emp_1.fullname

print('####################################################################################')
print('# 31 - Module CSV - Comment lire, analyser et ecrire des fichiers csv              #')
print('####################################################################################')
# https://www.youtube.com/watch?v=q5uM4VKywbA
# import csv
#
# with open('named.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('names.csv', 'r') as new_file:
#         fieldnames = ['new_names.csv', 'last_name', 'email']
#
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             del line['email']
#             csv_writer.writerow(line)

print('####################################################################################')
print('# 32 - Python Tips and Tricks For Writting Better Code                             #')
print('####################################################################################')
# https://www.youtube.com/watch?v=C-gEQdGVXbk

# 32-1 - Ternary condition
print('32-1 - Ternary condition')
condition = True

if condition:
    x = 1
else:
    x = 0

print(x)

# There is a faster way to write the lines above with ternary condition
condition = False
x = 1 if condition else 0
print(x)

# 32-2 - Large numbers
print('\n32-2 - Large numbers')
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')

# 32-3 - Opening a file
print('\n32-3 Opening file')

# 32-3-1 Old way to open a file
print('''\n32-3-1 Old way to open a file:
f = open('test.txt', 'r')
file_contents = f.read()
f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
''')
f = open('test.txt', 'r')
file_contents = f.read()
f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# 32-3-2 It is better to use context manager
print('32-3-2 It is better way to open a file in using contex manager')
print('''
with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
''')
with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# 32-4 - enumerate function
print('\n32-4 - enumerate function')

print('''mistake when you need an index:
index = 0
names = ['Corey', 'Chris', 'Dave', 'Travis']

for name in names:
    print(index, name)
    index += 1
''')
index = 0
names = ['Corey', 'Chris', 'Dave', 'Travis']

for name in names:
    print(index, name)
    index += 1

print('''there is better way to write the code above:
    names = ['Corey', 'Chris', 'Dave', 'Travis']
    for index, name in enumerate(names, start=0):
        print(index, name)
''')
names = ['Corey', 'Chris', 'Dave', 'Travis']
print('with enumerate we can pass as an argument where we want to start')
for index, name in enumerate(names, start=1):
    print(index, name)

# 32-5 This example is similar to the previous one
print('\n32-5 - Opening 2 files')
print(f'''
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

The code below works but this is not intuitive and there is a better way to write this code in python:
for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{{name}} is actually {{hero}}")
''')
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universe = ['Marvel', 'DC', 'Marvel', 'DC']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{name} is actually {hero}")

print('''Better way to write the code above:
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')
''')
print('In this case all of our list are the same length')
for name, hero, universe in zip(names, heroes, universe):
    print(f'{name} is actually {hero} from {universe}')
print('\nIf the list are not the same length, list will stop after the shortest list is exausted, if you want\n'
      'zip to go to the end of the longest list then you have to use the ziplongest function from the itertools\n'
      'library.')

print('\n32-6 - How unpacking works')
print(f'''
32-6-1 unpack values in 2 different variables:
a, b = (1, 2)
print(a)
print(b)

32-6-2 Now if you only want to use a variable and ignore b variable:
a, _ = (1, 2)
So _ tells python or anyone else that you are not planning to use that variable any where else in the code

32-6-3 If you try: more variables than values:
a, b, c = (1, 2)
you'll get a value error: not enough values to unpack (expected 3, got 2)

32-6-4-1 If you try: more values than variables:
a, b, c = (1, 2, 3, 4, 5)
you'll get a value error: too many values to unpack

32-6-4-2 Again, more values than variables but with a different syntax:
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
>> 1
>> 2
>> [3, 4, 5]

32-6-4-3 Again, like above but let's say this time that we want to ignore the last values (c)
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
>> 1
>> 2

32-6-5 Other unpacking possibilities
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(b)
print(c)
print(d)
>> 1
>> 2
>> [3, 4, 5, 6]
>> 7
''')

print(f'\n32-7 Getting and setting attribute on a certain object')
# print('''
# class Person():
#     pass
#
#
# person = Person()
#
# person.first = "Corey"
# person.last = "Schafer"
#
# print(person.first)
# print(person.last)
# ''')
# class Person():
#     pass
#
#
# person = Person()
#
# person.first = "Corey"
# person.last = "Schafer"
#
# print(person.first)
# print(person.last)
print('--------------')

# now what if the attribute we want to set is another variable?
# Lets start again
# class Person():
#     pass
#
#
# person = Person()
#
# first_key = 'first'
# first_val = 'Corey'
#
# # person.first_key = first_val this line doesn't work you have to use setattr:
# setattr(person, first_key, first_val)
# first = getattr(person, first_key)
# print('++++')
# print(first)

# class Person():
#     pass
#
# person = Person()
# person_info = {'first': 'Corey', 'last': 'Schafer'}
#
# for key, value in person_info.items():
#     setattr(person, key, value)
#
# for key in person_info.keys():
#     print(getattr(person, key))


print(f'\n32-8 Inputting secret information')
# # print(f'\n31-8-1 The wrong way to do this')
# # username = input('Username: ')
# # password = input('Password: ')
#
# print('Logging In...')
# print(f'\n31-8-2 The right way to do this')
# from getpass4 import getpass
#
# # ne fonctionne pas dans PC mais uniquement dans la console.
# # Le bug est reporte dans stack overflow, apres il y a pleins de bidouille a faire pour fixer le pb dans PC
#
# password = getpass('Password: ')
# print(password)
#
# # username = input('Username: ')
# # password = getpass(prompt="Type new password: ")
# #
# # print('Logging In...')

print(f'\n32-9 what does python -m means?')
# -m in the official documentation will search sys.path for the named modul and execute its content as the main
# modul. It means that it simply running that specific modul specifying after -m.

print('####################################################################################')
print('# 33 - Else Clauses on Loops                                                       #')
print('####################################################################################')
# my_list = [1, 2, 3, 4, 5]
#
# for i in my_list:
#     print(i)
# else:
#     print('num is not less than 2!')

# you have to see the else as a no break, so in other words when you finish the iteration on my_list no_break and run
# print('num is not less than 2!')

# So the for else means do all the iteration in for and then go to the else.

# Another example
# def find_index(to_search, target):
#     for i, value in enumerate(to_search):
#         print(value)
#         if value != target:
#             break
#         else:
#             return -1
#         return i
#
# my_list = ['Steve', 'Rick', 'John']
#
#
# print(f'Location of target is index: {find_index(my_list, "Steve")}')

# for i in range(0,5):
#     print(i)
# else:
#     print(f'test {i}')


print('####################################################################################')
print('# 34- ENV VARS WINDOWS                                                             #')
print('####################################################################################')
# # https://www.youtube.com/watch?v=IolxqkL7cD8
# import os
#
# db_user = os.environ.get('DB_USER')
# db_password = os.environ.get('DB_PASS')
#
# print(db_user)
# print(db_password)


print('####################################################################################')
print('# 35- How to send Emails Using Python - Plain Text, Adding Attachments, HTML       #\n'
      "# emails and More - NE FONCTIONNE PAS POUR L'INSTANT MAIL setup                    #")
print('####################################################################################')
# https://www.youtube.com/watch?v=JRCJ6RtE3xU
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#
#     subject = 'Grab dinner this weekend'
#     body = 'How about dinner at 6pm this Saturday'
#
#     msg = f'Subject: {subject}\n\n{body}'
#
#     smtp.sendmail(EMAIL_ADDRESS, '', msg)


print('####################################################################################')
print('# 35 - Automate Parsing and Renaming of Multiple Files                             #')
print('####################################################################################')
# https://www.youtube.com/watch?v=ve2pmm5JqmI
import os

os.chdir('/Users/julienpalleau/Downloads')
result = {}
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if 'IMG' in file_name:
        f_title, f_number = file_name.split('_')
        result[f_number] = f_title
for i, x in enumerate(sorted(result.keys())):
    print(x, list(result.values())[i])

print('####################################################################################')
print('# 36 - First Class Functions                                                       #')
print('####################################################################################')
# https://www.youtube.com/watch?v=kr0mpwqttM0
print('''
36-1 First-Class Function and First-Class Citizen
First-Class Functions:
"A Programming language is said to have first-class functions if it treats functions as first-class citizens."

First-Class Citizen (Programming):
"A first-class citizen (sometimes called first class objects) in a programming language is an entity which supports
all the operations generally available to other entities. These operations typically include being passed as an
argument, returned from a function, and assigned to a variable."
''')


def square(x):
    return x * x


f = square(5)
f = square
print('f = square(5), f = square')
print('''f = square
print(square)
print(f)''')
print(f'function square: {square}')
print(f'function f: {f}')
print(f'in the example above we now have f which point to the memory addres of square function, so '
      f'f is equal to square function')

print(f'So far we assigned function to a variable, but we can also pass function as argument and return'
      f'function as the result of other functions')
print(f"if a function accepts other functions as arguments or returns functions as their results"
      f"that's what you call a higher order function so, first let's look at an example of passing a function as"
      f"argument to another function so a great example of this is the map function, the map function take a "
      f"function and an array as its arguments and it runs each value of that array through the provided function"
      f"and it returns a new array of those results")


# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x * x
#
#
# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# square = my_map(cube, [1, 2, 3, 4, 5])
# print(square)

print(f"\nLet's have a look at return a function from another function")
# def logger(msg):
#     def log_message():
#         print('Log:', msg)
#
#     return log_message
#
# log_hi = logger('Hi')
# log_hi()

# def html_tag(tag):
#     def wrap_text(msg):
#         print('<{0}>{1}</{0}>'.format(tag, msg))
#     return wrap_text
#
# print_h1 = html_tag('h1')
# print_h1('Test Headline!')
# print_h1('Another Headline!')
#
# print_p = html_tag('p')
# print_p('Test Paragraph!')




print('####################################################################################')
print('# 37 - Closure                                                                     #')
print('####################################################################################')
# https://www.youtube.com/watch?v=swU3c34d2NQ
print('''\nWikipedia says, "A closure is a record storing a function together with an environment:
mapping associating each free variable of the function with the value or storage location to which the name
was bound when the closure was created. A closure, unlike a plain function, allows the function to access those
captured variables through the closure's reference to them, even when the function invoked outside their scope.''')

# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func()
#
# outer_func()

print('''\n!!! We can pass function as an argument to another function we can return function and we can assign function 
to variables !!!''')

print(f"\nWhat exaclty is a closure? A closure is a record storing a function together with an environment\n "
      f"a mapping associating each free variable of the function with a value or storage location to which the name\n"
      f"was bound when the closure was created. A closure unlike plain functions allows the function to access those\n"
      f"capture variables  through the closure reference to them even when the function is invoked outside her\n"
      f"scope\n")

# exemple 1:
# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
# my_func = outer_func()
# print(my_func.__name__)
#
# my_func()
# my_func()
# my_func()

print('''you can see above that it printed out our message of Hi, but we've done with the execution of 
our outer_func() but the inner_func() that we returned still has access to that message variable that's 
printing out, so that's what a closure is''')
print('''In simple term a closure is an inner function that remembers and has access to variables in the 
local scope in which it was created even after the outer function has finished executing''')

# # exemple 2:
# def outer_func(msg):
#     message = msg
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
# hi_func = outer_func('Hi')
# hello_func = outer_func('Hello')
#
# hi_func()
# hello_func()

print("One way you can remember this (above) is that a closure closes over the free variables from their environment"
      "and in this case msg will be the free variable")

# exemple 3:
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)