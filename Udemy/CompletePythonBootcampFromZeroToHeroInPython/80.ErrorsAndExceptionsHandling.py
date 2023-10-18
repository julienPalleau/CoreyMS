"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478394#search
Errors and Exception Handling:

https://docs.python.org/3.10/tutorial/errors.html?highlight=errors%20exception
https://docs.python.org/3.10/library/exceptions.html#bltin-exceptions

+ Errors are bound to happen in your codes!
+ Expecially when someone else ends up using it in an unexpected way.
+ We can use error handling to attempt to plan for possible errors.
+ For example, a user may try to write to a file that was only opened in mode='r'
+ Currently if there is any type of error in your code, the entire script will stop.
+ We can use Error Handling to let the script continue with other code, even if there is an error.
+ We use three keywords for this:
    - try: This is the block of code to be attempted (may lead to an error)
    - except: Block of code will execute in case there is an error in try block
    - finally: A final block of code to be executed, regardless of an error.
"""


# First example:
def add(n1, n2):
    print(n1 + n2)


add(10, 20)

# Second example:
try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

# Third example:
try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print('Hey you have an OS Error')
finally:
    print("I always run")

# Fourth example:
try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except:
    print('All other exceptions!')
finally:
    print("I always run")


# Fifth example
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("I'm going to ask you again! \n")


ask_for_int()
