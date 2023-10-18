"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9442732#search
*args and **kwargs
"""
# *args and **kwargs

def myfunc(a, b):
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


print(myfunc(40, 60))


# now with *args we can pass as many arguments we want.
def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60, 100, 1, 34))


def myfunc(*args):
    for item in args:
        print(item)


myfunc(40, 60, 100, 1, 34)


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))


myfunc(fruit='apple', veggie='lettuce')


def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')


# Exercice chapitre 50
def myfunc(mystring):
    count = 0
    result = ''
    for letter in mystring:
        if count % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()

        count += 1
    return result


print(myfunc('Anthropomorphism'))
