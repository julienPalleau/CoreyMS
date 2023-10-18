"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9442692#search
Lambda Expressions Map and Filter
"""
# check map function
print("example 1")


def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

# One way is to iterate through this
for item in map(square, my_nums):
    print(item)

# Another way is if you want a lit back
print(list(map(square, my_nums)))

print("")
print("example 2")


# Another example to show that function can be more complex than the example above
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

print("")
print("exemple 3")


def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)

print("")
print("exemple 4: what is a lambda expression: ")


# ici on définit une fonction qui calcul le carre d'un nombre
def square(num):
    result = num ** 2
    return result


print(square(3))

# On peut faire la meme chose que ci-dessus avec une lambda expression. On utilise la lambda expression si on
# l'expression qu'une seule fois.
print(list(map(lambda num: num ** 2, mynums)))

print("")
print("exemple 5: Another lambda expression exemple: ")
print(list(filter(lambda num: num%2 == 0, mynums)))


print("")
print("exemple 6: Another lambda expression exemple: ")
print(names)
print(list(map(lambda x: x[0], names)))
print(list(map(lambda x: x[::-1], names)))