# Working with Textual Data
# https://www.youtube.com/watch?v=k9TUPpGqYTo

print("###########################")
print(f'1 - Working with strings #')
print("###########################")

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

print("################################")
print(f'2 - Working with numeric Data #')
print("################################")
# https://www.youtube.com/watch?v=khKv-8q7YmY
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

print("##################")
print(f"3 - Comparisons #")
print("##################")
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

# https://www.pythonprogramming.in/append-a-dictionary-to-a-list-in-a-loop-python.html
print("##############################")
print(f'4 - Lists, Tuples, and Sets #')
print("##############################")
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

print('\n###################################################')
print('# 5 - Dictionaries - Working with Key-Value Pairs #')
print('###################################################')
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
student['phone']='555-5555'
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
print(f'a == b: {a==b}')

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