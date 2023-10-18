"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9442716#search
Nested Statements and Scope
"""
print("exemple 1: LEGB")
x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

print("""
How does python actually know which x assignement I am refering to in my code?
This is because the idea of scope (LEGB):
    + L: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function.
    + E: Enclosing functions locals - Names in the local scope of any and all enclosing functions (def or lambda), from 
      inner to outer.
    + G: Global (module) - Names assigned at the top-level of a module file, or declared global in a def within the file.
    + B: Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError, ...
""")

# Exemple 2
print("example 2: Local")
lambda num: num ** 2  # num is local to this lambda expression
# GLOBAL
name = 'THIS IS A GLOBAL STRING'


def greet():
    # ENCLOSING
    name = 'Julien'

    def hello():
        # LOCAL
        name = 'IM A LOCAL'
        print('Hello ' + name)

    hello()


greet()
# so if your run the code above you get Julien, if comment the line name = 'Julien, then according LEGB rules you get
# 'THIS IS A GLOBAL STRING'. After we added name = 'IM A LOCAL' this is what will be returned by greet().

# exemple 3
print("example 3")
x = 25


def printer():
    x = 50
    return x


print(x)

# This time we get 25 and not 50!

print("")
x = 50


def func(x):
    print(f'X is {x}')

    # LOCAL REASSIGNMENT!
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')


func(x)
print(x)
# Again according LEGB rules when you declare a variable inside a function (wichi is the case of x = 200) this variable
# name only has a scope local to this function

print("")
x = 50


def func():
    global x  # this is very dangerous !!! it would be better for the function to take x as a parameter and return x
    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X TO {x}')


func()
print(x)
