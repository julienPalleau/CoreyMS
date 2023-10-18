"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20548620#search
Basic Functions
"""
def say_hello(name="Lucie"):  # we set a default value here, the default value is Lucie
    print(f"hello {name}")


say_hello()
say_hello("Julien")


def add_num(num1, num2):
    return num1 + num2


result = add_num(10, 20)
print(result)


# What is the difference between printing inside the function vs returning the result ?

def print_result(a, b):
    print(a + b)


def return_result(a, b):
    return a + b


print_result(1, 20)

result = return_result(10, 20)
print(result)


def myfunc(a: int, b: int):  # here :int is to indicate what type a and b are but this is not mandatory.
    print(a + b)
    return a + b


result = myfunc(10, 40)
print(result)