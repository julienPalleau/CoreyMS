# def before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print("BEFORE")
#         value = func(*args, **kwargs)
#         print("AFTER")
#         return value
#
#     return wrapper
#
#
# @before_and_after
# def greet(name):
#     print(f"Hi {name}!")
#
#
# @before_and_after
# def adder(number_1, number_2):
#     print(number_1 + number_2)
#
#
# greet("PyCon")
# print(adder(3, 10))


# import random
#
#
# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs), func(*args, **kwargs)
#     return wrapper
#
#
# @do_twice
# def roll_dice():
#     return random.randint(1, 6)
#
#
# print(roll_dice())

# import random
# import functools
#
#
# def retry(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         while (True):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 print(f"Retrying ({e})")
#     return wrapper
#
#
# @retry
# def only_roll_sixes():
#     number = random.randint(1, 6)
#     if number != 6:
#         raise ValueError(number)
#     return number
#
#
# print(only_roll_sixes())

# import functools
# import random
#
#
# def retry(exception):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             while True:
#                 try:
#                     return func(*args, **kwargs)
#                 except exception as e:
#                     print(f"Retrying ({e})")
#         return wrapper
#     return decorator
#
#
# @retry(ValueError)
# def calculation():
#     number = random.randint(-5, 5)
#     if abs(1 / number) > 0.2:
#         raise ValueError(number)
#     return number
#
#
#
# calculation()

# import random
# import functools
#
#
# def retry(max_retry):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             i = 0
#             for _ in range (max_retry - 1):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Retrying ({e})")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @retry(max_retry=3)
# def only_roll_sixes():
#     number = random.randint(1, 6)
#     if number != 6:
#         raise ValueError(number)
#     return number
#
#
# print(only_roll_sixes())
# import functools


# def before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print("BEFORE")
#         value = func(*args, **kwargs)
#         print("AFTER")
#         return value
#     return wrapper


# class BeforeAndAfter:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("BEFORE")
#         value = self.func(*args, **kwargs)
#         print("AFTER")
#         return value
#
#
# @BeforeAndAfter
# def greet(name):
#     print(f"Hi {name}!")


# greet("PyCon")

import functools
import random


class Retry:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_retries = 0

    def __call__(self, *args, **kwargs):
        while True:
            try:
                return self.func(*args, **kwargs)
            except Exception as e:
                self.num_retries += 1
                print(f"Retry attempt {self.num_retries}")


@Retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


print(only_roll_sixes)
only_roll_sixes()
print(only_roll_sixes.num_retries)
