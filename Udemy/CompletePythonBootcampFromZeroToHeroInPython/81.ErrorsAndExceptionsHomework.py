"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478396#search
Errors and Exceptions Homework
"""


"""
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    print(i**2)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
"""
for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print(f"vous devez fournir un entier '{i}' n'est pas un entier!")

"""
Problem 2
Handle the exception thrown by the code below by susing try and excpt blocks. Then use a finally block to print 
'All Done'.
"""
print("")
x = 5
y = 0
try:
    z = x / y
except ZeroDivisionError:
    print(f"La division par 0 est impossible! Veuillez saisir une entier > 0")
finally:
    print('All Done.')

"""
Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block 
to account for incorrect inputs.
"""


def ask():
    while True:
        try:
            result = int(input("Input an integer: "))
        except ValueError:
            print("An error occured! Please try again")
            continue
        else:
            break

    print(f'Thank you, your number squared is: {result**2}')


ask()
