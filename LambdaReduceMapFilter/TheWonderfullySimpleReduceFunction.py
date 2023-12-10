# https://www.youtube.com/watch?v=RJE2aN_capA

from functools import reduce

letters = list('abcde')
print(letters)


def rev(a: str, b: str) -> str:
    return b + a


# it is better to use lambda as we use the function only once. In a pythonic way you define a function if you use it multiple times otherwise you must prefer lambda.
result = reduce(lambda a, b: b + a, letters)
print(result)

